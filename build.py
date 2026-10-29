"""Generate complete EN/ES HTML; all content remains usable without JavaScript."""
from html import escape
import json
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
        picture = f'<img src="assets/{name}" width="1080" height="2400" alt="{e(c["image_alts"][name])}" loading="{loading}" decoding="async">'
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

    rumbo, bitacora = PROJECTS[:2]
    steps = ''.join(f'<li><h3>{e(heading)}</h3><p>{e(body)}</p></li>' for heading, body in c['steps'])
    return f'''<!doctype html>
<html lang="{language}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(c['description'])}">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; script-src 'self'; font-src 'self'; img-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(c['description'])}"><meta property="og:type" content="website">
<link rel="canonical" href="{ORIGIN + ('es.html' if es else '')}"><link rel="alternate" hreflang="en" href="{ORIGIN}"><link rel="alternate" hreflang="es" href="{ORIGIN}es.html">
<link rel="preload" href="assets/fonts/Outfit.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<script src="assets/vendor/gsap.min.js" defer></script><script src="assets/vendor/ScrollTrigger.min.js" defer></script><script src="motion.js" defer></script>
</head>
<body>
<a class="skip" href="#main">{e(c['skip'])}</a>
<header class="site-header wrap"><nav aria-label="{e(c['nav_label'])}"><a class="wordmark" href="{filename}">Manuel Naval</a><div class="nav-links"><a href="#projects">{e(c['work'])}</a><a href="#approach">{e(c['method'])}</a><a href="{profile}">GitHub {arrow()}</a><a class="language" href="{c['other_file']}" lang="{other}" hreflang="{other}">{e(c['other'])}</a></div></nav></header>
<main class="wrap" id="main" tabindex="-1">
<section class="hero" aria-labelledby="home-title" data-layout="editorial-split">
<div class="hero-copy"><h1 id="home-title">{e(c['title_start'])}<br>{e(c['title_middle'])}<em>{e(c['title_accent'])}</em></h1><p class="intro">{e(c['intro'])}</p><div class="hero-actions"><a class="button" href="#projects">{e(c['cta'])}<span aria-hidden="true">→</span></a><a class="text-link" href="{profile}">GitHub {arrow()}</a></div></div>
<div class="hero-media"><figure><a class="hero-screen" href="#rumbo-android"><img src="assets/rumbo-explore.png" width="1080" height="2400" alt="{e(c['image_alts']['rumbo-explore.png'])}" decoding="async" fetchpriority="high"></a><figcaption>Rumbo / Android</figcaption></figure><figure><a class="hero-screen" href="#bitacora-flutter"><img src="assets/bitacora-board.png" width="1080" height="2400" alt="{e(c['image_alts']['bitacora-board.png'])}" decoding="async"></a><figcaption>Bitácora / Flutter</figcaption></figure></div>
</section>
<section class="selected-work chapter" id="projects" aria-label="{e(c['work'])}">
<article id="rumbo-android" class="rumbo-case" aria-labelledby="rumbo-title" data-layout="wide-media">
<p class="project-identity">{e(c['rumbo_identity'])}</p><h2 id="rumbo-title">{e(rumbo[language]['question'])}</h2>
<figure class="case-gallery"><div class="media-pair motion-media">{image('rumbo-explore.png')}{image('rumbo-offline.png')}</div><figcaption>{e(c['capture_credit'])} {e(c['rumbo_credit'])}</figcaption></figure>
<div class="case-caption"><p>{e(rumbo[language]['body'])}</p><div>{project_links(rumbo, True)}<p class="evidence">{e(rumbo[language]['evidence'])}</p><p class="stack">{e(rumbo['stack'])}</p></div></div>
</article>
<article id="bitacora-flutter" class="bitacora-case chapter" aria-labelledby="bitacora-title" data-layout="open-three-column">
<div class="bitacora-copy"><p class="project-identity">{e(c['bitacora_identity'])}</p><h2 id="bitacora-title">{e(bitacora[language]['question'])}</h2><div class="state-story"><h3>{e(c['bitacora_subtitle'])}</h3><p>{e(bitacora[language]['body'])}</p></div><p class="evidence">{e(bitacora[language]['evidence'])}</p>{project_links(bitacora, True)}</div>
<div class="board-image motion-media">{image('bitacora-board.png',c['board_caption'])}</div><div class="detail-image motion-media">{image('bitacora-detail.png',c['detail_caption'])}</div><p class="capture-credit">{e(c['capture_credit'])}</p>
</article></section>
<section class="lab-index chapter" id="labs" aria-labelledby="labs-title" data-layout="expandable-index">
<div class="lab-intro"><h2 id="labs-title">{e(c['lab_title'])}</h2><p>{e(c['lab_intro'])}</p><p class="reading-note">{e(c['lab_hint'])}</p></div><div class="lab-list">{''.join(lab(project) for project in PROJECTS[2:])}</div>
</section>
<section class="approach chapter" id="approach" aria-labelledby="approach-title" data-layout="open-sequence">
<div class="approach-head"><h2 id="approach-title">{e(c['method_title'])}</h2><p>{e(c['method_intro'])}</p></div><ol class="method-sequence">{steps}</ol><a class="method-link" href="https://github.com/navalcode/spec-evidence-lab">{e(c['method_link'])} {arrow()}</a>
</section>
<section class="closing chapter" aria-labelledby="closing-title" data-layout="editorial-close"><div><h2 id="closing-title">{e(c['closing_title'])}</h2><p>{e(c['closing_body'])}</p><p class="history-note">{e(c['history'])}</p></div><div class="closing-links"><a href="{profile}">{e(c['profile'])} {arrow()}</a><p>{e(c['profile_detail'])}</p><a href="{roadmap}">{e(c['roadmap'])} {arrow()}</a><p>{e(c['roadmap_detail'])}</p></div></section>
</main>
<footer class="site-footer wrap"><p>© 2026 Manuel Naval</p><p>{e(c['footer'])}</p><nav aria-label="{'Enlaces finales' if es else 'Footer links'}"><a href="https://github.com/navalcode/personal-website/blob/main/THIRD_PARTY.md">{e(c['credits'])}</a><a href="{c['other_file']}" lang="{other}">{e(c['other'])}</a></nav></footer>
</body></html>
'''


if __name__ == '__main__':
    for lang, filename in [('en','index.html'),('es','es.html')]:
        (ROOT/'docs'/filename).write_text(render(lang))
    print('Generated complete English and Spanish pages.')
