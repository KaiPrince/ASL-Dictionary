<!--
* Project Name: ASL Dictionary
* File Name: index.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains the home page for the project.
-->

<template>
  <v-container>
    <WordSearchBar
      :words="words"
      :value.sync="filterText"
      :on-change="goToDetails"
    />
    <v-row class="mt-10" justify="center" justify-md="space-around">
      <v-col v-for="word in filterWords" :key="word.id" cols="10" sm="4" md="3">
        <v-lazy min-height="500">
          <SignCard :word="word" />
        </v-lazy>
      </v-col>
      <p
        v-if="!loading && !filterWords.length"
        class="text-center text--secondary"
      >
        There's nothing here...
      </p>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapActions, mapGetters } from 'vuex'
import SignWord from '~/models/SignWord'
import SignCard from '~/components/SignCard.vue'
import WordSearchBar from '~/components/WordSearchBar.vue'
export default Vue.extend({
  name: 'IndexPage',
  components: {
    SignCard,
    WordSearchBar,
  },
  middleware: ['fetchWords'],
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
        word.label.toUpperCase().includes(this.filterText.toUpperCase())
      )
    },
  },
  mounted() {
    this.fetchWords()
  },
  methods: {
    ...mapActions('words', ['fetchWords']),
    goToDetails(wordId: number): void {
      this.$router.push({
        name: 'detail-slug',
        params: { slug: wordId.toString() },
      })
    },
  },
})
</script>
