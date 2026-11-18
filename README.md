# Vueltito · landing

La página de Vueltito: un solo `index.html` estático, sin build, servido por GitHub Pages desde la raíz de este
repo en <https://vueltito.legios.com.ar/> (también responde en <https://vueltito.github.io/>, que redirige).

```sh
python3 -m http.server 8765   # http://localhost:8765
```

Lo que dice la página sale de lo que el sistema hace hoy (los README de la base y de cada comercio). No se nombra a
ningún cliente. Todos los botones de contacto abren WhatsApp con un mensaje ya escrito.

## Dominio

`vueltito.legios.com.ar` es un `CNAME vueltito → vueltito.github.io` en la zona de legios en Cloudflare, con proxy
(igual que `quartermaster`; la zona está en SSL *Full*). El archivo `CNAME` de este repo le dice a Pages qué dominio
servir: si algún día se saca el registro, hay que sacar también el archivo, o Pages redirige a un dominio que no
resuelve.

## Páginas internas, Markdown y agentes

La portada (`index.html`) se escribe a mano. Todo lo demás sale de `herramientas/generar_paginas.py`, que lee el
texto de `herramientas/contenido.py`:

- `rubros/` (una página por rubro, más `rubros/index.html`), `about`, `contact`, `privacy` y `404`, cada una en
  `.html` y en `.md`.
- `index.md` (la portada en Markdown: si cambia `index.html`, revisar `index_md()`), `sitemap.xml`, `llms.txt` y
  `estilo/paginas.css` (los colores salen de `index.html`).

```sh
python3 herramientas/generar_paginas.py   # después de tocar contenido.py, paginas.css o la portada
node --test pruebas/                      # verifica que lo generado esté al día, enlaces, JSON-LD, sitemap y el worker
```

Las fotos de los sistemas por rubro van en `rubros/fotos/` (ver el README de esa carpeta). `agentes/` tiene el worker
de Cloudflare que responde Markdown a quien lo pide con `Accept: text/markdown`.
