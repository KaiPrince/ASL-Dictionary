/*
 * Project Name: ASL Dictionary
 * File Name: settings.ts
 * Programmer: Kai Prince
 * Date: Fri, Jul 10, 2020
 * Description: This file contains the Vuex Store module for app settings.
 */

import { GetterTree, ActionTree, MutationTree } from 'vuex'

export const state = () => ({
  settings: {
    autoplay: false,
  },
})

export type RootState = ReturnType<typeof state>

export const mutations: MutationTree<RootState> = {
  setSettings(state, settings) {
    state.settings = settings
  },
  updateSettings(state, settings) {
    state.settings = Object.assign(state.settings, settings)
  },
}

export const actions: ActionTree<RootState, RootState> = {
  updateSettings({ commit }, settings) {
    commit('updateSettings', settings)
  },
}

export const getters: GetterTree<RootState, RootState> = {
  settings: (state) => state.settings,
  autoplay: (state) => state.settings.autoplay,
}
