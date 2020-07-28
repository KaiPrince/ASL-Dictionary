<!--
* Project Name: ASL Dictionary
* File Name: MediaDisplay.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a component which displays an image or video.
-->

<template>
  <v-img
    v-if="item.type === 'image'"
    :src="item.src"
    :alt="item.altText"
    contain
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
  <video
    v-else-if="item.type === 'video'"
    ref="video"
    :poster="item.poster"
    :style="{
      maxHeight: height ? height + 'px' : null,
      width: height ? null : '100%',
    }"
    :autoplay="autoplay"
    :controls="controls"
    loop
    muted
    playsinline
  >
    <source v-if="preview && item.optimizedSrc" :src="item.optimizedSrc" />
    <source :src="item.src" />
    <source v-if="item.optimizedSrc" :src="item.optimizedSrc" />
    {{ item.altText }}
  </video>
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue'
import Media from '~/models/Media'
export default Vue.extend({
  name: 'MediaDisplay',
  props: {
    item: {
      type: Object,
      required: true,
    } as PropOptions<Media>,
    preview: {
      type: Boolean,
      default: false,
    },
    height: {
      type: Number,
      default: undefined,
    },
    autoplay: {
      type: Boolean,
      default: true,
    },
    controls: {
      type: Boolean,
      default: false,
    },
  },
  watch: {
    autoplay(newVal, oldVal) {
      if (oldVal === undefined) return

      const video = this.$refs.video as HTMLMediaElement

      if (newVal) {
        video.play()
      } else {
        video.pause()
      }
    },
  },
})
</script>
