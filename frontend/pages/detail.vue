<!--
* Project Name: ASL Dictionary
* File Name: detail.vue
* Programmer: Kai Prince
* Date: Sat, Apr 11, 2020
* Description: This file contains a detail view for a SignWord.
-->

<template>
  <v-container>
    <h1>
      {{ word.label }}
    </h1>
    <figure v-for="image in word.images" :key="image.id">
      <v-img
        :src="image.imageFile"
        :alt="image.altText"
        max-width="400"
        max-height="400"
      />
      <figcaption>{{ image.caption }}</figcaption>
    </figure>
    <figure v-for="video in word.videos" :key="video.id">
      <video width="400" height="400" controls autoplay loop muted>
        <source :src="video.videoFile" type="video/mp4" />
        {{ video.alt_text }}
      </video>
      <figcaption>{{ video.caption }}</figcaption>
    </figure>
    <p>
      {{ word.description }}
    </p>
  </v-container>
</template>
<script lang="ts">
import Vue from 'vue'
import { mapGetters } from 'vuex'
import SignWord from '~/models/SignWord'
export default Vue.extend({
  computed: {
    ...mapGetters('words', ['words']),
    word() {
      return this.words.find(
        (x: SignWord) => x.id.toString() === this.$route.params.id.toString()
      )
    },
  },
})
</script>
