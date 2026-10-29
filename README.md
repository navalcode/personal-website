# Personal website

[Español](README.es.md) · [Website](https://navalcode.github.io/personal-website/) · [GitHub](https://github.com/navalcode)

Source for Manuel Naval's personal website. GitHub is the main place to read the work; the site provides a visual introduction to eight original apps/labs and links to their code and CI history. English is primary, with a substantive Spanish version.

## Develop

Python 3 generates complete static pages from `content.json`. No package installation or backend is required. Outfit/Fraunces, screenshots, GSAP 3.15.0 and ScrollTrigger are local assets; there are no font-CDN requests or analytics.

```sh
python3 build.py
python3 check.py
python3 -m http.server 8048 --directory docs --bind 127.0.0.1
```

Edit content, renderer, CSS or the optional `docs/motion.js`, then regenerate and reload. `check.py` validates translation keys, eight project/evidence routes, local files, calculated contrast and pinned asset hashes. Those source checks do not replace browser review.

## Design and behavior

[DESIGN.md](DESIGN.md) explains the shared visual system and six compositions: editorial split, wide Rumbo media, open Bitácora narrative, expandable lab index, four-phase working sequence and editorial close. Captures come from the actual API 37 Android demos in English, with fictional data. Rumbo's landscapes are original Canvas artwork; no generated design concept is presented as a running app.

HTML owns navigation, links, landmarks and native `details/summary` disclosures. GSAP only scales/fades media and pins the lab context on sufficiently wide/tall desktop windows. `prefers-reduced-motion` disables those effects and CSS movement. Content and disclosures remain usable without JavaScript. Fonts and vendor notices are preserved separately from the original MIT source.

Local app checks cited by the redesign: Rumbo: 32 JVM/8 emulator checks and Bitácora: 23 controller/widget checks plus native persistence. Each repository documents validation limits. A CI-history link does not assert that the latest source has passed remotely. Native iOS remains a gradual roadmap, not an implemented capability.

## Hosting

GitHub Pages serves `main` → `/docs` at the project URL above. `site.json` defines canonical URLs. Earlier `/portfolio/` URLs redirect through compatibility pages in `navalcode.github.io`; association, authentication and privacy resources are maintained separately. Do not restore the abandoned custom domain or publish the coordination workspace.

Original source, copy, design and demo captures: [MIT](LICENSE), Manuel Naval, 2026. Fonts, GSAP and linked projects retain their own licenses and attribution. See [credits and notices](THIRD_PARTY.md) and [pinned sources/hashes](third_party.json).
