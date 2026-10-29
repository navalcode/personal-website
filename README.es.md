# Web personal

[English](README.md) · [Web española](https://navalcode.github.io/personal-website/es.html) · [GitHub](https://github.com/navalcode)

Fuentes de la web personal de Manuel Naval. GitHub es el lugar principal para leer el trabajo; la web ofrece una entrada visual a ocho apps/laboratorios originales y enlaza código e historial de CI. Inglés principal y versión española sustancial.

## Desarrollo

Python 3 genera páginas estáticas completas desde `content.json`. No requiere instalar paquetes ni un backend. Outfit/Fraunces, capturas, GSAP 3.15.0 y ScrollTrigger son recursos locales; no hay peticiones a CDN de fuentes ni analítica.

```sh
python3 build.py
python3 check.py
python3 -m http.server 8048 --directory docs --bind 127.0.0.1
```

Modifica contenido, renderer, CSS o el `docs/motion.js` opcional; después regenera y recarga. `check.py` comprueba claves de traducción, ocho rutas de proyectos/evidencia, recursos locales, contraste calculado y hashes de terceros. No sustituye la revisión en navegador.

## Diseño y comportamiento

[DESIGN.md](DESIGN.md) explica el sistema visual y sus seis composiciones: hero editorial, media de Rumbo, narrativa abierta de Bitácora, índice expandible, secuencia de cuatro fases y cierre editorial. Las capturas proceden de las demos Android ejecutadas en API 37, en inglés y con datos ficticios. Los paisajes de Rumbo son Canvas originales; ningún concepto generado se presenta como una app ejecutada.

HTML conserva navegación, enlaces, landmarks y controles nativos `details/summary`. GSAP escala/desvanece media y fija el contexto del índice en escritorios suficientemente anchos/altos. `prefers-reduced-motion` desactiva esos efectos y el movimiento CSS. El contenido y las secciones expandibles siguen funcionando sin JavaScript. Las fuentes y GSAP conservan avisos/licencias propios, separados del código original MIT.

Comprobaciones locales citadas por el rediseño: Rumbo: 32 JVM/8 de emulador y Bitácora: 23 de controlador/widgets más persistencia nativa. Cada repositorio documenta sus límites. Un enlace al historial CI no afirma que las últimas fuentes hayan pasado remotamente. iOS nativo sigue siendo una ampliación gradual planificada.

## Alojamiento

GitHub Pages sirve `main` → `/docs` en la URL de proyecto enlazada. `site.json` define canonical. Las rutas anteriores `/portfolio/` redirigen mediante compatibilidad en `navalcode.github.io`; asociación, autenticación y privacidad se mantienen aparte. No restaurar el dominio abandonado ni publicar el workspace de coordinación.

Fuentes, textos, diseño y capturas originales: [MIT](LICENSE), Manuel Naval, 2026. Fuentes tipográficas, GSAP y proyectos enlazados conservan sus licencias y atribuciones. Ver [créditos y avisos](THIRD_PARTY.md) y [fuentes/hashes fijados](third_party.json).
