/*
 * Project Name: ASL Dictionary
 * File Name: WordSlug.spec.ts
 * Programmer: Kai Prince
 * Date: Sat, May 23, 2020
 * Description: This file contains unit tests for the parseSlug function.
 */

import { wordToSlug, slugToWord, parseSlug } from '~/utils/helpers'
import SignWord from '~/models/SignWord'

const genWord = (id: number, label: string): SignWord => ({
  id,
  label,
  description: '',
  synonyms: '',
  images: [],
  videos: [],
  seeAlso: [],
})
const labelAndSlug = [
  // [ label, slug ]
  ['hello', 'hello'],
  ['hello', 'hello-2'],
  ['hell-o', 'hell-o'],
  ['2-hello', '2-hello'],
]

const signWords: Array<SignWord> = labelAndSlug.map(([label], i) =>
  genWord(i, label)
)

describe('Parse Slug', () => {
  test.each([
    ['hello-2', 'hello', 2],
    ['hello', 'hello', 0],
    ['hell-o', 'hell-o', 0],
    ['2-hello', '2-hello', 0],
    ['hello-0', 'hello', 0],
  ])('%p -> %p, %p', (slug, assertLabel, assertIndex) => {
    // Arrange

    // Act
    const { label, index } = parseSlug(slug)

    // Assert
    expect(label).toBe(assertLabel)
    expect(index).toBe(assertIndex)
  })
})

describe('Word to Slug', () => {
  const testCases = labelAndSlug.map(([_label, slug], i) => [
    signWords[i],
    slug,
    signWords,
  ])
  test.each(testCases)('%p -> %p', (word, assertSlug, words) => {
    // Arrange

    // Act
    const slug = wordToSlug(word as SignWord, words as Array<SignWord>)

    // Assert
    expect(slug).toBe(assertSlug)
  })
})

describe('Slug to Word', () => {
  const testCases = labelAndSlug.map(([_label, slug], i) => [
    slug,
    signWords[i],
    signWords,
  ])

  test.each(testCases)('%p -> %p', (slug, assertWord, words) => {
    // Arrange

    // Act
    const word = slugToWord(slug as string, words as Array<SignWord>)

    // Assert
    expect(word).toBe(assertWord)
  })
})
