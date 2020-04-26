<!--
* Project Name: ASL Dictionary
* File Name: basic.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a simple layout with a navbar.
-->

<template>
  <v-app>
    <v-app-bar flat app dense>
      <v-btn icon to="/" nuxt>
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-spacer />
      <v-toolbar-items>
        <WordSearchBar :words="words" :on-change="goToDetails" app-bar />
      </v-toolbar-items>
    </v-app-bar>
    <v-content class="pt-12">
      <v-progress-linear v-if="loading" indeterminate />
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer app tile absolute>
      <span>Made by Kai Prince</span>
    </v-footer>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapGetters } from 'vuex'
import WordSearchBar from '~/components/WordSearchBar.vue'
export default Vue.extend({
  name: 'BasicLayout',
  components: {
    WordSearchBar,
  },
  computed: {
    ...mapGetters('words', ['words', 'loading']),
  },
  methods: {
    goToDetails(wordId: number): void {
      this.$router.push({
        name: 'detail-id',
        params: { id: wordId.toString() },
      })
    },
  },
})
</script>
