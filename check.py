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
SCRIPTS = {'assets/vendor/gsap.min.js', 'assets/vendor/ScrollTrigger.min.js', 'motion.js'}


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
    assert len(build.PROJECTS) == 8 and len({p['id'] for p in build.PROJECTS}) == 8
    for p in build.PROJECTS:
        assert set(p['en']) == set(p['es']) == {'question', 'body', 'evidence'}
        assert all(p[lang][key].strip() for lang in ['en', 'es'] for key in p[lang])
    assert len(build.COPY['en']['steps']) == len(build.COPY['es']['steps']) == 4
    assert set(build.COPY['en']['image_alts']) == set(build.COPY['es']['image_alts'])
    results = []
    for language, filename in [('en', 'index.html'), ('es', 'es.html')]:
        text = (DOCS / filename).read_text()
        assert text == build.render(language), 'generated page is stale'
        assert not any(term in text.lower() for term in ['lorem ipsum', '[insert', 'section 01', 'question 05'])
        page = Page(); page.feed(text)
        assert page.language == language and page.h1 == 1 and page.articles == 8
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
        assert '#main' in page.links and build.COPY[language]['other_file'] in page.links
        results.append({'language': language, 'projects': page.articles, 'disclosures': page.disclosures, 'layout_labels': sorted(page.layouts), 'links': len(page.links), 'unique_html_resources': len(set(page.resources))})
    css = (DOCS / 'styles.css').read_text()
    for resource in re.findall(r"url\(['\"]?([^)'\"]+)", css):
        assert not urlsplit(resource).scheme and (DOCS / resource).is_file(), 'invalid CSS resource'
    pairs = [('body', '#202421', '#faf8f3', 4.5), ('muted', '#5e625c', '#faf8f3', 4.5), ('accent', '#9b432f', '#faf8f3', 4.5), ('button', '#ffffff', '#9b432f', 4.5), ('selection', '#9b432f', '#f2e3db', 4.5), ('control_outline', '#85877e', '#faf8f3', 3)]
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
