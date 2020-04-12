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
    <MediaDisplay
      :item="item"
      :video-width="width"
      :image-min-height="imageMinHeight"
    />
    <v-card-text>{{ item.caption }}</v-card-text>
  </v-card>
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue'
import Media from '~/models/Media'
import { MEDIA_CARD } from '~/utils/constants'
import MediaDisplay from '~/components/MediaDisplay.vue'
export default Vue.extend({
  name: 'MediaCard',
  components: { MediaDisplay },
  props: {
    item: {
      type: Object,
      required: true,
    } as PropOptions<Media>,
    width: {
      type: Number,
      default: MEDIA_CARD.width,
    },
  },
  computed: {
    imageMinHeight(): number {
      return this.width * MEDIA_CARD.imageHeightRatio
    },
  },
})
</script>
