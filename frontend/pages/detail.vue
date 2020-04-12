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
    <v-row
      class="mt-10"
      align="center"
      justify="space-around"
      align-content="space-around"
    >
      <v-col v-for="item in media" :key="item.id">
        <v-card width="400">
          <v-container>
            <v-row>
              <v-col>
                <div>
                  <v-img
                    v-if="item.type === 'image'"
                    :src="item.src"
                    :alt="item.altText"
                    contain
                    min-height="300"
                  >
                    <template v-slot:placeholder>
                      <v-row
                        class="fill-height ma-0"
                        align="center"
                        justify="center"
                      >
                        <v-progress-circular
                          indeterminate
                          color="grey lighten-5"
                        ></v-progress-circular>
                      </v-row>
                    </template>
                  </v-img>
                  <video v-else width="375" controls autoplay loop muted>
                    <source :src="item.src" type="video/mp4" />
                    {{ item.altText }}
                  </video>
                </div>
                <v-card-text>{{ item.caption }}</v-card-text>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
    <p class="mt-10">
      {{ word.description }}
    </p>
  </v-container>
</template>
<script lang="ts">
import Vue from 'vue'
import { mapGetters } from 'vuex'
import SignWord from '~/models/SignWord'

interface Media {
  id: number
  altText: string
  caption: string
  src: string
  type: 'image' | 'video'
}
export default Vue.extend({
  computed: {
    ...mapGetters('words', ['words']),
    word(): SignWord {
      return this.words.find(
        (x: SignWord) => x.id.toString() === this.$route.params.id.toString()
      )
    },
    media(): Array<Media> {
      const images: Array<Media> = this.word.images.map((image) => ({
        id: image.id,
        altText: image.altText,
        caption: image.caption,
        src: image.imageFile,
        type: 'image',
      }))
      const videos: Array<Media> = this.word.videos.map((video) => ({
        id: video.id,
        altText: video.altText,
        caption: video.caption,
        src: video.videoFile,
        type: 'video',
      }))
      return [...images, ...videos, ...images, ...images, ...images, ...images]
    },
  },
})
</script>
