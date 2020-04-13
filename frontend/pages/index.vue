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
    <v-row v-if="loading" justify="center">
      <v-progress-circular indeterminate />
    </v-row>
    <v-row class="mt-10" justify="space-around" align-content="space-around">
      <v-col v-for="word in filterWords" :key="word.id" lg="4">
        <v-slide-y-reverse-transition>
          <WordCard :word="word" :width="cardWidth" />
        </v-slide-y-reverse-transition>
      </v-col>
      <p v-if="!loading && !filterWords.length">
        There's nothing here...
      </p>
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
    cardWidth(): number {
      return this.filterWords.length < 3 ? 400 : 268
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
