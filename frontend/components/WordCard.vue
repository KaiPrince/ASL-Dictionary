<!--
* Project Name: ASL Dictionary
* File Name: WordCard.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a component to display a SignWord entry.
-->

<template>
  <v-card raised nuxt :to="{ name: 'detail-slug', params: { slug: word.id } }">
    <v-card-title>
      {{ word.label }}
    </v-card-title>
    <MediaDisplay
      v-if="getPreviewMedia"
      :item="getPreviewMedia"
      :height="mediaHeight"
      :class="[cardFooter ? null : 'mb-n2']"
      preview
    />
    <v-card-text v-if="cardFooter">
      {{ cardFooter }}
    </v-card-text>
  </v-card>
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue'
import _ from 'lodash'
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
    mediaHeight: {
      type: Number,
      default: undefined,
    },
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
      const textContent = this.word.description || caption

      const footerText = _.truncate(textContent, { length: 50 })
      return footerText
    },
  },
})
</script>
