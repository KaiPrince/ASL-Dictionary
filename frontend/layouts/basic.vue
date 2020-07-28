<!--
* Project Name: ASL Dictionary
* File Name: basic.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a simple layout with a navbar.
-->

<template>
  <BaseLayout>
    <v-app-bar flat app dense>
      <v-btn icon to="/" nuxt>
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-spacer />
      <v-toolbar-items>
        <WordSearchBar
          :words="words"
          :on-change="goToDetails"
          app-bar
          class="my-auto"
        />
      </v-toolbar-items>
    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <BasicFooter />
  </BaseLayout>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapGetters } from 'vuex'
import BaseLayout from '~/layouts/base.vue'
import WordSearchBar from '~/components/WordSearchBar.vue'
import BasicFooter from '~/components/BasicFooter.vue'
export default Vue.extend({
  name: 'BasicLayout',
  components: {
    BaseLayout,
    WordSearchBar,
    BasicFooter,
  },
  computed: {
    ...mapGetters('words', ['words', 'loading']),
  },
  methods: {
    goToDetails(wordId: number): void {
      this.$router.push({
        name: 'detail-slug',
        params: { slug: wordId.toString() },
      })
    },
  },
})
</script>
