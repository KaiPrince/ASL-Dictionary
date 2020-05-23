/*
 * Project Name: ASL Dictionary
 * File Name: dictionary.js
 * Programmer: Kai Princes
 * Date: Sat, Apr 11, 2020
 * Description: This file contains the Vuex Store module for the dictionary.
 */

import { GetterTree, ActionTree, MutationTree } from 'vuex'
import { stateHelpers, mutationHelpers, getterHelpers } from '@/utils/store'

export const state = () => ({
  ...stateHelpers,
  words: [],
})

export type RootState = ReturnType<typeof state>

export const mutations: MutationTree<RootState> = {
  ...mutationHelpers,
  setWords(state, words) {
    state.words = words
  },
}

export const actions: ActionTree<RootState, RootState> = {
  async fetchWords({ commit }) {
    try {
      commit('setLoading', true)
      const { data } = await this.$axios.get('signwords/')
      commit('setWords', data)
    } catch (error) {
      commit('setError', error)
    } finally {
      commit('setLoading', false)
    }
  },
}

export const getters: GetterTree<RootState, RootState> = {
  ...getterHelpers,
  words: (state) => state.words,
}