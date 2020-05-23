/*
 * Project Name: ASL Dictionary
 * File Name: fetchWords.js
 * Programmer: Kai Prince
 * Date: Fri, Apr 17, 2020
 * Description: This file contains middleware to fetch Words.
 */

import { Middleware } from '@nuxt/types'

const fetchWords: Middleware = async ({ store, payload }) => {
  if (payload) {
    return store.commit('setWords', payload)
  }

  // Fetch Words from API
  const { loading, words } = store.state.words
  if (!loading && !words.length) {
    return await store.dispatch('words/fetchWords')
  }
}

export default fetchWords
