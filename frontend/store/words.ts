/*
 * Project Name: ASL Dictionary
 * File Name: dictionary.js
 * Programmer: Kai Princes
 * Date: Sat, Apr 11, 2020
 * Description: This file contains the Vuex Store module for the dictionary.
 */

import { GetterTree, ActionTree, MutationTree } from 'vuex'
import { stateHelpers, mutationHelpers, getterHelpers } from '@/utils/store'
import { RouteSlug, slugToWord, wordToSlug } from '~/utils/helpers'
import SignWord from '~/models/SignWord'
import Media, { fromImage, fromVideo } from '~/models/Media'

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
  getBySlug: ({ words: stateWords }) => (
    slug: RouteSlug,
    words: Array<SignWord>
  ) => {
    // Static Generation
    // ..Use given word list, if provided
    const _words = words ?? stateWords

    const foundWord = _words.find(
      (x: SignWord) => String(x.id) === String(slug)
    )
    const word = foundWord ?? slugToWord(String(slug), _words)
    return word
  },
  getSlug: ({ words: stateWords }) => (
    word: SignWord,
    words: Array<SignWord>
  ) => {
    // Static Generation
    // ..Use given word list, if provided
    const _words = words ?? stateWords

    return wordToSlug(word, _words)
  },
  getDefinitionVideos: () => (word: SignWord) => {
    const signVideos = word.videos
    const definitionVideos = signVideos.filter((video) => !video.isSentence)
    return definitionVideos
  },
  getSentenceVideos: () => (word: SignWord) => {
    const signVideos = word.videos
    const sentenceVideos = signVideos.filter((video) => video.isSentence)
    return sentenceVideos
  },
  getPreviewMedia: (_state, { getDefinitionVideos }) => (
    word: SignWord
  ): Media | null => {
    // Find first image, or video
    if (word.images.length) {
      const image = word.images[0]
      return fromImage(image)
    } else if (word.videos.length) {
      const definitionVideos = getDefinitionVideos(word)
      const definitionVideo = definitionVideos.length
        ? definitionVideos[0]
        : null
      const video = definitionVideo ?? word.videos[0]
      return fromVideo(video)
    } else {
      return null
    }
  },
}
