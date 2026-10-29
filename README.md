# Manuel Naval portfolio

[Español](README.es.md)

English-first static portfolio with a full Spanish page, original CSS and links to executable public evidence. No JavaScript, tracking, accounts, backend, external fonts or runtime packages.

```sh
python3 build.py
python3 -m http.server 8048 --directory docs --bind 127.0.0.1
```

`build.py` generates both pages from reviewed bilingual content. GitHub Pages serves only `docs/`; project source and this README are not runtime assets. The source branch and `/docs` path are configured in the dedicated repository’s Pages settings. Deployment is independent of existing application/authentication resources.

Project descriptions deliberately distinguish original demos, historical labs, simulated data and physical validation. CI links identify actual executed runs. The Bitácora image is an actual emulator capture from the original public demo; the Rumbo graphic is an implementation diagram.

Original code, copy, design and image: [MIT](LICENSE), Manuel Naval, 2026. Linked historical repositories retain their own licenses and attribution.
