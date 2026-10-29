"""Check generated pages, local resources and declared evidence links."""
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import urlsplit
import build

ROOT = Path(__file__).resolve().parent


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.resources = set(), [], []
        self.h1 = self.articles = self.scripts = 0
        self.language = None

    def handle_starttag(self, tag, values):
        attrs = dict(values)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, 'duplicate ID'
            self.ids.add(attrs['id'])
        if tag == 'html': self.language = attrs['lang']
        if tag == 'h1': self.h1 += 1
        if tag == 'article': self.articles += 1
        if tag == 'script': self.scripts += 1
        if tag == 'a': self.links.append(attrs['href'])
        if tag == 'img':
            assert attrs.get('alt'), 'missing image description'
            self.resources.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') in ['stylesheet', 'icon']:
            self.resources.append(attrs['href'])


def luminance(color):
    channels = [int(color[i:i+2],16)/255 for i in (1,3,5)]
    channels = [v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in channels]
    return sum(v*w for v,w in zip(channels,[.2126,.7152,.0722]))


def check():
    results = []
    for language, filename in [('en','index.html'),('es','es.html')]:
        text = (ROOT/'docs'/filename).read_text()
        assert text == build.render(language), 'generated page is stale'
        page = Page(); page.feed(text)
        assert page.language == language and page.h1 == 1 and page.articles == 8 and not page.scripts
        for resource in page.resources:
            assert not urlsplit(resource).scheme and not urlsplit(resource).netloc, 'external runtime resource'
        for href in page.links + page.resources:
            parsed = urlsplit(href)
            if not parsed.scheme and parsed.path:
                assert (ROOT/'docs'/parsed.path).is_file(), f'missing resource: {href}'
            if not parsed.path and parsed.fragment: assert parsed.fragment in page.ids
        for slug, _, _, run, *_ in build.PROJECTS:
            base='https://github.com/navalcode/'+slug
            assert base in page.links and base+'/actions/runs/'+run in page.links
        results.append({'language':language,'projects':page.articles,'links':len(page.links),'resources':len(page.resources)})
    pairs = [('body','#192a30','#f6f7f2'),('muted','#4d6066','#f6f7f2'),('accent','#006b59','#f6f7f2'),('tags','#284a41','#e7f0e8'),('capture','#203f56','#dfe9ef'),('button','#ffffff','#192a30')]
    contrast={}
    css=(ROOT/'docs/styles.css').read_text()
    for name,fg,bg in pairs:
        assert fg.lower() in css.lower() and bg.lower() in css.lower(), 'contrast pair absent from CSS'
        values=sorted([luminance(fg),luminance(bg)])
        ratio=(values[1]+.05)/(values[0]+.05); assert ratio>=4.5,(name,ratio)
        contrast[name]=round(ratio,2)
    return {'pages':results,'text_contrast_ratios':contrast,'scripts':0,'external_runtime_resources':0}


if __name__=='__main__': print(json.dumps(check(),indent=2))
