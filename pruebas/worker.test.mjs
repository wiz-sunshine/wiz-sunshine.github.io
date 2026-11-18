// node --test pruebas/
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, existsSync } from "node:fs";
import worker, { prefiereMarkdown, candidatos } from "../agentes/worker.js";

const RAIZ = new URL("../", import.meta.url);
const SITIO = "https://vueltito.legios.com.ar";

// Imita a GitHub Pages sirviendo los archivos del repo.
async function pages(entrada) {
  const url = new URL(typeof entrada === "string" ? entrada : entrada.url);
  let ruta = url.pathname;
  if (ruta.endsWith("/")) ruta += "index.html";
  else if (!/\.[a-z0-9]+$/i.test(ruta)) ruta += ".html";
  const archivo = new URL("." + ruta, RAIZ);
  if (!existsSync(archivo)) return new Response(readFileSync(new URL("404.html", RAIZ)), { status: 404, headers: { "Content-Type": "text/html; charset=utf-8", "Vary": "Accept-Encoding" } });
  const tipo = ruta.endsWith(".md") ? "text/markdown; charset=utf-8" : ruta.endsWith(".xml") ? "application/xml" : "text/html; charset=utf-8";
  return new Response(readFileSync(archivo), { headers: { "Content-Type": tipo, "Vary": "Accept-Encoding" } });
}
const pedir = (ruta, accept, method = "GET") =>
  worker.fetch(new Request(SITIO + ruta, { method, headers: accept ? { Accept: accept } : {} }), {}, {}, pages);

test("lee el Accept con sus q", () => {
  assert.equal(prefiereMarkdown("text/markdown"), true);
  assert.equal(prefiereMarkdown("text/markdown, text/html;q=0.9"), true);
  assert.equal(prefiereMarkdown("text/html, text/markdown;q=0.5"), false);
  assert.equal(prefiereMarkdown("text/html,application/xhtml+xml,*/*;q=0.8"), false);
  assert.equal(prefiereMarkdown("text/markdown;q=0"), false);
  assert.equal(prefiereMarkdown(""), false);
  assert.equal(prefiereMarkdown(null), false);
});

test("sabe dónde buscar el .md de cada ruta", () => {
  assert.deepEqual(candidatos("/"), ["/index.md"]);
  assert.deepEqual(candidatos("/about"), ["/about.md", "/about/index.md"]);
  assert.deepEqual(candidatos("/rubros/"), ["/rubros/index.md"]);
  assert.deepEqual(candidatos("/index.html"), ["/index.md"]);
  assert.deepEqual(candidatos("/sitemap.xml"), []);
});

test("la portada en Markdown, con Vary: Accept", async () => {
  const r = await pedir("/", "text/markdown");
  assert.equal(r.status, 200);
  assert.match(r.headers.get("Content-Type"), /^text\/markdown/);
  assert.match(r.headers.get("Vary"), /\bAccept\b/);
  assert.equal(r.headers.get("Link"), `<${SITIO}/>; rel="canonical"`);
  const cuerpo = await r.text();
  assert.match(cuerpo, /^# Vueltito/);
});

test("la portada en HTML sigue igual, con Vary: Accept agregado", async () => {
  for (const accept of ["text/html", null]) {
    const r = await pedir("/", accept);
    assert.equal(r.status, 200);
    assert.match(r.headers.get("Content-Type"), /^text\/html/);
    assert.equal(r.headers.get("Vary"), "Accept-Encoding, Accept");
    assert.match(await r.text(), /^<!doctype html>/);
  }
});

test("cada página tiene su Markdown", async () => {
  for (const ruta of ["/about", "/contact", "/privacy", "/rubros/", "/rubros", "/rubros/arquitectos", "/rubros/medicos", "/rubros/laboratorios"]) {
    const r = await pedir(ruta, "text/markdown");
    assert.equal(r.status, 200, ruta);
    assert.match(r.headers.get("Content-Type"), /^text\/markdown/, ruta);
    assert.match(await r.text(), /^# /, ruta);
  }
});

test("404 en Markdown, con explicación y enlaces", async () => {
  const r = await pedir("/__no-existe-xyz", "text/markdown");
  assert.equal(r.status, 404);
  assert.match(r.headers.get("Content-Type"), /^text\/markdown/);
  assert.match(r.headers.get("Vary"), /\bAccept\b/);
  const cuerpo = await r.text();
  assert.ok(cuerpo.length >= 20);
  assert.match(cuerpo, /llms\.txt/);
  assert.match(cuerpo, /sitemap\.xml/);
});

test("404 en HTML sigue siendo HTML", async () => {
  const r = await pedir("/__no-existe-xyz", "text/html");
  assert.equal(r.status, 404);
  assert.match(r.headers.get("Content-Type"), /^text\/html/);
});

test("lo que no tiene versión Markdown se entrega tal cual", async () => {
  const r = await pedir("/sitemap.xml", "text/markdown");
  assert.equal(r.status, 200);
  assert.equal(r.headers.get("Content-Type"), "application/xml");
});

test("HEAD en Markdown no manda cuerpo", async () => {
  const r = await pedir("/", "text/markdown", "HEAD");
  assert.equal(r.status, 200);
  assert.match(r.headers.get("Content-Type"), /^text\/markdown/);
  assert.equal(await r.text(), "");
});
