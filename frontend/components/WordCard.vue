<!--
* Project Name: ASL Dictionary
* File Name: WordCard.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a component to display a SignWord entry.
-->

<template>
  <v-card
    class="mx-auto"
    :max-width="width"
    raised
    nuxt
    :to="{ name: 'detail', query: { id: word.id } }"
  >
    <v-card-title>
      {{ word.label }}
    </v-card-title>
    <MediaDisplay
      v-if="getPreviewMedia"
      :item="getPreviewMedia"
      :video-width="width"
    />
    <v-card-text class="text-truncate">
      {{ word.description }}
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
    width: {
      type: Number,
      default: 350,
    },
  },
  computed: {
    getPreviewMedia(): Media | null {
      if (this.word.images.length) {
        const image = this.word.images[0]
        return fromImage(image)
      } else if (this.word.videos.length) {
        const video = this.word.videos[0]
        return fromVideo(video)
      } else {
      }
      return null
    },
  },
})
</script>
