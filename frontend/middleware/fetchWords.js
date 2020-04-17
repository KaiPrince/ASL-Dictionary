/*
 * Project Name: ASL Dictionary
 * File Name: fetchWords.js
 * Programmer: Kai Prince
 * Date: Fri, Apr 17, 2020
 * Description: This file contains middleware to fetch Words.
 */

export default function ({ store }) {
  // Fetch Words from API
  const { loading, words } = store.state.words
  if (!loading && !words.length) {
    return store.dispatch('words/fetchWords')
  }
}
