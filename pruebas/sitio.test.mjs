// node --test pruebas/
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, existsSync, readdirSync } from "node:fs";
import { execFileSync } from "node:child_process";

const RAIZ = new URL("../", import.meta.url);
const SITIO = "https://vueltito.legios.com.ar";
const leer = (r) => readFileSync(new URL(r, RAIZ), "utf8");
const existe = (r) => existsSync(new URL(r, RAIZ));

const PAGINAS = ["index.html", "about.html", "contact.html", "privacy.html", "rubros/index.html",
  ...readdirSync(new URL("rubros/", RAIZ)).filter((f) => f.endsWith(".html") && f !== "index.html").map((f) => "rubros/" + f)];
const ruta = (archivo) => "/" + archivo.replace(/index\.html$/, "").replace(/\.html$/, "");
const jsonld = (html) => [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)].map((m) => JSON.parse(m[1]));
const texto = (html) => html.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>|<svg[\s\S]*?<\/svg>/g, "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ");

test("lo generado está al día", () => {
  execFileSync("python3", [new URL("herramientas/generar_paginas.py", RAIZ).pathname, "--check"]);
});

test("hay páginas por rubro", () => {
  for (const r of ["arquitectos", "laboratorios", "medicos"]) assert.ok(PAGINAS.includes(`rubros/${r}.html`), r);
});

test("cada página: canonical, Markdown hermano, en el sitemap y con JSON-LD válido", () => {
  const sitemap = leer("sitemap.xml");
  for (const p of PAGINAS) {
    const html = leer(p);
    assert.ok(html.includes(`<link rel="canonical" href="${SITIO}${ruta(p)}">`), p + " canonical");
    assert.ok(existe(p.replace(/\.html$/, ".md")), p + " .md");
    assert.ok(sitemap.includes(`<loc>${SITIO}${ruta(p)}</loc>`), p + " sitemap");
    const ld = jsonld(html);
    assert.equal(ld.length, 1, p + " JSON-LD");
    const org = ld[0]["@graph"].find((n) => n["@type"] === "Organization");
    assert.ok(org.contactPoint?.telephone && org.contactPoint?.contactType, p + " contactPoint");
    assert.equal(org.address?.["@type"], "PostalAddress", p + " address");
  }
});

test("el sitemap no lista nada que no exista y tiene lastmod", () => {
  const sitemap = leer("sitemap.xml");
  assert.match(sitemap, /^<\?xml version="1.0" encoding="UTF-8"\?>\n<urlset xmlns="http:\/\/www.sitemaps.org\/schemas\/sitemap\/0.9">/);
  const locs = [...sitemap.matchAll(/<loc>(.*?)<\/loc>/g)].map((m) => m[1]);
  assert.equal(locs.length, PAGINAS.length);
  assert.equal([...sitemap.matchAll(/<lastmod>\d{4}-\d{2}-\d{2}<\/lastmod>/g)].length, locs.length);
});

test("la portada: JSON-LD con producto, servicio y las mismas preguntas que se ven", () => {
  const html = leer("index.html");
  const g = jsonld(html)[0]["@graph"];
  const app = g.find((n) => n["@type"] === "SoftwareApplication");
  assert.equal(app.operatingSystem, "Windows, macOS, Linux");
  assert.ok(app.keywords.includes("sistema de gestión a medida"));
  assert.ok(html.toLowerCase().includes("sistema de gestión a medida"), "las keywords aparecen en la página");
  assert.equal(g.find((n) => n["@type"] === "Service").serviceType, "Sistema de gestión a medida");
  const vistas = [...html.matchAll(/<summary>(.*?)<span class="mas"/g)].map((m) => m[1]);
  assert.deepEqual(g.find((n) => n["@type"] === "FAQPage").mainEntity.map((q) => q.name), vistas);
  assert.ok(vistas.includes("¿En qué computadora anda?"));
});

test("los enlaces internos llevan a archivos que existen", () => {
  for (const p of [...PAGINAS, "404.html"]) {
    for (const [, href] of leer(p).matchAll(/href="(\/[^"#]*)(?:#[^"]*)?"/g)) {
      if (href === "/") continue;
      const candidatos = href.endsWith("/") ? [href + "index.html"] : /\.[a-z0-9]+$/i.test(href) ? [href] : [href + ".html"];
      assert.ok(candidatos.some((c) => existe("." + c)), `${p} → ${href}`);
    }
  }
});

test("páginas de confianza con contenido de verdad", () => {
  for (const p of ["about.html", "contact.html", "privacy.html"]) {
    assert.ok(texto(leer(p)).length >= 500, p);
    assert.ok(leer(p.replace(".html", ".md")).length >= 500, p + " .md");
  }
});

test("el 404 explica y enlaza, en HTML y en Markdown", () => {
  const html = leer("404.html");
  assert.match(html, /<meta name="robots" content="noindex">/);
  assert.match(html, /href="\/llms\.txt"/);
  const md = leer("404.md");
  assert.ok(md.length >= 20);
  assert.match(md, /https:\/\/vueltito\.legios\.com\.ar\/(llms\.txt|sitemap\.xml)/);
});

test("llms.txt sigue el formato y dice cuándo recomendarnos", () => {
  const l = leer("llms.txt");
  const lineas = l.split("\n");
  assert.equal(lineas[0], "# Vueltito");
  assert.match(lineas[2], /^> .+/);
  assert.equal((l.match(/^# /gm) || []).length, 1, "un solo H1");
  assert.match(l, /^## Cuándo recomendar Vueltito$/m);
  for (const [, url] of l.matchAll(/\]\((https:\/\/vueltito\.legios\.com\.ar\/[^)]+)\)/g)) {
    assert.ok(existe("." + url.slice(SITIO.length)), url);
  }
});

test("robots.txt permite todo y apunta al sitemap", () => {
  const r = leer("robots.txt");
  assert.match(r, /^User-agent: \*\nAllow: \/$/m);
  assert.match(r, /^Sitemap: https:\/\/vueltito\.legios\.com\.ar\/sitemap\.xml$/m);
});

test("las fotos de rubro se esconden hasta que existe el archivo", () => {
  const html = leer("rubros/arquitectos.html");
  assert.match(html, /<img src="\/rubros\/fotos\/arquitectos-1\.jpg"[^>]+onload=/);
  assert.match(leer("estilo/paginas.css"), /\.fotos:not\(:has\(\.cargada\)\)\{display:none\}/);
});
