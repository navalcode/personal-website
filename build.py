"""Generate complete EN/ES HTML; all content remains usable without JavaScript."""
from html import escape
import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORIGIN = json.loads((ROOT / 'site.json').read_text())['origin'].rstrip('/') + '/'
CONTENT = json.loads((ROOT / 'content.json').read_text())
PROJECTS = CONTENT['projects']
COPY = CONTENT['copy']


def render(language):
    c = COPY[language]
    es = language == 'es'
    other = 'en' if es else 'es'
    filename = 'es.html' if es else 'index.html'
    profile = 'https://github.com/navalcode' + ('/navalcode/blob/main/README.es.md' if es else '')
    roadmap = 'https://github.com/navalcode/navalcode/blob/main/MOBILE_ROADMAP' + ('.es' if es else '') + '.md'
    title = 'Manuel Naval · ' + c['footer']
    e = escape

    def arrow():
        return '<span aria-hidden="true">↗</span>'

    def image(name, caption=None, eager=False):
        loading = 'eager' if eager else 'lazy'
        width, height = struct.unpack('>II', (ROOT / 'docs/assets' / name).read_bytes()[16:24])
        picture = f'<img src="assets/{name}" width="{width}" height="{height}" alt="{e(c["image_alts"][name])}" loading="{loading}" decoding="async">'
        link = f'<a class="screen-link" href="assets/{name}">{picture}</a>'
        if caption:
            return f'<figure class="screen-figure">{link}<figcaption>{e(caption)}</figcaption></figure>'
        return link

    def project_links(project, long=False):
        repo = 'https://github.com/navalcode/' + project['id']
        label = c['source'] if long else c['source_short']
        return f'<div class="project-links"><a href="{repo}">{e(label)} {arrow()}<span class="sr-only"> · {e(project["title"])}</span></a><a href="{repo}/actions">{e(c["ci"])}<span class="sr-only"> · {e(project["title"])}</span></a></div>'

    def lab(project):
        p = project[language]
        opened = ' open' if project['id'] == 'compose-effect-lab' else ''
        return f'''<article class="lab" id="{project['id']}" aria-labelledby="title-{project['id']}">
<details{opened}><summary><span class="summary-copy"><strong id="title-{project['id']}">{e(project['title'])}</strong><span>{e(p['question'])}</span></span><span class="summary-icon" aria-hidden="true"></span></summary>
<div class="lab-body"><p class="stack">{e(project['stack'])}</p><p>{e(p['body'])}</p><p class="evidence">{e(p['evidence'])}</p>{project_links(project)}</div></details></article>'''

    by_id = {project['id']: project for project in PROJECTS}
    rumbo, bitacora, ios = (by_id[key] for key in ('rumbo-android', 'bitacora-flutter', 'bitacora-ios'))
    labs = [project for project in PROJECTS if project['id'] not in {'rumbo-android', 'bitacora-flutter', 'bitacora-ios'}]
    steps = ''.join(f'<li><h3>{e(heading)}</h3><p>{e(body)}</p></li>' for heading, body in c['steps'])
    contexts = ''.join(f'<div class="experience-context"><h3>{e(item["name"])}</h3><p class="context-area">{e(item["area"])}</p><p>{e(item["body"])}</p></div>' for item in c['experience_contexts'])
    technical_rows = ''.join(f'<div class="technical-row"><dt>{e(row["title"])}</dt><dd><p>{e(row["body"])}</p><p class="stack">{e(row["stack"])}</p><a href="#{row["target"]}">{e(row["link"])} {arrow()}</a></dd></div>' for row in c['technical_rows'])
    project_index = ''.join(f'<a href="#{project["id"]}"><span>{e(project["title"])}</span>{arrow()}</a>' for project in PROJECTS)
    return f'''<!doctype html>
<html lang="{language}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(c['description'])}">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; script-src 'self'; font-src 'self'; img-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(c['description'])}"><meta property="og:type" content="website">
<link rel="canonical" href="{ORIGIN + ('es.html' if es else '')}"><link rel="alternate" hreflang="en" href="{ORIGIN}"><link rel="alternate" hreflang="es" href="{ORIGIN}es.html">
<link rel="preload" href="assets/fonts/IBMPlexSans.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="styles.css"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml">

</head>
<body>
<a class="skip" href="#main">{e(c['skip'])}</a>
<header class="site-header"><div class="wrap"><nav aria-label="{e(c['nav_label'])}"><a class="wordmark" href="{filename}">Manuel Naval</a><div class="nav-links"><a href="#experience">{e(c['experience'])}</a><a href="#projects">{e(c['work'])}</a><a href="#approach">{e(c['method'])}</a><a href="{profile}">GitHub {arrow()}</a><a class="language" href="{c['other_file']}" lang="{other}" hreflang="{other}">{e(c['other'])}</a></div></nav></div></header>
<main id="main" tabindex="-1"><div class="hero-surface">
<section class="hero wrap" aria-labelledby="home-title" data-layout="editorial-split">
<div class="hero-copy"><h1 id="home-title">{e(c['title_start'])}</h1><p class="hero-specialty">{e(c['title_middle'])}<span>{e(c['title_accent'])}</span></p><p class="intro">{e(c['intro'])}</p><div class="hero-actions"><a class="button" href="#projects">{e(c['cta'])}<span aria-hidden="true">→</span></a><a class="text-link" href="#experience">{e(c['experience'])} <span aria-hidden="true">↓</span></a></div></div>
<div class="hero-media"><figure><a class="hero-screen" href="#rumbo-android"><img src="assets/rumbo-explore.png" width="1080" height="2400" alt="{e(c['image_alts']['rumbo-explore.png'])}" decoding="async" fetchpriority="high"></a><figcaption><span>Rumbo / Android</span><span>Kotlin · Compose</span></figcaption></figure></div>
</section>
</div>
<div class="wrap page-body">
<section class="technical chapter" aria-labelledby="technical-title" data-layout="technical-capabilities"><div class="technical-heading"><h2 id="technical-title">{e(c['technical_title'])}</h2><p>{e(c['technical_intro'])}</p></div><dl class="technical-list">{technical_rows}</dl></section>
<section class="experience chapter" id="experience" aria-labelledby="experience-title" data-layout="professional-context">
<div class="experience-heading"><h2 id="experience-title">{e(c['experience_title'])}</h2><p>{e(c['experience_intro'])}</p></div>
<div class="experience-content"><div class="babel-context"><h3>{e(c['experience_role'])}</h3><p>{e(c['experience_body'])}</p></div><div class="experience-contexts">{contexts}</div><p class="experience-note">{e(c['experience_note'])}</p></div>
</section>
<section class="work-index chapter" aria-labelledby="work-title" data-layout="project-directory"><div><h2 id="work-title">{e(c['selected_title'])}</h2><p>{e(c['selected_intro'])}</p></div><nav class="project-directory" aria-label="{e(c['project_index'])}">{project_index}</nav></section>
<section class="selected-work chapter" id="projects" aria-label="{e(c['work'])}">
<article id="rumbo-android" class="rumbo-case" aria-labelledby="rumbo-title" data-layout="wide-media">
<h2 id="rumbo-title">Rumbo<span class="project-platform">{e(c['rumbo_identity'].split(" / ")[1])}</span></h2><p class="project-question">{e(rumbo[language]['question'])}</p>
<figure class="case-gallery"><div class="media-pair motion-media">{image('rumbo-explore.png')}{image('rumbo-offline.png')}</div><figcaption>{e(c['capture_credit'])} {e(c['rumbo_credit'])}</figcaption></figure>
<div class="case-caption"><p>{e(rumbo[language]['body'])}</p><div>{project_links(rumbo, True)}<p class="evidence">{e(rumbo[language]['evidence'])}</p><p class="stack">{e(rumbo['stack'])}</p></div></div>
</article>
<article id="bitacora-flutter" class="bitacora-case chapter" aria-labelledby="bitacora-title" data-layout="open-three-column">
<div class="bitacora-copy"><h2 id="bitacora-title">Bitácora<span class="project-platform">Flutter</span></h2><p class="project-question">{e(bitacora[language]['question'])}</p><div class="state-story"><h3>{e(c['bitacora_subtitle'])}</h3><p>{e(bitacora[language]['body'])}</p></div><p class="evidence">{e(bitacora[language]['evidence'])}</p>{project_links(bitacora, True)}</div>
<div class="board-image motion-media">{image('bitacora-board.png',c['board_caption'])}</div><div class="detail-image motion-media">{image('bitacora-detail.png',c['detail_caption'])}</div><p class="capture-credit">{e(c['capture_credit'])}</p>
</article>
<article id="bitacora-ios" class="bitacora-case chapter" aria-labelledby="ios-title" data-layout="open-three-column">
<div class="bitacora-copy"><h2 id="ios-title">Bitácora<span class="project-platform">SwiftUI · {"Demo iOS nativa" if es else "Native iOS demo"}</span></h2><p class="project-question">{e(ios[language]['question'])}</p><div class="state-story"><h3>{e(c['ios_subtitle'])}</h3><p>{e(ios[language]['body'])}</p></div><p class="evidence">{e(ios[language]['evidence'])}</p><p class="reading-note">{e(c['ios_scope'])}</p>{project_links(ios, True)}</div>
<div class="board-image motion-media">{image('bitacora-ios-board.png',c['board_caption'])}</div><div class="detail-image motion-media">{image('bitacora-ios-detail.png',c['ios_detail_caption'])}</div><p class="capture-credit">{e(c['ios_credit'])}</p>
</article></section>
<section class="lab-index chapter" id="labs" aria-labelledby="labs-title" data-layout="expandable-index">
<div class="lab-intro"><h2 id="labs-title">{e(c['lab_title'])}</h2><p>{e(c['lab_intro'])}</p><p class="reading-note">{e(c['lab_hint'])}</p></div><div class="lab-list">{''.join(lab(project) for project in labs)}</div>
</section>
<section class="approach chapter" id="approach" aria-labelledby="approach-title" data-layout="open-sequence">
<div class="approach-head"><h2 id="approach-title">{e(c['method_title'])}</h2><p>{e(c['method_intro'])}</p></div><ol class="method-sequence">{steps}</ol><a class="method-link" href="https://github.com/navalcode/spec-evidence-lab">{e(c['method_link'])} {arrow()}</a>
</section>
<section class="closing chapter" aria-labelledby="closing-title" data-layout="editorial-close"><div><h2 id="closing-title">{e(c['closing_title'])}</h2><p>{e(c['closing_body'])}</p><p class="history-note">{e(c['history'])}</p></div><div class="closing-links"><a href="{profile}">{e(c['profile'])} {arrow()}</a><p>{e(c['profile_detail'])}</p><a href="{roadmap}">{e(c['roadmap'])} {arrow()}</a><p>{e(c['roadmap_detail'])}</p></div></section>
</div></main>
<footer class="site-footer wrap"><p>© 2026 Manuel Naval</p><p>{e(c['footer'])}</p><nav aria-label="{'Enlaces finales' if es else 'Footer links'}"><a href="https://github.com/navalcode/personal-website/blob/main/THIRD_PARTY.md">{e(c['credits'])}</a><a href="{c['other_file']}" lang="{other}">{e(c['other'])}</a></nav></footer>
</body></html>
'''


if __name__ == '__main__':
    for lang, filename in [('en','index.html'),('es','es.html')]:
        (ROOT/'docs'/filename).write_text(render(lang))
    print('Generated complete English and Spanish pages.')
