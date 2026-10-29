# Personal website

[Español](README.es.md) · [Website](https://navalcode.github.io/personal-website/) · [GitHub](https://github.com/navalcode)

Source for my personal website. GitHub is the main place to read my work; the site offers a visual introduction and links to the same repositories.

## Develop

The site is static HTML and CSS. Python generates the English and Spanish pages from the content in `build.py`. There are no runtime packages, external fonts or analytics.

```sh
python3 build.py
python3 check.py
python3 -m http.server 8048 --directory docs --bind 127.0.0.1
```

GitHub Pages publishes `main` → `/docs`. `site.json` defines canonical URLs. The previous `/portfolio/` URLs redirect through compatibility pages in `navalcode.github.io`; application association, authentication and privacy resources are maintained separately.

## Content

Project descriptions link to source and executed checks. The Bitácora image is an emulator screenshot; the Rumbo graphic is an implementation diagram. Each project documents its own validation scope.

Original source, writing, design and image: [MIT](LICENSE), Manuel Naval, 2026. Linked projects retain their own licenses and attribution.
