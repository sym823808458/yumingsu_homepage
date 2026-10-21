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
        'pub_intro': '优先展示第一作者（含共同一作）及通讯作者论文，其余按引用次数排序。引用快照截至 {date}；新增论文未核实的引用数标为“未记录”。完整列表见 Google Scholar。',
        'results_selected': '展示 {count} 篇论文',
        'static_papers': '当前展示 10 篇论文，完整列表请访问 Google Scholar。',
        'first': '第一作者', 'co_first': '共同第一作者', 'corresponding': '通讯作者', 'co_corresponding': '共同通讯作者', 'citation_unknown': '未记录',
        'cited': '次引用', 'featured': '代表作', 'journal': '期刊论文', 'preprint': '预印本', 'resource': '软件资源', 'paper_link': '查看论文 ↗',
        'contact_title': '欢迎交流与合作', 'contact_text': '围绕可解释机器学习、化学材料与自动化实验，探索共同感兴趣的问题。',
        'updated': '更新于', 'source': '网站源码', 'home': '首页', 'code': '源码仓库 ↗', 'docs': '使用手册 ↗', 'download': '下载软件 ↗',
        'related': '相关研究', 'project_info': '项目信息', 'back': '全部软件', 'project_note': '软件在用户自己的环境中运行。本页提供介绍、手册与代码入口。', 'quick_start': '快速安装',
        'contact_project': '联系了解软件 ↗', 'stage': '开发阶段', 'availability': '获取方式',
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
        'pub_intro': 'First-author (including co-first) and corresponding-author papers are shown first; other papers follow by citation count. Citation snapshot: {date}. Counts not verified for newly added papers are marked as not recorded. See Google Scholar for the full list.',
        'results_selected': 'Showing {count} papers',
        'static_papers': 'Ten papers are shown. Visit Google Scholar for the full list.',
        'first': 'First author', 'co_first': 'Co-first author', 'corresponding': 'Corresponding author', 'co_corresponding': 'Co-corresponding author', 'citation_unknown': 'Not recorded',
        'cited': 'citations', 'featured': 'Selected', 'journal': 'Journal article', 'preprint': 'Preprint', 'resource': 'Software resource', 'paper_link': 'Read paper ↗',
        'contact_title': 'Let’s explore a question together.', 'contact_text': 'Open to conversations on interpretable machine learning, chemistry, materials and automated experiments.',
        'updated': 'Updated', 'source': 'Website source', 'home': 'Home', 'code': 'Source code ↗', 'docs': 'Documentation ↗', 'download': 'Download ↗',
        'related': 'Related research', 'project_info': 'Project information', 'back': 'All software', 'project_note': 'Software runs in the user’s own environment. This page provides information, documentation and source links.', 'quick_start': 'Quick install',
        'contact_project': 'Discuss this software ↗', 'stage': 'Development stage', 'availability': 'Availability',
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
    return re.sub(r'(?<![\w])(?:Yuming Su|Yu-Ming Su|Y\. M\. Su|Y\. Su)(?![\w])', r'<span class="author-self">\g<0></span>', text)

def publication(paper, t, lang, hidden=False):
    link = 'https://doi.org/' + paper['doi'] if paper.get('doi') else paper.get('url', '')
    if not link:
        link = 'https://scholar.google.com/scholar?q=' + __import__('urllib.parse', fromlist=['quote']).quote(paper['title'])
    venue = paper.get('venue_zh', paper['venue']) if lang == 'zh' else paper['venue']
    details = paper.get('details_zh', paper['details']) if lang == 'zh' else paper['details']
    link_label = 'DOI ↗' if paper.get('doi') else t['paper_link']
    role_labels = ''.join(f'<span class="pub-type pub-role">{E(t[role])}</span>' for role in paper.get('author_roles', []))
    citations = paper['citations'] if paper['citations'] is not None else '—'
    citation_label = t['cited'] if paper['citations'] is not None else t['citation_unknown']
    return f'''<li class="publication" id="{E(paper['id'])}" data-publication{' hidden' if hidden else ''}>
      <div class="pub-year">{paper['year']}</div><div>
      <a class="pub-title" href="{E(link)}" lang="en">{E(paper['title'])}</a>
      <p class="pub-authors">{authors(paper)}</p>
      <p class="pub-venue"><em>{E(venue)}</em> · {E(details)}</p>
      <div class="pub-links">{role_labels}<span class="pub-type">{t[paper['type']]}</span><a href="{E(link)}">{link_label}</a></div></div>
      <div class="pub-citations"><strong>{citations}</strong>{citation_label}</div></li>'''

def research_item(item, papers, lang, prefix):
    figure = item['figure']
    source = prefix + figure['src']
    image_version = hashlib.sha256((ROOT/figure['src']).read_bytes()).hexdigest()[:12]
    image_url = source + '?v=' + image_version
    paper = next(p for p in papers if p['id'] == item['publication_id'])
    view_label = '查看完整图片 ↗' if lang == 'zh' else 'View full figure ↗'
    paper_label = '代表论文' if lang == 'zh' else 'Representative paper'
    return f'''<article class="research-item">
      <figure class="research-figure"><a class="research-image-link" href="{E(image_url)}" target="_blank" rel="noopener" aria-label="{E(view_label+': '+figure['alt'][lang])}">
        <img src="{E(image_url)}" alt="{E(figure['alt'][lang])}" width="{int(figure['width'])}" height="{int(figure['height'])}" loading="lazy">
        <span class="research-image-action">{view_label}</span></a>
        <figcaption>{E(figure['caption'][lang])}<span class="research-credit"><a href="{E(figure['source'])}">{E(figure['attribution'])}</a> · <a href="{E(figure['license_url'])}">{E(figure['license'])}</a></span></figcaption>
      </figure>
      <div class="research-copy"><div class="research-number">{E(item['number'])}</div><h3>{E(item['title'][lang])}</h3><p>{E(item['text'][lang])}</p>{localized_tags(item,lang)}
        <div class="research-paper"><span>{paper_label}</span><a href="https://doi.org/{E(paper['doi'])}" lang="en">{E(paper['title'])} ↗</a></div>
      </div></article>'''


def software_row(project, index, lang):
    name = E(software_name(project, lang))
    online = project.get('online')
    badge = ''
    if online:
        label = E(online['label'][lang])
        badge = f'<a class="software-online" href="{E(online["url"])}" aria-label="{name}: {label}">{label} <span aria-hidden="true">↗</span></a>'
    return f'<article class="software-row"><span class="software-index">{index:02d}</span><div><div class="software-title"><a class="software-name" href="software/{project["slug"]}/">{name}</a>{badge}</div><div class="software-category">{E(project["category"][lang])}</div></div><p class="software-summary">{E(project["summary"][lang])}</p><a class="text-link" href="software/{project["slug"]}/">{TEXT[lang]["software_view"]}<span class="sr-only"> {name}</span></a></article>'


def home_body(profile, papers, software, lang, prefix):
    t = TEXT[lang]
    portrait_version = hashlib.sha256((ROOT/'images/profile.jpg').read_bytes()).hexdigest()[:12]
    links = profile['links']
    snapshot = profile['scholar_snapshot']
    contacts = [(t['email'], 'mailto:' + profile['email']), ('Google Scholar', links['scholar']), ('GitHub', links['github']), ('ORCID', links['orcid'])]
    contact_links = ''.join(f'<a href="{E(url)}">{E(name)} ↗</a>' for name,url in contacts)
    metrics = ''.join(f'<div class="metric"><strong>{snapshot[key]}</strong><span>{t[label]}</span></div>' for key,label in [('citations','citations'),('h_index','hindex'),('i10_index','i10index')])
    timeline = ''.join(f'<div class="timeline-item" id="{["work","education","education-bachelors"][i]}"><div class="timeline-period">{E(x["period"])}</div><div class="timeline-title">{E(x["title"][lang])}</div><div class="timeline-place">{E(x["institution"][lang])}</div></div>' for i,x in enumerate(profile['experience']))
    research = ''.join(research_item(item,papers,lang,prefix) for item in profile['research'])
    rows = ''.join(software_row(s,i,lang) for i,s in enumerate(software,1))
    online_note = ''
    if any(s.get('online') for s in software):
        note = '线上体验免费，须注册、验证邮箱并经管理员批准。' if lang == 'zh' else 'Online trials are free to use; email verification and administrator approval are required.'
        online_note = f'<p class="software-online-note">{note}</p>'
    # Software-resource records stay in the data archive, not the paper display.
    ordered = sorted((p for p in papers if p['type'] != 'resource'), key=lambda p:(p.get('display_priority', 100000), -(p['citations'] if p['citations'] is not None else -1), -p['year']))
    pub_rows = ''.join(publication(p,t,lang,hidden=i>=10) for i,p in enumerate(ordered))
    count = t['results_selected'].format(count=min(10,len(ordered)))
    return f'''<div class="container">
      <section id="home" class="hero" aria-label="Yuming Su">
        <div class="hero-main"><div class="hero-intro"><div class="eyebrow">{t['eyebrow']}</div>
          <h1>Yuming Su<span class="chinese-name">苏禹铭</span></h1><p class="role">{E(profile['position'][lang])}</p>
          <p class="affiliation">{E(profile['affiliation'][lang])}<br>{E(profile['location'][lang])}</p></div>
          <p class="hero-description">{t['hero']}</p><div class="contact-links">{contact_links}</div></div>
        <figure class="portrait-wrap"><div class="portrait-frame"><img class="profile-photo" src="{prefix}images/profile.jpg?v={portrait_version}" alt="Yuming Su / 苏禹铭" width="886" height="1067"></div></figure>
      </section>
      <div class="metrics-band" aria-label="{t['snapshot']}">{metrics}<div class="metrics-note"><a href="{E(links['scholar'])}">{t['snapshot']} ↗</a><br>{E(t['snapshot_note'].format(date=snapshot['date']))}</div></div>
      <section class="section" id="about">{heading(t['about_kicker'],t['about_title'])}<div class="about-layout"><div class="prose">{markdown(ROOT/'content'/f'about.{lang}.md')}</div><div class="timeline">{timeline}</div></div></section>
      <section class="section" id="research">{heading(t['research_kicker'],t['research_title'])}<div class="research-grid">{research}</div></section>
      <section class="section" id="software">{heading(t['software_kicker'],t['software_title'],f'<a class="section-link" href="{E(links["github"])}">GitHub ↗</a>')}{online_note}<div class="software-list">{rows}</div></section>
      <section class="section" id="publications">{heading(t['pub_kicker'],t['pub_title'],f'<a class="section-link" href="{E(links["scholar"])}">{t["full_list"]}</a>')}
        <p class="publication-intro">{E(t['pub_intro'].format(date=snapshot['date']))}</p>
        <p class="result-count" id="publication-count" aria-live="polite" data-template="{E(t['results_selected'])}">{count}</p>
        <ol class="publication-list" data-publications>{pub_rows}</ol><noscript><p class="result-count">{t['static_papers']}</p></noscript>
      </section>
      <section class="contact-section" id="contact"><div><p class="section-kicker">{t['contact']}</p><h2>{t['contact_title']}</h2><p>{t['contact_text']}</p></div><a class="button" href="mailto:{E(profile['email'])}">{E(profile['email'])} <span aria-hidden="true">↗</span></a></section>
    </div>'''

def project_media(project, lang, prefix):
    blocks = []
    for item in project.get('media', []):
        source = item['src'][lang] if isinstance(item['src'], dict) else item['src']
        picture = f'<img src="{E(prefix+source)}" width="{int(item["width"])}" height="{int(item["height"])}" alt="{E(item["alt"][lang])}" loading="lazy">'
        if item.get('mobile_src'):
            mobile = item['mobile_src'][lang] if isinstance(item['mobile_src'],dict) else item['mobile_src']
            picture = f'<picture><source media="(max-width:700px)" srcset="{E(prefix+mobile)}" width="{int(item["mobile_width"])}" height="{int(item["mobile_height"])}">{picture}</picture>'
        figure = f'<figure class="project-media"><div class="project-media-image">{picture}</div><figcaption>{E(item["caption"][lang])}</figcaption></figure>'
        if item.get('type') == 'animation':
            blocks.append(f'<details class="project-animation"><summary>{E(item["label"][lang])}</summary>{figure}</details>')
        else:
            blocks.append(figure)
    return '<section class="project-showcase">' + ''.join(blocks) + '</section>' if blocks else ''


def project_body(project, papers, lang, home, prefix, email):
    t = TEXT[lang]
    buttons = ''
    if project.get('repository'):
        buttons += f'<a class="button" href="{E(project["repository"])}">{t["code"]}</a>'
    if project.get('contact'):
        buttons += f'<a class="button" href="mailto:{E(email)}">{t["contact_project"]}</a>'
    docs = project.get('docs_en' if lang=='en' else 'docs')
    if docs:
        buttons += f'<a class="button secondary" href="{E(docs)}">{t["docs"]}</a>'
    if project.get('download'):
        buttons += f'<a class="button secondary" href="{E(project["download"])}">{t["download"]}</a>'
    if project.get('preprint'):
        label = '预印本' if lang == 'zh' else 'Preprint'
        buttons += f'<a class="button secondary" href="{E(project["preprint"])}">{label}</a>'
    online_note = ''
    if project.get('online'):
        online = project['online']
        label = '在线计算演示' if lang == 'zh' else 'Online compute demo'
        buttons += f'<a class="button secondary" href="{E(online["url"])}">{label}</a>'
        online_note = f'<p class="project-status">{E(online["note"][lang])}</p>'
    related = ''
    for paper_id in project['related_publications']:
        p = next(p for p in papers if p['id']==paper_id)
        related += f'<a class="pub-title" lang="en" href="{home}#{E(p["id"])}">{E(p["title"])} ({p["year"]}) ↗</a>'
    related_block = f'<h2>{t["related"]}</h2>{related}' if related else ''
    project_note = ('在线任务由独立计算服务为已批准账户运行；此页提供说明及本地工作流链接。' if lang == 'zh' else 'Online tasks run on a separate compute service for approved accounts. This page provides documentation and local workflow links.') if project.get('online') else t['project_note']
    quick = f'<p class="workflow-label">{t["quick_start"]}</p><p><code>{E(project["command"])}</code></p>' if project.get('command') else ''
    status = f'<p class="project-status">{E(project["status"][lang])}</p>' if project.get('status') else ''
    availability = f'<h2>{t["availability"]}</h2><p>{E(project["availability"][lang])}</p>' if project.get('availability') else ''
    stage = f'<h2>{t["stage"]}</h2><p>{E(project["status"][lang])}</p>' if project.get('status') else ''
    return f'''<div class="container"><section class="project-hero"><div class="breadcrumb"><a href="{home}">{t['home']}</a> / <a href="{home}#software">{t['back']}</a> / {E(software_name(project,lang))}</div><div class="eyebrow">{E(project['category'][lang])}</div><h1>{E(software_name(project,lang))}</h1>{status}<p class="project-lead">{E(project['summary'][lang])}</p>{localized_tags(project,lang)}<div class="project-buttons">{buttons}</div>{online_note}</section>
      {project_media(project,lang,prefix)}<div class="project-layout"><article class="prose project-prose">{markdown(ROOT/'content/software'/f'{project["slug"]}.{lang}.md')}</article><aside class="project-aside"><h2>{t['project_info']}</h2><p>{project_note}</p>{stage}{availability}{quick}{related_block}</aside></div></div>'''

def validate(profile, papers, software):
    if len({p['id'] for p in papers}) != len(papers):
        raise ValueError('Duplicate publication id')
    if len({s['slug'] for s in software}) != len(software):
        raise ValueError('Duplicate software slug')
    priorities = [p['display_priority'] for p in papers if 'display_priority' in p]
    if len(set(priorities)) != len(priorities):
        raise ValueError('Duplicate publication display priority')
    for p in papers:
        for field in ['title','authors','venue','details','year','citations','type']:
            if field not in p:
                raise ValueError(f'Missing {field}: {p["id"]}')
        if p['type'] not in ('journal','preprint','resource') or (p['citations'] is not None and (type(p['citations']) is not int or p['citations'] < 0)):
            raise ValueError('Invalid publication record: ' + p['id'])
        roles = p.get('author_roles', [])
        if not isinstance(roles, list) or any(role not in ('first','co_first','corresponding','co_corresponding') for role in roles) or len(set(roles)) != len(roles):
            raise ValueError('Invalid author roles: ' + p['id'])
        if 'display_priority' in p and (type(p['display_priority']) is not int or p['display_priority'] < 1 or not roles or not p.get('author_role_source')):
            raise ValueError('Publication priority requires confirmed authorship: ' + p['id'])
    for s in software:
        if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',s['slug']):
            raise ValueError('Invalid software slug')
        if not (s.get('repository') or s.get('contact')):
            raise ValueError('Software needs a repository or a contact route: ' + s['slug'])
        for media in s.get('media', []):
            sources = list(media['src'].values()) if isinstance(media['src'],dict) else [media['src']]
            if media.get('mobile_src'):
                sources += list(media['mobile_src'].values()) if isinstance(media['mobile_src'],dict) else [media['mobile_src']]
            for source in sources:
                if not (ROOT/source).is_file():
                    raise ValueError('Missing software media: ' + source)
        for lang in TEXT:
            if not (ROOT/'content/software'/f'{s["slug"]}.{lang}.md').exists():
                raise ValueError('Missing software Markdown')
        for p in s['related_publications']:
            if p not in {x['id'] for x in papers}:
                raise ValueError('Unknown related publication: ' + p)
    if not (ROOT/'images/profile.jpg').exists():
        raise ValueError('Missing portrait')

def unlisted_redirect(target, lang):
    label = '查看软件列表' if lang == 'zh' else 'View software projects'
    return f'''<!doctype html>
<html lang="{'zh-CN' if lang == 'zh' else 'en'}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>{label} · Yuming Su</title>
<meta http-equiv="refresh" content="0;url={E(target)}">
<script>location.replace({json.dumps(target)});</script></head>
<body><p><a href="{E(target)}">{label}</a></p></body></html>
'''


def build(check=False):
    profile, papers, software = load('profile'), load('publications'), load('software')
    visible_software = [project for project in software if project.get('visible', True)]
    analytics = load('analytics')
    endpoint = analytics['endpoint'].rstrip('/')
    if analytics['provider'] != 'goatcounter':
        raise ValueError('Unsupported analytics provider')
    if analytics['enabled']:
        if not re.fullmatch(r'https://[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.goatcounter\.com', endpoint):
            raise ValueError('Use the public GoatCounter site URL, never an API token')
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', analytics['started_on']):
            raise ValueError('Record the real analytics activation date')
    validate(profile,papers,software)
    template = Template((ROOT/'templates/base.html').read_text(encoding='utf-8'))
    asset_text = ''.join((ROOT/'assets'/name).read_text(encoding='utf-8') for name in ['site.css','site.js','analytics.js'])
    asset_version = hashlib.sha256(asset_text.encode('utf-8')).hexdigest()[:12]
    outputs = {}
    for lang,t in TEXT.items():
        locale_path = Path(language_root(lang))
        for project in [None] + software:
            path = locale_path / ('software/'+project['slug'] if project else '') / 'index.html'
            depth = len(path.parts)-1
            prefix = '../'*depth if depth else './'
            home = prefix + language_root(lang)
            if project and not project.get('visible', True):
                outputs[path] = unlisted_redirect(home + '#software', lang)
                continue
            other = 'zh' if lang=='en' else 'en'
            language_url = prefix + language_root(other) + ('software/'+project['slug']+'/' if project else '')
            nav = ''.join(f'<a href="{home}#{section}">{t[section]}</a>' for section in ['about','research','software','publications','contact'])
            body = project_body(project,papers,lang,home,prefix,profile['email']) if project else home_body(profile,papers,visible_software,lang,prefix)
            if project:
                if analytics['enabled']:
                    label = '累计访问' if lang == 'zh' else 'Recorded visits'
                    status = f'<strong data-visit-count="/software/{E(project["slug"])}/">…</strong>'
                    note = ('自 '+analytics['started_on']+' 起，中英文合并；按会话计次，并非历史独立人数。' if lang=='zh' else 'Since '+analytics['started_on']+'; English and Chinese combined. Session-based visits, not lifetime unique people.')
                else:
                    label = '访问统计' if lang == 'zh' else 'Visit statistics'
                    status = '尚未启用' if lang == 'zh' else 'Not enabled'
                    note = '启用后开始累计，无法补回此前访问。' if lang=='zh' else 'Counts begin on activation; earlier visits cannot be recovered.'
                stats = f'<section class="visit-statistics"><h2>{label}</h2><p>{status}</p><p class="stats-note">{E(note)}</p></section>'
                body = body.replace('</aside>',stats+'</aside>')
            elif analytics['enabled']:
                label = '累计访问' if lang=='zh' else 'Recorded visits'
                for item in visible_software:
                    anchor = f'<div class="software-category">{E(item["category"][lang])}</div>'
                    counter = f'<div class="software-visits">{label} <span data-visit-count="/software/{E(item["slug"])}/">…</span></div>'
                    body = body.replace(anchor,anchor+counter)
            outputs[path] = template.substitute(
                analytics_endpoint=E(endpoint if analytics['enabled'] else ''),analytics_hosts=E(','.join(analytics['allowed_hosts'])),
                analytics_path='/software/'+E(project['slug'])+'/' if project else '/',analytics_title=E(project['name'] if project else 'Yuming Su'),
                html_lang='zh-CN' if lang=='zh' else 'en',title=E(software_name(project,lang)+' · Yuming Su' if project else t['title']),
                description=E(project['summary'][lang] if project else t['description']),prefix=prefix,asset_version=asset_version,skip=t['skip'],navigation=t['navigation'],home=home,nav=nav,
                language_url=language_url,other_lang='en' if other=='en' else 'zh-CN',language_label='English' if lang=='zh' else '中文',body=body,
                year=profile['updated'][:4],updated_label=t['updated'],updated=profile['updated'],source_label=t['source'])
    # Preserve previously shared /en/ URLs as redirects to the English primary routes.
    for project in [None] + software:
        path = Path('en') / ('software/'+project['slug'] if project else '') / 'index.html'
        prefix = '../' * (len(path.parts)-1)
        if project and not project.get('visible', True):
            outputs[path] = unlisted_redirect(prefix + '#software', 'en')
            continue
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
    print(f'{"Checked" if check else "Built"} {len(outputs)-1} HTML pages; {len(papers)} scholarly records; {len(visible_software)} visible software projects.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    build(parser.parse_args().check)
