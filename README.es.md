# Portfolio de Manuel Naval

[English](README.md)

Web estática con inglés principal y página española completa, CSS original y enlaces a evidencia pública ejecutable. Sin JavaScript, analítica, cuentas, backend, fuentes externas o paquetes de runtime.

```sh
python3 build.py
python3 -m http.server 8048 --directory docs --bind 127.0.0.1
```

`build.py` genera ambas páginas desde contenido bilingüe revisado. GitHub Pages sirve únicamente `docs/`; las fuentes y este README no son recursos del sitio. La rama y ruta `/docs` se configuran en Pages del repositorio dedicado. Publicación independiente de los recursos existentes de autenticación/aplicaciones.

Las descripciones distinguen demos originales, laboratorios históricos, simulación y validación física. Los enlaces de CI apuntan a ejecuciones concretas. La imagen de Bitácora es una captura real de su demo pública; el gráfico de Rumbo es un esquema de implementación.

Código, textos, diseño e imagen originales: [MIT](LICENSE), Manuel Naval, 2026. Los repositorios históricos conservan licencias y atribución propias.
