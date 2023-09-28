// Name of the Cache.
const CACHE = "cacheV1";

// Select files for caching.
let urlsToCache = [
  "/",
  // "/scripts/brython_stdlib.js",
  // "/scripts/editor.py",
  // "/scripts/pwa-handler.js",
  // "/scripts/sw.js",
  // "/scripts/brython.js",
  "/manifest.json",
  "/scripts",
  "/brython.css",
  "/console.css",
  "/index.html",
];

// Cache all the selected items once application is installed.
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => {
      console.log("Caching started.");
      return cache.addAll(urlsToCache);
    })
  );
});

// Whenever a resource is requested, return if its cached else fetch the resourcefrom server.
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      if (response) {
        return response;
      }
      return fetch(event.request);
    })
  );
});
