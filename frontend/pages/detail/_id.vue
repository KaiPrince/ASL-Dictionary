<!--
* Project Name: ASL Dictionary
* File Name: detail.vue
* Programmer: Kai Prince
* Date: Sat, Apr 11, 2020
* Description: This file contains a detail view for a SignWord.
-->

<template>
  <v-container>
    <h1 class="display-3">
      {{ word.label }}
    </h1>
    <v-row class="mt-10" justify="space-around" align-content="space-around">
      <v-col v-for="item in media" :key="item.id" sm="6">
        <MediaCard :item="item" class="mx-auto" :media-height="500" />
      </v-col>
    </v-row>
    <p class="preserve-whitespace">
      {{ word.description }}
    </p>
    <div v-if="seeAlsoWords.length">
      <h2 class="mt-10">See Also</h2>
      <v-row align-content="space-around">
        <v-col v-for="seeAlsoWord in seeAlsoWords" :key="seeAlsoWord.id" sm="4">
          <WordCard :word="seeAlsoWord" />
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>
<script lang="ts">
import Vue from 'vue'
import { mapGetters } from 'vuex'
import SignWord from '~/models/SignWord'
import Media, { fromImage, fromVideo } from '~/models/Media'
import MediaCard from '~/components/MediaCard.vue'
import WordCard from '~/components/WordCard.vue'

export default Vue.extend({
  name: 'DetailPage',
  layout: 'basic',
  components: {
    MediaCard,
    WordCard,
  },
  middleware: ['fetchWords'],
  computed: {
    ...mapGetters('words', ['words']),
    id(): string {
      return this.$route.params.id
    },
    word(): SignWord {
      const foundWord = this.words.find(
        (x: SignWord) => String(x.id) === String(this.id)
      )
      return foundWord
    },
    media(): Array<Media> {
      const images: Array<Media> = this.word.images.map(fromImage)
      const videos: Array<Media> = this.word.videos.map(fromVideo)
      return [...images, ...videos]
    },
    seeAlsoWords(): Array<SignWord> {
      return this.words.filter((word: SignWord) =>
        this.word.seeAlso.includes(word.id)
      )
    },
  },
  created() {
    const noRouteId = !this.id && String(this.id) !== String(0)
    const wordNotFound = !this.word
    if (noRouteId || wordNotFound) {
      this.$router.replace({ name: 'index' })
    }
  },
  head() {
    const word: SignWord = this.word
    return {
      titleTemplate: '%s - ' + 'ASL Dictionary',
      title: word.label,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: 'The sign for ' + word.label + ' in ASL',
        },
      ],
    }
  },
})
</script>
<style lang="sass" scoped>
.preserve-whitespace
  white-space: pre-line
</style>
