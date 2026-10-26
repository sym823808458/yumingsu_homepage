"""Illustrated bilingual guides from reviewed public content; no visit writes."""
import html,json
from pathlib import Path
E=lambda value:html.escape(str(value),quote=True)

def build_guides(root,template,profile,text,software,asset_version):
    guides=json.loads((root/'data/guides.json').read_text(encoding='utf-8'))
    expected={p['slug'] for p in software if p.get('online')}
    if set(guides)!=expected:raise ValueError('Every online tool needs a guide')
    outputs={}
    for project in software:
        slug=project['slug']
        if slug not in guides:continue
        guide=guides[slug]
        for lang,t in text.items():
            zh=lang=='zh';locale='zh/' if zh else '';other='' if zh else 'zh/'
            path=Path(locale+'software/'+slug+'/guide/index.html');prefix='../'*(len(path.parts)-1);home=prefix+locale
            title=guide['title'][lang];steps=[];toc=[]
            for i,step in enumerate(guide['steps'],1):
                heading=step['title'][lang];toc.append(f'<a href="#step-{i}">{i}. {E(heading)}</a>')
                paragraphs=''.join(f'<p>{E(p)}</p>' for p in step['text'][lang])
                figure=''
                if step.get('image'):
                    image=step['image']
                    if not image.startswith('images/guides/') or '..' in Path(image).parts or not (root/image).is_file():raise ValueError('Missing or unsafe guide image: '+image)
                    caption=step['caption'][lang]
                    figure=f'<figure><a href="{E(prefix+image)}" target="_blank" rel="noopener"><img src="{E(prefix+image)}" alt="{E(caption)}" loading="lazy"></a><figcaption>{E(caption)}</figcaption></figure>'
                steps.append(f'<section class="guide-step" id="step-{i}"><h2>{i}. {E(heading)}</h2>{paragraphs}{figure}</section>')
            back='软件介绍' if zh else 'Software overview';launch='免费使用 · 线上体验' if zh else 'Free online experience'
            note='截图来自公开教学数据或合成示例，不含用户账户、任务令牌或未公开研究数据。点击图片可放大。' if zh else 'Screenshots use public teaching data or synthetic examples, without user accounts, task tokens or private research data. Select an image to enlarge it.'
            body=f'<div class="container guide-page"><div class="breadcrumb"><a href="../">{back}</a> / {E(title)}</div><h1>{E(title)}</h1><p class="project-lead">{E(guide["intro"][lang])}</p><div class="project-buttons"><a class="button" href="{E(project["online"]["url"])}">{launch}</a><a class="button secondary" href="../">{back}</a></div><p class="guide-note">{note}</p><nav class="guide-toc" aria-label="Guide steps">{"".join(toc)}</nav>{"".join(steps)}<section class="guide-step"><h2>{"遇到问题" if zh else "Troubleshooting"}</h2>{"".join(f"<p>{E(p)}</p>" for p in guide["troubleshooting"][lang])}</section></div>'
            nav=''.join(f'<a href="{home}#{section}">{t[section]}</a>' for section in ['about','research','software','publications','contact'])
            outputs[path]=template.substitute(analytics_endpoint='',analytics_hosts='',analytics_provider='cloudflare-d1',analytics_software='',analytics_minutes=30,html_lang='zh-CN' if zh else 'en',title=E(title+' · Yuming Su'),description=E(guide['intro'][lang]),prefix=prefix,asset_version=asset_version,skip=t['skip'],navigation=t['navigation'],home=home,nav=nav,language_url=prefix+other+'software/'+slug+'/guide/',other_lang='en' if zh else 'zh-CN',language_label='English' if zh else '中文',body=body,year=profile['updated'][:4],updated_label=t['updated'],updated=profile['updated'],source_label=t['source'])
    return outputs
