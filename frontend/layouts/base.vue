<!--
* Project Name: ASL Dictionary
* File Name: base.vue
* Programmer: Kai Prince
* Date: Sun, Apr 26, 2020
* Description: This file contains the base layout that all other layouts extend.
-->

<template>
  <v-app>
    <v-progress-linear
      v-if="loading"
      indeterminate
      fixed
      class="app-loading-bar"
    />
    <slot></slot>
    <ConnectionStatus />
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapActions, mapGetters } from 'vuex'
import ConnectionStatus from '~/components/ConnectionStatus.vue'
export default Vue.extend({
  name: 'BaseLayout',
  components: {
    ConnectionStatus,
  },
  computed: {
    ...mapGetters('words', ['loading']),
  },
  watch: {
    '$nuxt.isOnline'(isOnline, wasOnline): void {
      if (isOnline && !wasOnline) {
        this.fetchWords()

        window.location.reload()
      }
    },
  },
  beforeMount() {
    this.updateDarkTheme()
    window
      .matchMedia('(prefers-color-scheme: dark)')
      .addListener(this.updateDarkTheme)
  },
  beforeDestroy() {
    window
      .matchMedia('(prefers-color-scheme: dark)')
      .removeListener(this.updateDarkTheme)
  },
  methods: {
    ...mapActions('words', ['fetchWords']),
    updateDarkTheme() {
      // Set the theme based on:
      // 1. Local storage
      // 2. OS preference.

      let useDarkTheme = this.$nuxt.$vuetify.theme.dark

      // Get the user's theme preference from local storage, if it's available
      const storedTheme = localStorage.getItem('theme')

      if (storedTheme === 'dark') {
        useDarkTheme = true
      } else if (storedTheme === 'light') {
        useDarkTheme = false
      } else {
        // Check for dark mode preference at the OS level
        const prefersDarkScheme = window.matchMedia(
          '(prefers-color-scheme: dark)'
        ).matches
        const prefersLightScheme = window.matchMedia(
          '(prefers-color-scheme: light)'
        ).matches

        if (prefersDarkScheme) {
          useDarkTheme = true
        } else if (prefersLightScheme) {
          useDarkTheme = false
        }
      }

      this.$nuxt.$vuetify.theme.dark = useDarkTheme
    },
  },
})
</script>
<style lang="sass" scoped>
.app-loading-bar
  z-index: 6
</style>
