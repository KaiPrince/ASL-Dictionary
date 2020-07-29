/*
 * Project Name: ASL Dictionary
 * File Name: forceLabelSlug.ts
 * Programmer: Kai Prince
 * Date: Sat, May 23, 2020
 * Description: This file contains middleware that replaces the route param
 * Id with Label.
 */
import { Middleware } from '@nuxt/types'
import { RouteSlug, wrongCase } from '~/utils/helpers'

const forceLabelSlug: Middleware = ({
  route,
  redirect,
  store: { getters, $router },
  payload,
}) => {
  const routeSlug: RouteSlug = route.params.slug

  const { 'words/getBySlug': getBySlug, 'words/getSlug': getSlug } = getters
  const word = payload ? getBySlug(routeSlug, payload) : getBySlug(routeSlug)

  if (!word) return

  // Force label-based route
  const trimZeroIndex = routeSlug.toString().endsWith('-0')
  if (
    !isNaN(routeSlug as any) ||
    wrongCase(word.label, routeSlug.toString()) ||
    trimZeroIndex
  ) {
    const slug = payload ? getSlug(word, payload) : getSlug(word)

    $router.replace({
      name: 'detail-slug',
      params: { slug },
    })

    redirect({
      name: 'detail-slug',
      params: { slug },
    })
  }
}

export default forceLabelSlug
