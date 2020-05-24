<!--
* Project Name: ASL Dictionary
* File Name: WordCard.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a component to display a SignWord entry.
-->

<template>
  <v-row justify="center">
    <v-col :class="mediaHeight ? 'flex-grow-0' : null">
      <v-card
        raised
        nuxt
        :to="{ name: 'detail-slug', params: { slug: word.id } }"
      >
        <v-card-title>
          {{ word.label }}
        </v-card-title>
        <MediaDisplay
          v-if="getPreviewMedia"
          ref="media"
          v-resize="autoSizeText"
          v-intersect.quiet="autoSizeText"
          :item="getPreviewMedia"
          :height="mediaHeight"
          :class="[cardFooter ? null : 'mb-n2']"
          preview
        />
        <v-card-text
          v-if="cardFooter"
          class="text-truncate"
          :style="{
            maxWidth: textWidth + 'px',
          }"
        >
          {{ cardFooter }}
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
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
    mediaHeight: {
      type: Number,
      default: undefined,
    },
  },
  data() {
    return {
      textWidth: this.mediaHeight ? 0 : null,
    } as { textWidth: number | null }
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
  mounted() {
    this.autoSizeText()
  },
  updated() {
    this.autoSizeText()
  },
  methods: {
    autoSizeText(): void {
      const el = this.$refs.media as Vue
      this.textWidth = el.$el.clientWidth
    },
  },
})
</script>
