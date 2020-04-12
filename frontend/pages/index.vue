<template>
  <v-container>
    <v-autocomplete
      :items="words"
      :item-text="itemText"
      placeholder="Search..."
      autofocus
      auto-select-first
      solo
      prepend-inner-icon="mdi-magnify"
      :search-input.sync="filterText"
      :hint="hint"
      hide-no-data
    />
    <v-row
      class="mt-10"
      align="center"
      justify="space-around"
      align-content="space-around"
    >
      <v-progress-circular v-if="loading" indeterminate />
      <v-col v-for="word in filterWords" :key="word.id">
        <v-slide-y-reverse-transition>
          <WordCard :word="word" width="350" />
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
export default Vue.extend({
  name: 'IndexPage',
  components: {
    WordCard,
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
    hint(): string {
      if (!this.words.length) {
        return ''
      }

      return `Try "${this.words[0].label}"...`
    },
  },
  mounted() {
    this.fetchWords()
  },
  methods: {
    ...mapActions('words', ['fetchWords']),
    itemText(item: SignWord): string {
      return item.label
    },
  },
})
</script>
