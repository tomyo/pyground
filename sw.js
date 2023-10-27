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
      return cache.addAll(["/*"]);
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      // Attempt to fetch a fresh response from the network.
      const networkFetch = fetch(event.request)
        .then((networkResponse) => {
          // Update the cache with the fresh response.
          caches.open(CACHE).then((cache) => {
            cache.put(event.request, networkResponse.clone());
          });
          return networkResponse;
        })
        .catch(() => cachedResponse); // Fallback to cached response if network request fails.

      // Return the cached response if available, or the network response.
      return cachedResponse || networkFetch;
    })
  );
});
