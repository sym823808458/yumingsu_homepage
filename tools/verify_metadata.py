"""One-off Crossref metadata audit. Never called by the offline site build."""
import concurrent.futures
import difflib
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def norm(value):
    return re.sub(r"[^a-z0-9]", "", value.lower())

def audit(paper):
    if paper['type'] != 'journal':
        return paper, 'skipped non-journal'
    if paper.get('doi'):
        url = 'https://api.crossref.org/works/' + urllib.parse.quote(paper['doi'], safe='')
    else:
        url = 'https://api.crossref.org/works?' + urllib.parse.urlencode({'query.title': paper['title'], 'rows': 1})
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'YumingSuHomepageMetadataAudit/1.0'})
        with urllib.request.urlopen(request, timeout=35) as response:
            message = json.load(response)['message']
        item = message if paper.get('doi') else message['items'][0]
        title = re.sub('<[^>]+>', '', item['title'][0])
        score = difflib.SequenceMatcher(None, norm(title), norm(paper['title'])).ratio()
        if score < .85:
            return paper, f'REVIEW title match {score:.2f}: {title}'
        paper['doi'] = item['DOI']
        paper['metadata_source'] = 'https://api.crossref.org/works/' + item['DOI']
        paper['metadata_checked'] = '2026-10-19'
        paper['authors_verified'] = [f"{a.get('given', '')} {a.get('family', '')}".strip() for a in item.get('author', [])]
        parts = [item.get('volume', '')]
        if item.get('issue'):
            parts[0] += ' (' + item['issue'] + ')'
        parts.append(item.get('page', item.get('article-number', '')))
        verified_details = ', '.join(p for p in parts if p)
        change = ''
        if verified_details and norm(verified_details) != norm(paper['details']):
            change = f"; details {paper['details']} -> {verified_details}"
            paper['details'] = verified_details
        return paper, f'verified {item["DOI"]}{change}'
    except Exception as error:
        return paper, 'UNVERIFIED: ' + str(error)

if __name__ == '__main__':
    path = ROOT / 'data/publications.json'
    papers = json.loads(path.read_text(encoding='utf-8'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(audit, papers))
    path.write_text(json.dumps([p for p, _ in results], ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for paper, status in results:
        print(paper['id'] + ': ' + status)
