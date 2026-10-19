"""Check generated pages, local links, fragments, and basic content integrity."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self,path):
        super().__init__()
        self.path=path
        self.ids=set()
        self.links=[]
        self.title=False
        self.language=False
        self.publications=0
        self.errors=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids:
                self.errors.append('duplicate id '+a['id'])
            self.ids.add(a['id'])
        if tag=='html': self.language=bool(a.get('lang'))
        if tag=='title': self.title=True
        if tag=='img' and not a.get('alt'): self.errors.append('image missing alt')
        if 'data-publication' in a: self.publications+=1
        for attribute in ('href','src'):
            if a.get(attribute): self.links.append(a[attribute])

def main():
    pages={}
    for path in [ROOT/'index.html',*(ROOT/'en').rglob('*.html'),*(ROOT/'zh').rglob('*.html'),*(ROOT/'software').rglob('*.html')]:
        parser=Page(path)
        parser.feed(path.read_text(encoding='utf-8'))
        pages[path.resolve()]=parser
    errors=[]
    for path,page in pages.items():
        if not page.title or not page.language: page.errors.append('missing title or language')
        for link in page.links:
            parts=urlsplit(link)
            if parts.scheme or parts.netloc: continue
            target=(path.parent/unquote(parts.path)).resolve() if parts.path else path
            if target.is_dir(): target=target/'index.html'
            if not target.is_relative_to(ROOT):
                page.errors.append('link escapes site root: '+link)
            elif not target.exists():
                page.errors.append('missing local target: '+link)
            elif parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
                page.errors.append('missing fragment: '+link)
        errors.extend(f'{path.relative_to(ROOT)}: {e}' for e in page.errors)
    papers=json.loads((ROOT/'data/publications.json').read_text(encoding='utf-8'))
    for path in (ROOT/'index.html',ROOT/'zh/index.html'):
        if pages[path.resolve()].publications!=len(papers): errors.append('incomplete publication rendering: '+str(path))
    if errors: raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} pages, all local links/fragments, image alt text and {len(papers)} scholarly records in both languages.')

if __name__=='__main__': main()
