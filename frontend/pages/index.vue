<!--
* Project Name: ASL Dictionary
* File Name: index.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains the home page for the project.
-->

<template>
  <v-container>
    <WordSearchBar :words="words" :value.sync="filterText" />
    <v-row
      class="mt-10"
      align="center"
      justify="space-around"
      align-content="space-around"
    >
      <v-progress-circular v-if="loading" indeterminate />
      <v-col v-for="word in filterWords" :key="word.id" lg="4">
        <v-slide-y-reverse-transition>
          <WordCard :word="word" width="268" />
        </v-slide-y-reverse-transition>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapActions, mapGetters } from 'vuex'
import SignWord from '~/models/SignWord'
import WordCard from '~/components/WordCard.vue'
import WordSearchBar from '~/components/WordSearchBar.vue'
export default Vue.extend({
  name: 'IndexPage',
  components: {
    WordCard,
    WordSearchBar,
  },
  data() {
    return {
      filterText: '',
    }
  },
  computed: {
    ...mapGetters('words', ['words', 'loading']),
    filterWords(): Array<SignWord> {
      if (!this.filterText) {
        return this.words
      }

      return this.words.filter((word: SignWord) =>
        word.label.toLowerCase().includes(this.filterText.toLowerCase())
      )
    },
  },
  mounted() {
    this.fetchWords()
  },
  methods: {
    ...mapActions('words', ['fetchWords']),
  },
})
</script>
