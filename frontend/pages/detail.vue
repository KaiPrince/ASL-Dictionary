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
      <v-col v-for="item in media" :key="item.id">
        <MediaCard :item="item" />
      </v-col>
    </v-row>
    <p class="mt-10 preserve-whitespace">
      {{ word.description }}
    </p>
  </v-container>
</template>
<script lang="ts">
import Vue from 'vue'
import { mapGetters } from 'vuex'
import SignWord from '~/models/SignWord'
import Media, { fromImage, fromVideo } from '~/models/Media'
import MediaCard from '~/components/MediaCard.vue'

export default Vue.extend({
  name: 'DetailPage',
  layout: 'basic',
  components: {
    MediaCard,
  },
  middleware({ store }) {
    // Fetch Words from API
    const { loading, words } = store.state.words
    if (!loading && !words.length) {
      return store.dispatch('words/fetchWords')
    }
  },
  computed: {
    ...mapGetters('words', ['words']),
    word(): SignWord {
      return this.words.find(
        (x: SignWord) => x.id.toString() === this.$route.query.id.toString()
      )
    },
    media(): Array<Media> {
      const images: Array<Media> = this.word.images.map(fromImage)
      const videos: Array<Media> = this.word.videos.map(fromVideo)
      return [...images, ...videos]
    },
  },
})
</script>
<style lang="sass" scoped>
.preserve-whitespace
  white-space: pre-line
</style>
