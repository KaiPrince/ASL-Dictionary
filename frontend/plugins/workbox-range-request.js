/*
 * Project Name: ASL Dictionary
 * File Name: workbox-range-request.js
 * Programmer: Kai Prince
 * Date: Tue, Apr 28, 2020
 * Description: This file contains a plugin for the service worker to work on
 *  Safari browsers.
 */

workbox.routing.registerRoute(
  /optimized.*\.(mp4|webm|mov)/i,
  new workbox.strategies.CacheFirst({
    plugins: [new workbox.rangeRequests.Plugin()],
  }),
  'GET'
)
