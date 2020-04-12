/*
 * Project Name: Salseros Attendance
 * File Name: store.js
 * Programmer: Kai Prince
 * Date: Sun, Apr 05, 2020
 * Description: This file contains the common functions for the Vuex Store.
 */

export const stateHelpers = {
  loading: false,
  error: null,
}

export const mutationHelpers = {
  setLoading(state, payload) {
    state.loading = payload
  },
  setError(state, payload) {
    state.error = payload
  },
}

export const getterHelpers = {
  loading: (state) => state.loading,
  error: (state) => state.error,
}
