/*
 * Project Name: ASL Dictionary
 * File Name: _wordToSlug.js
 * Programmer: Kai Prince
 * Date: Sat, May 23, 2020
 * Description: This file contains a duplicate of the wordToSlug function.
 *  This exists only because the original is written is TS, and won't load
 *  in the nuxt.config.js file.
 *  To fix this problem, install webpack and ts-loader, and compile this
 *  file to JS in the build step in package.json, then import the .js
 *  version in nuxt.config.js
 */

/// Consumes a SignWord, Array<SignWord> and produces a string.
export const wordToSlug = (word, words) => {
  const matchedWords = words.filter((x) => x.label === word.label)
  const properties = {
    label: word.label,
    index: matchedWords.indexOf(word),
  }

  return propertiesToSlug(properties)
}

const propertiesToSlug = (props) =>
  // 'hello' or 'hello-2' because human lists start at 1
  props.index ? `${props.label}-${props.index + 1}` : props.label
