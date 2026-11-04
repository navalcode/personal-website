# Web personal

[English](README.md) · [Web española](https://navalcode.github.io/personal-website/es.html) · [GitHub](https://github.com/navalcode)

Fuentes de la web personal de Manuel Naval. GitHub es el lugar principal para leer el trabajo; la web ofrece una entrada visual a nueve aplicaciones y laboratorios técnicos y enlaza código e historial de CI. El inglés es el idioma principal y la versión española ofrece el mismo contenido.

## Desarrollo

Python 3 genera páginas estáticas completas desde `content.json`. No requiere instalar paquetes ni un backend. IBM Plex Sans y las capturas son recursos locales; los assets tipográficos y de animación anteriores se conservan con sus licencias, pero no se cargan; no hay peticiones a CDN de fuentes ni analítica.

```sh
python3 build.py
python3 check.py
python3 -m http.server 8048 --directory docs --bind 127.0.0.1
```

Modifica el contenido, el generador de HTML, el CSS; después regenera y recarga. `check.py` comprueba claves de traducción, nueve rutas de proyectos/evidencia, recursos locales, contraste calculado y hashes de terceros. No sustituye la revisión en navegador.

## Diseño y comportamiento

[DESIGN.md](DESIGN.md) explica el sistema tipográfico IBM Plex Sans, la paleta mineral y azul y las composiciones. Primero aparecen Manuel Naval y sus habilidades: estado/concurrencia, integración/persistencia y pruebas/especificaciones, con enlaces a ejemplos. Babel/Renfe/AWAI aparecen solo en experiencia. El directorio permite explorar nueve proyectos de Android, Flutter, SwiftUI, integración y herramientas. [PRODUCT.md](PRODUCT.md) recoge público y límites. [Impeccable](https://github.com/pbakaus/impeccable) es referencia de diseño; su motor no se instala ni se incorpora a la web.

Las capturas proceden de demos propias en emulador Android API 37 e iOS Simulator 27.2, en inglés y con datos ficticios. La experiencia profesional se describe por separado, sin material corporativo. HTML resuelve navegación, regiones y controles nativos `details/summary`. La página no carga JavaScript; el índice usa sticky CSS en escritorio. Foco, selección, controles y reflow forman parte del sistema. Se conservan avisos y licencias de terceros.

Comprobaciones locales citadas por el rediseño: Rumbo: 35 JVM/9 de emulador y Bitácora: 37 de controlador/widgets más persistencia nativa. Cada repositorio documenta sus límites. Los enlaces a CI llevan a las ejecuciones actuales de cada proyecto. Bitácora SwiftUI añade una demostración iOS nativa con 43 pruebas macOS, dos casos XCTest nativos y evidencia de Simulator. VoiceOver, protección física y tiendas mantienen sus comprobaciones separadas.

## Alojamiento

GitHub Pages sirve `main` → `/docs` en la URL de proyecto enlazada. `site.json` define las URL canónicas. Las rutas anteriores `/portfolio/` redirigen mediante compatibilidad en `navalcode.github.io`; asociación, autenticación y privacidad se mantienen aparte. La web utiliza la dirección github.io, sin dominio personalizado.

Fuentes, textos, diseño y capturas originales: [MIT](LICENSE), Manuel Naval, 2026. Fuentes tipográficas, GSAP y proyectos enlazados conservan sus licencias y atribuciones. Ver [créditos y avisos](THIRD_PARTY.md) y [fuentes/hashes fijados](third_party.json).
