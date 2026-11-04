"""Check static content, bilingual parity, links, local resources and asset integrity."""
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
import build

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'docs'
SCRIPTS = set()


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.resources, self.scripts, self.layouts = set(), [], [], [], set()
        self.h1 = self.articles = self.disclosures = 0
        self.language = None

    def handle_starttag(self, tag, values):
        attrs = dict(values)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, 'duplicate ID: ' + attrs['id']
            self.ids.add(attrs['id'])
        if tag == 'html': self.language = attrs['lang']
        if tag == 'h1': self.h1 += 1
        if tag == 'article': self.articles += 1
        if tag == 'details': self.disclosures += 1
        if 'data-layout' in attrs: self.layouts.add(attrs['data-layout'])
        if tag == 'script':
            assert 'defer' in attrs and attrs.get('src') in SCRIPTS, 'unreviewed or blocking script'
            self.scripts.append(attrs['src'])
            self.resources.append(attrs['src'])
        if tag == 'a': self.links.append(attrs['href'])
        if tag == 'img':
            assert attrs.get('alt') and attrs.get('width') and attrs.get('height'), 'image description/dimensions missing'
            self.resources.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') in {'stylesheet', 'icon', 'preload'}:
            self.resources.append(attrs['href'])


def luminance(color):
    channels = [int(color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in channels]
    return sum(v * w for v, w in zip(linear, [.2126, .7152, .0722]))


def check():
    assert set(build.COPY['en']) == set(build.COPY['es']), 'copy keys differ between languages'
    assert len(build.PROJECTS) == 9 and len({p['id'] for p in build.PROJECTS}) == 9
    for p in build.PROJECTS:
        assert set(p['en']) == set(p['es']) == {'question', 'body', 'evidence'}
        assert all(p[lang][key].strip() for lang in ['en', 'es'] for key in p[lang])
    for language in ['en', 'es']:
        contexts = build.COPY[language]['experience_contexts']
        assert [item['name'] for item in contexts] == ['Renfe', 'AWAI']
        assert all(set(item) == {'name', 'area', 'body'} and all(item.values()) for item in contexts)
    for language in ['en', 'es']:
        assert len(build.COPY[language]['technical_rows']) == 3
        for row in build.COPY[language]['technical_rows']:
            assert set(row) == {'title', 'body', 'stack', 'target', 'link'}
            assert row['target'] in {project['id'] for project in build.PROJECTS}
            assert all(row.values())
    assert 'earlier_projects' not in build.CONTENT
    for language in ['en', 'es']:
        assert len(build.COPY[language]['professional_contributions']) == 3
        for item in build.COPY[language]['professional_contributions']:
            assert set(item) == {'title', 'body'} and all(item.values())
    assert len(build.COPY['en']['steps']) == len(build.COPY['es']['steps']) == 4
    assert set(build.COPY['en']['image_alts']) == set(build.COPY['es']['image_alts'])
    results = []
    for language, filename in [('en', 'index.html'), ('es', 'es.html')]:
        text = (DOCS / filename).read_text()
        assert text == build.render(language), 'generated page is stale'
        assert not any(term in text.lower() for term in ['lorem ipsum', '[insert', 'section 01', 'question 05'])
        page = Page(); page.feed(text)
        assert page.language == language and page.h1 == 1 and page.articles == 9
        assert page.disclosures == 6 and len(page.layouts) >= 4 and set(page.scripts) == SCRIPTS
        for resource in page.resources:
            parsed = urlsplit(resource)
            assert not parsed.scheme and not parsed.netloc, 'external runtime resource: ' + resource
        for href in page.links + page.resources:
            parsed = urlsplit(href)
            assert not parsed.scheme or parsed.scheme == 'https', 'unexpected link scheme'
            if not parsed.scheme and parsed.path:
                target = (DOCS / parsed.path).resolve()
                assert DOCS.resolve() in target.parents and target.is_file(), 'missing/escaping resource: ' + href
            if not parsed.path and parsed.fragment: assert parsed.fragment in page.ids
        for p in build.PROJECTS:
            repo = 'https://github.com/navalcode/' + p['id']
            assert repo in page.links and repo + '/actions' in page.links
        assert 'earlier-work' not in text
        assert not any('https://github.com/navalcode/' + name in page.links for name in ['DojoNavalManuel', 'Trianafy', 'tabla_angular', 'FlutterVariants'])
        assert '#experience' in page.links and 'experience' in page.ids
        assert 'Babel' in text and 'Renfe' in text and 'AWAI' in text
        opening = text.split('<section class="experience chapter"')[0]
        assert not any(name in opening for name in ['Babel', 'Renfe', 'AWAI'])
        assert 'engineer' not in text.lower() and 'ingenier' not in text.lower()
        assert '<h1 id="home-title">Manuel Naval.</h1>' in text
        assert 'automotive' not in text.lower(), 'restricted sector label in public page'
        assert '#main' in page.links and build.COPY[language]['other_file'] in page.links
        results.append({'language': language, 'projects': page.articles, 'disclosures': page.disclosures, 'layout_labels': sorted(page.layouts), 'links': len(page.links), 'unique_html_resources': len(set(page.resources))})
    css = (DOCS / 'styles.css').read_text()
    for resource in re.findall(r"url\(['\"]?([^)'\"]+)", css):
        assert not urlsplit(resource).scheme and (DOCS / resource).is_file(), 'invalid CSS resource'
    pairs = [('body', '#17252f', '#f5f6f7', 4.5), ('muted', '#52616b', '#f5f6f7', 4.5), ('accent', '#2348b3', '#f5f6f7', 4.5), ('button', '#ffffff', '#2348b3', 4.5), ('selection', '#17252f', '#e5eafa', 4.5), ('control_outline', '#7b8790', '#f5f6f7', 3), ('gallery_caption', '#52616b', '#e4e9ee', 4.5)]
    contrast = {}
    for name, fg, bg, minimum in pairs:
        assert fg in css.lower() and bg in css.lower(), 'contrast tokens absent from CSS'
        values = sorted([luminance(fg), luminance(bg)])
        ratio = (values[1] + .05) / (values[0] + .05)
        assert ratio >= minimum, (name, ratio)
        contrast[name] = round(ratio, 2)
    vendor = json.loads((ROOT / 'third_party.json').read_text())
    for artifact in vendor['files']:
        assert hashlib.sha256((ROOT / artifact['path']).read_bytes()).hexdigest() == artifact['sha256'], 'changed vendor/font asset'
    return {'pages': results, 'calculated_contrast': contrast, 'scripts': sorted(SCRIPTS), 'external_runtime_resources': 0, 'pinned_asset_hashes': len(vendor['files']), 'scope': 'Static/source checks. Runtime, keyboard, motion and visual geometry require browser review.'}


if __name__ == '__main__': print(json.dumps(check(), indent=2))
