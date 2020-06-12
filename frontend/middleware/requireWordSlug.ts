/*
 * Project Name: ASL Dictionary
 * File Name: requireWordSlug.ts
 * Programmer: Kai Prince
 * Date: Sat, May 23, 2020
 * Description: This file contains middleware the redirects if a valid slug
 *  is not given.
 */
import { Middleware } from '@nuxt/types'
import { RouteSlug } from '~/utils/helpers'

const requireWordSlug: Middleware = ({ route, store, redirect }) => {
  // Static Generation
  // ..skip the redirect
  if (process.static) return

  const routeSlug: RouteSlug = route.params.slug

  const { 'words/getBySlug': getBySlug } = store.getters
  const word = getBySlug(routeSlug)

  const noRouteId = !routeSlug && String(routeSlug) !== String(0)

  // Redirect if not found
  if (noRouteId || !word) {
    return redirect({ name: 'index' })
  }
}

export default requireWordSlug
