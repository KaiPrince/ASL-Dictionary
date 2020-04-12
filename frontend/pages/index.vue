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
    <v-layout column justify-center align-center class="mt-12">
      <v-slide-y-reverse-transition>
        <v-card
          v-for="word in filterWords"
          :key="word.id"
          class="mx-auto"
          max-width="350"
          raised
          nuxt
          :to="{ name: 'detail', params: { id: word.id } }"
        >
          <v-card-title>
            {{ word.label }}
          </v-card-title>
          <v-img
            v-for="image in word.images"
            :key="image.id"
            :src="image.imageFile"
          >
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular
                  indeterminate
                  color="grey lighten-5"
                ></v-progress-circular>
              </v-row>
            </template>
          </v-img>
          <v-card-text class="text-truncate">
            {{ word.description }}
          </v-card-text>
        </v-card>
      </v-slide-y-reverse-transition>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapActions, mapGetters } from 'vuex'
import SignWord from '~/models/SignWord'
export default Vue.extend({
  name: 'IndexPage',
  components: {},
  data() {
    return {
      filterText: '',
    }
  },
  computed: {
    ...mapGetters('words', ['words']),
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
