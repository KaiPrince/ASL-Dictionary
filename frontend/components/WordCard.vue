<!--
* Project Name: ASL Dictionary
* File Name: WordCard.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a component to display a SignWord entry.
-->

<template>
  <v-card raised nuxt :to="{ name: 'detail-id', params: { id: word.id } }">
    <v-card-title>
      {{ word.label }}
    </v-card-title>
    <MediaDisplay
      v-if="getPreviewMedia"
      :item="getPreviewMedia"
      :class="cardFooter ? null : 'mb-n2'"
    />
    <v-card-text v-if="cardFooter" class="text-truncate">
      {{ cardFooter }}
    </v-card-text>
  </v-card>
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue'
import SignWord from '~/models/SignWord'
import MediaDisplay from '~/components/MediaDisplay.vue'
import Media, { fromImage, fromVideo } from '~/models/Media'
export default Vue.extend({
  name: 'WordCard',
  components: { MediaDisplay },
  props: {
    word: {
      type: Object,
      required: true,
    } as PropOptions<SignWord>,
  },
  computed: {
    getPreviewMedia(): Media | null {
      // Find first image, or video
      if (this.word.images.length) {
        const image = this.word.images[0]
        return fromImage(image)
      } else if (this.word.videos.length) {
        const video = this.word.videos[0]
        return fromVideo(video)
      } else {
        return null
      }
    },
    cardFooter(): string {
      const caption = this.getPreviewMedia ? this.getPreviewMedia.caption : ''
      return this.word.description || caption
    },
  },
})
</script>
