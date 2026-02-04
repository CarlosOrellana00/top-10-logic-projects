const CACHE_NAME = "clima-pwa-v1";

// OJO: rutas relativas a /js/ porque sw.js está en esa carpeta
const STATIC_ASSETS = [
  "../index.html",
  "./manifest.json",
  "../css/style.css",
  "./app.js",
  "../icons/icon-192.png",
  "../icons/icon-512.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(STATIC_ASSETS))
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.map((k) => (k !== CACHE_NAME ? caches.delete(k) : null)))
    )
  );
});

// Cache-first para estáticos; para otras cosas intenta red y si falla vuelve al cache
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => {
      if (cached) return cached;
      return fetch(event.request).catch(() => caches.match("./index.html"));
    })
  );
});
