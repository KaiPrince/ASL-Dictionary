<!--
* Project Name: ASL Dictionary
* File Name: MediaCard.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a component which shows an image or video
	in a Material Design card.
-->

<template>
  <v-card :width="width">
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
      <video v-else :width="width" controls autoplay loop muted>
        <source :src="item.src" type="video/mp4" />
        {{ item.altText }}
      </video>
    </div>
    <v-card-text>{{ item.caption }}</v-card-text>
  </v-card>
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue'
import Media from '~/models/Media'
export default Vue.extend({
  name: 'MediaCard',
  props: {
    item: {
      type: Object,
      required: true,
    } as PropOptions<Media>,
    width: {
      type: Number,
      default: 400,
    },
  },
  computed: {
    imageMinHeight(): number {
      return (3 / 4) * this.width
    },
  },
})
</script>
