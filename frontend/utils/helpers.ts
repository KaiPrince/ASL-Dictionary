/*
 * Project Name: ASL Dictionary
 * File Name: helpers.ts
 * Programmer: Kai Prince
 * Date: Sat, May 23, 2020
 * Description: This file contains helper utility functions.
 */

import SignWord from '~/models/SignWord'

export const wrongCase = (s1: string, s2: string) =>
  s1 !== s2 && s1.toUpperCase() === s2.toUpperCase()

interface WordSlug {
  label: string
  index: number
}

export type RouteSlug = string | number

export const parseSlug = (slug: string) => {
  // 'hello-2' -> hello, 2
  // 'hello' -> hello, 0
  // 'hell-o' -> hell-o, 0

  const tail = slug.split('-').reverse()[0]
  const tailIsNumber = !isNaN(parseInt(tail))

  const index = slug.includes('-') && tailIsNumber ? parseInt(tail) : 0
  const label =
    slug.includes('-') && tailIsNumber
      ? slug.slice(0, slug.lastIndexOf('-'))
      : slug

  return { label, index }
}

export const slugToProperties = (slug: string): WordSlug => {
  const { label, index: parsedIndex } = parseSlug(slug)

  // 'hello' or 'hello-2' because human lists start at 1
  const index = parsedIndex > 0 ? parsedIndex - 1 : parsedIndex

  return {
    label,
    index,
  }
}

const propertiesToSlug = (props: WordSlug): string =>
  // 'hello' or 'hello-2' because human lists start at 1
  props.index ? `${props.label}-${props.index + 1}` : props.label

/// Consumes a string, Array<SignWord> and produces a SignWord.
export const slugToWord = (
  slug: string,
  words: Array<SignWord>
): SignWord | undefined => {
  const { label, index } = slugToProperties(slug)
  const matchedWords = words.filter(
    (word) => word.label.toUpperCase() === label.toUpperCase()
  )
  const word = matchedWords[index]

  return word
}

/// Consumes a SignWord, Array<SignWord> and produces a string.
export const wordToSlug = (word: SignWord, words: Array<SignWord>): string => {
  const matchedWords = words.filter((x) => x.label === word.label)
  const properties: WordSlug = {
    label: word.label,
    index: matchedWords.indexOf(word),
  }

  return propertiesToSlug(properties)
}
