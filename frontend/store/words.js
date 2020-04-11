/*
 * Project Name: ASL Dictionary
 * File Name: dictionary.js
 * Programmer: Kai Princes
 * Date: Sat, Apr 11, 2020
 * Description: This file contains the Vuex Store module for the dictionary.
 */

import { stateHelpers, mutationHelpers, getterHelpers } from '@/utils/store'

export const state = () => ({
  ...stateHelpers,
  words: [],
})

export const mutations = {
  ...mutationHelpers,
  setWords(state, words) {
    state.words = words
  },
}

export const actions = {
  ...getterHelpers,
  async fetchWords({ commit }) {
    try {
      const { data } = await this.$axios.get('signwords/')
      commit('setWords', data)
    } catch (error) {
      commit('setError', error)
    }
  },
}

export const getters = {
  words: (state) => state.words,
}
