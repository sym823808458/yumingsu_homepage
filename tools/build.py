"""Build the bilingual static website with Python's standard library only.

Run: python tools/build.py
Check generated pages: python tools/build.py --check
"""
import argparse
import hashlib
import html
import json
import re
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parents[1]
E = html.escape
DEFAULT_LANGUAGE = 'en'


def language_root(lang):
    return '' if lang == DEFAULT_LANGUAGE else 'zh/'


def software_name(project, lang):
    return project.get('name_' + lang, project['name'])

TEXT = {
    'zh': {
        'skip': '跳至正文', 'navigation': '主导航', 'about': '关于我', 'research': '研究', 'software': '软件', 'publications': '论文', 'contact': '联系',
        'title': '苏禹铭 Yuming Su · 个人学术主页', 'description': '苏禹铭的个人学术主页：可解释化学机器学习、自动化电化学、双光子吸收，以及科研软件与论文。',
        'hero': '用可解释的模型理解化学，<br>用自动化实验探索材料。', 'eyebrow': '化学 · 机器学习 · 自动化', 'portrait_caption': '化学 × 数据 × 实验',
        'email': '邮件', 'citations': '总引用', 'hindex': 'h 指数', 'i10index': 'i10 指数',
        'snapshot': 'Google Scholar 快照', 'snapshot_note': '截至 {date} · 非实时统计',
        'about_title': '连接化学、数据与实验', 'about_kicker': '关于我 · 学术背景',
        'research_title': '研究方向', 'research_kicker': '研究 · 问题与方法',
        'software_title': '让方法成为可用的工具', 'software_kicker': '软件 · 科研工具', 'software_view': '了解项目 ↗',
        'pub_title': '论文与学术成果', 'pub_kicker': '学术论文 · 研究成果', 'full_list': '完整学术列表 ↗',
        'pub_intro': '收录部分期刊论文、预印本与软件资源。引用次数采用 {date} 的 Google Scholar 快照；本页记录数不代表全部论文数。',
        'search': '搜索标题、作者或期刊', 'all_years': '全部年份', 'newest': '按年份排序', 'most_cited': '按引用排序',
        'all': '全部记录', 'selected': '代表作', 'results': '显示 {count} / {total} 条记录', 'empty': '没有匹配的记录，请调整搜索或筛选条件。',
        'cited': '次引用', 'featured': '代表作', 'journal': '期刊论文', 'preprint': '预印本', 'resource': '软件资源', 'paper_link': '查看论文 ↗',
        'contact_title': '欢迎交流与合作', 'contact_text': '围绕可解释机器学习、化学材料与自动化实验，探索共同感兴趣的问题。',
        'updated': '更新于', 'source': '网站源码', 'home': '首页', 'code': '源码仓库 ↗', 'docs': '使用手册 ↗', 'download': '下载软件 ↗',
        'related': '相关研究', 'project_info': '项目信息', 'back': '全部软件', 'project_note': '软件在用户自己的环境中运行。本页提供介绍、手册与代码入口。', 'quick_start': '快速安装',
    },
    'en': {
        'skip': 'Skip to content', 'navigation': 'Main navigation', 'about': 'About', 'research': 'Research', 'software': 'Software', 'publications': 'Publications', 'contact': 'Contact',
        'title': 'Yuming Su · Chemistry, Machine Learning & Automation', 'description': 'Yuming Su: interpretable chemical machine learning, automated electrochemistry, two-photon absorption, research software and publications.',
        'hero': 'Understanding chemistry with interpretable models.<br>Exploring materials through automated experiments.', 'eyebrow': 'CHEMISTRY · MACHINE LEARNING · AUTOMATION', 'portrait_caption': 'CHEMISTRY × DATA × EXPERIMENTS',
        'email': 'Email', 'citations': 'Citations', 'hindex': 'h-index', 'i10index': 'i10-index',
        'snapshot': 'Google Scholar snapshot', 'snapshot_note': 'As of {date} · not a live feed',
        'about_title': 'Connecting chemistry, data & experiments', 'about_kicker': 'ABOUT / BACKGROUND',
        'research_title': 'Research interests', 'research_kicker': 'RESEARCH / QUESTIONS & METHODS',
        'software_title': 'From methods to usable tools', 'software_kicker': 'SOFTWARE / RESEARCH TOOLS', 'software_view': 'Explore ↗',
        'pub_title': 'Publications & scholarly work', 'pub_kicker': 'PUBLICATIONS / RESEARCH OUTPUTS', 'full_list': 'Full list on Scholar ↗',
        'pub_intro': 'A selection of journal articles, preprints and software resources. Citation counts are a Google Scholar snapshot dated {date}; listed records are not the total publication count.',
        'search': 'Search titles, authors or journals', 'all_years': 'All years', 'newest': 'Newest first', 'most_cited': 'Most cited',
        'all': 'All records', 'selected': 'Selected work', 'results': 'Showing {count} of {total} records', 'empty': 'No matching records. Try another search or filter.',
        'cited': 'citations', 'featured': 'Selected', 'journal': 'Journal article', 'preprint': 'Preprint', 'resource': 'Software resource', 'paper_link': 'Read paper ↗',
        'contact_title': 'Let’s explore a question together.', 'contact_text': 'Open to conversations on interpretable machine learning, chemistry, materials and automated experiments.',
        'updated': 'Updated', 'source': 'Website source', 'home': 'Home', 'code': 'Source code ↗', 'docs': 'Documentation ↗', 'download': 'Download ↗',
        'related': 'Related research', 'project_info': 'Project information', 'back': 'All software', 'project_note': 'Software runs in the user’s own environment. This page provides information, documentation and source links.', 'quick_start': 'Quick install',
    },
}

def load(name):
    return json.loads((ROOT / 'data' / (name + '.json')).read_text(encoding='utf-8'))

def inline(text):
    text = E(text)
    def link(match):
        label, url = match.groups()
        if not url.startswith(('https://', 'http://', 'mailto:')):
            raise ValueError('Unsupported Markdown link: ' + url)
        return f'<a href="{url}">{label}</a>'
    text = re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)', link, text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)

def markdown(path):
    """Supported authoring subset: paragraphs, ##/###, lists, links, bold, code."""
    result, paragraph, in_list = [], [], False
    def flush():
        if paragraph:
            result.append('<p>' + inline(' '.join(paragraph)) + '</p>')
            paragraph.clear()
    for raw in path.read_text(encoding='utf-8').splitlines() + ['']:
        line = raw.strip()
        if not line:
            flush()
            if in_list:
                result.append('</ul>')
                in_list = False
        elif line.startswith('## '):
            flush()
            result.append('<h2>' + inline(line[3:]) + '</h2>')
        elif line.startswith('### '):
            flush()
            result.append('<h3>' + inline(line[4:]) + '</h3>')
        elif line.startswith('- '):
            flush()
            if not in_list:
                result.append('<ul>')
                in_list = True
            result.append('<li>' + inline(line[2:]) + '</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            paragraph.append(line)
    return '\n'.join(result)

def tags(values):
    return '<div class="tags">' + ''.join(f'<span class="tag">{E(v)}</span>' for v in values) + '</div>'


def localized_tags(record, lang):
    return tags(record.get('tags_zh', record['tags']) if lang == 'zh' else record['tags'])

def heading(kicker, title, extra=''):
    return f'<div class="section-head"><div><p class="section-kicker">{E(kicker)}</p><h2>{E(title)}</h2></div>{extra}</div>'

def authors(paper):
    values = paper.get('authors_verified', [])
    text = ', '.join(values) if values else paper['authors']
    text = E(text)
    return re.sub(r'(?<![\w])(?:Yuming Su|Y\. M\. Su|Y\. Su)(?![\w])', r'<span class="author-self">\g<0></span>', text)

def publication(paper, t, lang):
    link = 'https://doi.org/' + paper['doi'] if paper.get('doi') else paper.get('url', '')
    if not link:
        link = 'https://scholar.google.com/scholar?q=' + __import__('urllib.parse', fromlist=['quote']).quote(paper['title'])
    search = E(' '.join([paper['title'], paper['authors'], ' '.join(paper.get('authors_verified', [])), paper['venue'], paper.get('doi','')]).lower(), quote=True)
    venue = paper.get('venue_zh', paper['venue']) if lang == 'zh' else paper['venue']
    details = paper.get('details_zh', paper['details']) if lang == 'zh' else paper['details']
    selected = f'<span class="pub-featured">{t["featured"]}</span>' if paper.get('featured') else ''
    link_label = 'DOI ↗' if paper.get('doi') else t['paper_link']
    return f'''<li class="publication" id="{E(paper['id'])}" data-publication data-year="{paper['year']}" data-citations="{paper['citations']}" data-featured="{str(paper.get('featured',False)).lower()}" data-search="{search}">
      <div class="pub-year">{paper['year']}</div><div>
      <a class="pub-title" href="{E(link)}" lang="en">{E(paper['title'])}</a>
      <p class="pub-authors">{authors(paper)}</p>
      <p class="pub-venue"><em>{E(venue)}</em> · {E(details)}</p>
      <div class="pub-links"><span class="pub-type">{t[paper['type']]}</span><a href="{E(link)}">{link_label}</a>{selected}</div></div>
      <div class="pub-citations"><strong>{paper['citations']}</strong>{t['cited']}</div></li>'''

def home_body(profile, papers, software, lang, prefix):
    t = TEXT[lang]
    links = profile['links']
    snapshot = profile['scholar_snapshot']
    contacts = [(t['email'], 'mailto:' + profile['email']), ('Google Scholar', links['scholar']), ('GitHub', links['github']), ('ORCID', links['orcid'])]
    contact_links = ''.join(f'<a href="{E(url)}">{E(name)} ↗</a>' for name,url in contacts)
    metrics = ''.join(f'<div class="metric"><strong>{snapshot[key]}</strong><span>{t[label]}</span></div>' for key,label in [('citations','citations'),('h_index','hindex'),('i10_index','i10index')])
    timeline = ''.join(f'<div class="timeline-item" id="{["work","education","education-bachelors"][i]}"><div class="timeline-period">{E(x["period"])}</div><div class="timeline-title">{E(x["title"][lang])}</div><div class="timeline-place">{E(x["institution"][lang])}</div></div>' for i,x in enumerate(profile['experience']))
    research = ''.join(f'<article class="research-item"><div class="research-number">{x["number"]}</div><h3>{E(x["title"][lang])}</h3><p>{E(x["text"][lang])}</p>{localized_tags(x,lang)}</article>' for x in profile['research'])
    rows = ''.join(f'<article class="software-row"><span class="software-index">{i:02d}</span><div><a class="software-name" href="software/{s["slug"]}/">{E(software_name(s,lang))}</a><div class="software-category">{E(s["category"][lang])}</div></div><p class="software-summary">{E(s["summary"][lang])}</p><a class="text-link" href="software/{s["slug"]}/">{t["software_view"]}<span class="sr-only"> {E(software_name(s,lang))}</span></a></article>' for i,s in enumerate(software,1))
    ordered = sorted(papers, key=lambda p:(p['year'],p['citations']), reverse=True)
    pub_rows = ''.join(publication(p,t,lang) for p in ordered)
    years = ''.join(f'<option value="{y}">{y}</option>' for y in sorted({p['year'] for p in papers}, reverse=True))
    # 2013 is retained only as the date of the supplied software-resource record.
    count = t['results'].format(count=len(papers),total=len(papers))
    return f'''<div class="container">
      <section id="home" class="hero" aria-label="Yuming Su">
        <div class="hero-main"><div class="hero-intro"><div class="eyebrow">{t['eyebrow']}</div>
          <h1>Yuming Su<span class="chinese-name">苏禹铭</span></h1><p class="role">{E(profile['position'][lang])}</p>
          <p class="affiliation">{E(profile['affiliation'][lang])}<br>{E(profile['location'][lang])}</p></div>
          <p class="hero-description">{t['hero']}</p><div class="contact-links">{contact_links}</div></div>
        <div class="portrait-wrap"><img class="profile-photo" src="{prefix}images/profile.jpg" alt="Yuming Su / 苏禹铭" width="240" height="278"><p class="portrait-caption">{t['portrait_caption']}</p></div>
      </section>
      <div class="metrics-band" aria-label="{t['snapshot']}">{metrics}<div class="metrics-note"><a href="{E(links['scholar'])}">{t['snapshot']} ↗</a><br>{E(t['snapshot_note'].format(date=snapshot['date']))}</div></div>
      <section class="section" id="about">{heading(t['about_kicker'],t['about_title'])}<div class="about-layout"><div class="prose">{markdown(ROOT/'content'/f'about.{lang}.md')}</div><div class="timeline">{timeline}</div></div></section>
      <section class="section" id="research">{heading(t['research_kicker'],t['research_title'])}<div class="research-grid">{research}</div></section>
      <section class="section" id="software">{heading(t['software_kicker'],t['software_title'],f'<a class="section-link" href="{E(links["github"])}">GitHub ↗</a>')}<div class="software-list">{rows}</div></section>
      <section class="section" id="publications">{heading(t['pub_kicker'],t['pub_title'],f'<a class="section-link" href="{E(links["scholar"])}">{t["full_list"]}</a>')}
        <p class="publication-intro">{E(t['pub_intro'].format(date=snapshot['date']))}</p>
        <div class="publication-toolbar"><div class="search-wrap"><label class="sr-only" for="publication-search">{t['search']}</label><input type="search" id="publication-search" placeholder="{t['search']}" autocomplete="off"></div>
        <label class="sr-only" for="publication-year">{t['all_years']}</label><select id="publication-year" class="filter-select"><option value="">{t['all_years']}</option>{years}</select>
        <label class="sr-only" for="publication-sort">{t['newest']}</label><select id="publication-sort" class="filter-select"><option value="year">{t['newest']}</option><option value="citations">{t['most_cited']}</option></select>
        <div class="pub-tabs"><button type="button" data-publication-mode="all" aria-pressed="true">{t['all']}</button><button type="button" data-publication-mode="selected" aria-pressed="false">{t['selected']}</button></div></div>
        <p class="result-count" id="publication-count" aria-live="polite" data-template="{E(t['results'])}">{count}</p>
        <ol class="publication-list" data-publications>{pub_rows}</ol><p id="publication-empty" class="empty-state" hidden>{t['empty']}</p>
      </section>
      <section class="contact-section" id="contact"><div><p class="section-kicker">{t['contact']}</p><h2>{t['contact_title']}</h2><p>{t['contact_text']}</p></div><a class="button" href="mailto:{E(profile['email'])}">{E(profile['email'])} <span aria-hidden="true">↗</span></a></section>
    </div>'''

def project_body(project, papers, lang, home):
    t = TEXT[lang]
    buttons = f'<a class="button" href="{E(project["repository"])}">{t["code"]}</a>'
    docs = project.get('docs_en' if lang=='en' else 'docs')
    if docs:
        buttons += f'<a class="button secondary" href="{E(docs)}">{t["docs"]}</a>'
    if project.get('download'):
        buttons += f'<a class="button secondary" href="{E(project["download"])}">{t["download"]}</a>'
    related = ''
    for paper_id in project['related_publications']:
        p = next(p for p in papers if p['id']==paper_id)
        related += f'<a class="pub-title" lang="en" href="{home}#{E(p["id"])}">{E(p["title"])} ({p["year"]}) ↗</a>'
    related_block = f'<h2>{t["related"]}</h2>{related}' if related else ''
    quick = f'<p class="workflow-label">{t["quick_start"]}</p><p><code>{E(project["command"])}</code></p>' if project.get('command') else ''
    return f'''<div class="container"><section class="project-hero"><div class="breadcrumb"><a href="{home}">{t['home']}</a> / <a href="{home}#software">{t['back']}</a> / {E(software_name(project,lang))}</div><div class="eyebrow">{E(project['category'][lang])}</div><h1>{E(software_name(project,lang))}</h1><p class="project-lead">{E(project['summary'][lang])}</p>{localized_tags(project,lang)}<div class="project-buttons">{buttons}</div></section>
      <div class="project-layout"><article class="prose project-prose">{markdown(ROOT/'content/software'/f'{project["slug"]}.{lang}.md')}</article><aside class="project-aside"><h2>{t['project_info']}</h2><p>{t['project_note']}</p>{quick}{related_block}</aside></div></div>'''

def validate(profile, papers, software):
    if len({p['id'] for p in papers}) != len(papers):
        raise ValueError('Duplicate publication id')
    if len({s['slug'] for s in software}) != len(software):
        raise ValueError('Duplicate software slug')
    for p in papers:
        for field in ['title','authors','venue','details','year','citations','type']:
            if field not in p:
                raise ValueError(f'Missing {field}: {p["id"]}')
        if p['type'] not in ('journal','preprint','resource') or p['citations'] < 0:
            raise ValueError('Invalid publication record: ' + p['id'])
    for s in software:
        if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',s['slug']):
            raise ValueError('Invalid software slug')
        for lang in TEXT:
            if not (ROOT/'content/software'/f'{s["slug"]}.{lang}.md').exists():
                raise ValueError('Missing software Markdown')
        for p in s['related_publications']:
            if p not in {x['id'] for x in papers}:
                raise ValueError('Unknown related publication: ' + p)
    if not (ROOT/'images/profile.jpg').exists():
        raise ValueError('Missing portrait')

def build(check=False):
    profile, papers, software = load('profile'), load('publications'), load('software')
    validate(profile,papers,software)
    template = Template((ROOT/'templates/base.html').read_text(encoding='utf-8'))
    asset_text = (ROOT/'assets/site.css').read_text(encoding='utf-8') + (ROOT/'assets/site.js').read_text(encoding='utf-8')
    asset_version = hashlib.sha256(asset_text.encode('utf-8')).hexdigest()[:12]
    outputs = {}
    for lang,t in TEXT.items():
        locale_path = Path(language_root(lang))
        for project in [None] + software:
            path = locale_path / ('software/'+project['slug'] if project else '') / 'index.html'
            depth = len(path.parts)-1
            prefix = '../'*depth if depth else './'
            home = prefix + language_root(lang)
            other = 'zh' if lang=='en' else 'en'
            language_url = prefix + language_root(other) + ('software/'+project['slug']+'/' if project else '')
            nav = ''.join(f'<a href="{home}#{section}">{t[section]}</a>' for section in ['about','research','software','publications','contact'])
            body = project_body(project,papers,lang,home) if project else home_body(profile,papers,software,lang,prefix)
            outputs[path] = template.substitute(
                html_lang='zh-CN' if lang=='zh' else 'en',title=E(software_name(project,lang)+' · Yuming Su' if project else t['title']),
                description=E(project['summary'][lang] if project else t['description']),prefix=prefix,asset_version=asset_version,skip=t['skip'],navigation=t['navigation'],home=home,nav=nav,
                language_url=language_url,other_lang='en' if other=='en' else 'zh-CN',language_label='English' if lang=='zh' else '中文',body=body,
                year=profile['updated'][:4],updated_label=t['updated'],updated=profile['updated'],source_label=t['source'])
    # Preserve previously shared /en/ URLs as redirects to the English primary routes.
    for project in [None] + software:
        path = Path('en') / ('software/'+project['slug'] if project else '') / 'index.html'
        prefix = '../' * (len(path.parts)-1)
        target = prefix + ('software/'+project['slug']+'/' if project else '')
        outputs[path] = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>Yuming Su — English website</title>
<meta http-equiv="refresh" content="0;url={E(target)}">
<script>location.replace({json.dumps(target)} + location.search + location.hash);</script></head>
<body><p><a href="{E(target)}">Continue to the English website</a></p></body></html>
'''
    outputs[Path('.nojekyll')] = ''
    differences = []
    for path,content in outputs.items():
        target = ROOT/path
        if check:
            if not target.exists() or target.read_text(encoding='utf-8') != content:
                differences.append(str(path))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content,encoding='utf-8',newline='\n')
    if differences:
        raise SystemExit('Generated files are out of date: '+', '.join(differences))
    print(f'{"Checked" if check else "Built"} {len(outputs)-1} HTML pages; {len(papers)} scholarly records; {len(software)} software projects.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    build(parser.parse_args().check)
