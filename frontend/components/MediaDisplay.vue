<!--
* Project Name: ASL Dictionary
* File Name: MediaDisplay.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a component which displays an image or video.
-->

<template>
  <div>
    <v-img
      v-if="item.type === 'image'"
      :src="item.src"
      :alt="item.altText"
      contain
      :min-height="imageMinHeight"
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
    <div v-else-if="item.type === 'video'" class="d-flex">
      <video class="flex-shrink-1" autoplay loop muted>
        <source :src="item.src" type="video/mp4" />
        {{ item.altText }}
      </video>
    </div>
  </div>
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue'
import Media from '~/models/Media'
import { MEDIA_CARD } from '~/utils/constants'
export default Vue.extend({
  name: 'MediaDisplay',
  props: {
    item: {
      type: Object,
      required: true,
    } as PropOptions<Media>,
    imageMinHeight: {
      type: Number,
      default: MEDIA_CARD.imageHeight,
    },
  },
})
</script>
