# Web personal

[English](README.md) · [Web](https://navalcode.github.io/personal-website/es.html) · [GitHub](https://github.com/navalcode)

Fuentes de mi web personal. GitHub es el lugar principal para leer mi trabajo; la web ofrece una introducción visual y enlaza los mismos repositorios.

## Desarrollo

El sitio utiliza HTML y CSS estáticos. Python genera las páginas inglesa y española a partir del contenido de `build.py`. No hay paquetes de runtime, fuentes externas ni analítica.

```sh
python3 build.py
python3 check.py
python3 -m http.server 8048 --directory docs --bind 127.0.0.1
```

GitHub Pages publica `main` → `/docs`. `site.json` define las URL canónicas. Las direcciones anteriores `/portfolio/` redirigen mediante páginas de compatibilidad en `navalcode.github.io`; los recursos de asociación de aplicaciones, autenticación y privacidad se mantienen por separado.

## Contenido

Las descripciones enlazan código y comprobaciones ejecutadas. La imagen de Bitácora es una captura del emulador; el gráfico de Rumbo es un esquema de implementación. Cada proyecto documenta el alcance de su validación.

Fuentes, textos, diseño e imagen originales: [MIT](LICENSE), Manuel Naval, 2026. Los proyectos enlazados conservan sus licencias y atribución.
