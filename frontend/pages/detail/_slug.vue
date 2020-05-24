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
      {{ word ? word.label : '' }}
    </h1>
    <v-row class="mt-10" justify="space-around" align-content="space-around">
      <v-col v-for="item in media" :key="item.id">
        <v-row justify="center">
          <v-col class="flex-grow-0">
            <MediaCard :item="item" :media-height="350" />
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <p class="preserve-whitespace">
      {{ word ? word.description : '' }}
    </p>
    <div v-if="seeAlsoWords.length">
      <h2 class="mt-10">See Also</h2>
      <v-row align-content="space-around">
        <v-col
          v-for="seeAlsoWord in seeAlsoWords"
          :key="seeAlsoWord.id"
          class="flex-grow-0"
        >
          <WordCard :word="seeAlsoWord" :media-height="350" />
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
  asyncData({ payload }) {
    // Static Generation
    // .. This only exists because I can't get it to work in the
    // middleware. Remove it if a fix is found.
    return {
      payloadWords: payload,
    }
  },
  data() {
    // Static Generation
    return {
      payloadWords: [],
    }
  },
  middleware: ['fetchWords', 'requireWordSlug', 'forceLabelSlug'],
  computed: {
    ...mapGetters('words', ['getBySlug']),
    // Static Generation
    ...mapGetters('words', { storeWords: 'words' }),
    words(): Array<SignWord> {
      // Static Generation
      const words: Array<SignWord> = this.storeWords.length
        ? this.storeWords
        : this.payloadWords

      return words
    },
    slug(): string {
      const { slug } = this.$route.params

      return String(slug)
    },
    word(): SignWord | undefined {
      return this.getBySlug(this.slug)
    },
    media(): Array<Media> {
      const images: Array<Media> = this.word?.images.map(fromImage) ?? []
      const videos: Array<Media> = this.word?.videos.map(fromVideo) ?? []
      return [...images, ...videos]
    },
    seeAlsoWords(): Array<SignWord> {
      return this.words.filter((word: SignWord) =>
        this.word?.seeAlso.includes(word.id)
      )
    },
  },
  head() {
    // Opt-out of typing, because MetaInfo spec should allow
    // content: undefined, but TypeDef does not.
    const word: SignWord | undefined | any = this.word

    const title = word?.label
    const description = word?.label.toLocaleLowerCase()
    const titleTemplate = (s: string) => `${s} - ASL Dictionary`
    const descriptionTemplate = (s: string) =>
      `The sign for ${s} in American Sign Language`
    const image = word?.videos[0].thumbnailFile
    const video = word?.videos[0].videoFile

    const path: string = this.$route.path
    const url = word?.label
      ? `${path.slice(1, path.lastIndexOf('/'))}/${word?.label}`
      : undefined
    const urlTemplate = (s: string) => process.env.baseUrl + s

    return {
      title,
      titleTemplate,
      meta: [
        {
          hid: 'og:title',
          name: 'og:title',
          property: 'og:title',
          template: titleTemplate,
          content: title,
        },
        {
          hid: 'description',
          name: 'description',
          property: 'og:description',
          template: descriptionTemplate,
          content: description,
        },
        {
          hid: 'og:url',
          name: 'og:url',
          property: 'og:url',
          template: urlTemplate,
          content: url,
        },
        {
          hid: 'og:image',
          name: 'og:image',
          content: image,
        },
        {
          hid: 'og:video',
          name: 'og:video',
          content: video,
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
