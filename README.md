# Personal website

[Español](README.es.md) · [Website](https://navalcode.github.io/personal-website/) · [GitHub](https://github.com/navalcode)

Source for Manuel Naval's personal website. GitHub is the main place to read the work; the site provides a visual introduction to nine apps and technical labs and links to their code and CI history. English is primary, with a substantive Spanish version.

## Develop

Python 3 generates complete static pages from `content.json`. No package installation or backend is required. IBM Plex Sans and screenshots are local assets; earlier font and animation assets retain their notices but are not loaded; there are no font-CDN requests or analytics.

```sh
python3 build.py
python3 check.py
python3 -m http.server 8048 --directory docs --bind 127.0.0.1
```

Edit content, renderer, CSS, then regenerate and reload. `check.py` validates translation keys, nine project/evidence routes, local files, calculated contrast and pinned asset hashes. Those source checks do not replace browser review.

## Design and behavior

[DESIGN.md](DESIGN.md) explains the IBM Plex Sans typography, mineral/blue palette and compositions. Manuel Naval and his capabilities come first: state/concurrency, integration/persistence and testing/specifications, each linked to original examples. Babel/Renfe/AWAI appear only in experience. A directory opens nine Android, Flutter, SwiftUI, integration and tooling projects. Four earlier projects add Java MVC, a collaborative REST API, Angular editing state and Flutter environment configuration, with their original learning scope and validation limits. [PRODUCT.md](PRODUCT.md) records audience and claim boundaries. [Impeccable](https://github.com/pbakaus/impeccable) is a design reference; its engine is not installed or shipped.

Captures come from original demos in Android API 37 emulator and iOS 27.2 Simulator, in English with fictional data. Professional contexts are described separately without corporate materials. HTML owns navigation, landmarks and native `details/summary` disclosures. The page loads no JavaScript; the lab index uses CSS sticky on desktop. Focus, selection, controls and reflow belong to the visual system. Third-party notices and licenses remain intact.

Local app checks cited by the redesign: Rumbo: 35 JVM/9 emulator checks and Bitácora: 37 controller/widget checks plus native persistence. Each repository documents validation limits. Follow each project’s CI link for its current runs. Bitácora SwiftUI adds a native iOS demonstration with 43 macOS tests, two native XCTest cases and Simulator evidence. VoiceOver, physical-device protection and stores remain separate checks.

## Hosting

GitHub Pages serves `main` → `/docs` at the project URL above. `site.json` defines canonical URLs. Earlier `/portfolio/` URLs redirect through compatibility pages in `navalcode.github.io`; association, authentication and privacy resources are maintained separately. The website uses the github.io address; no custom domain is configured.

Original source, copy, design and demo captures: [MIT](LICENSE), Manuel Naval, 2026. Fonts, GSAP and linked projects retain their own licenses and attribution. See [credits and notices](THIRD_PARTY.md) and [pinned sources/hashes](third_party.json).
