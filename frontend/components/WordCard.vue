<!--
* Project Name: ASL Dictionary
* File Name: WordCard.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a component to display a SignWord entry.
-->

<template>
  <v-card
    raised
    nuxt
    :to="{ name: 'detail-slug', params: { slug: getSlug(word) } }"
    @focus="focused = true"
    @blur="focused = false"
  >
    <v-card-title class="py-2">
      <h2>{{ word.label }}</h2>
    </v-card-title>
    <v-hover v-slot:default="{ hover }">
      <MediaDisplay
        v-if="previewMedia"
        :item="previewMedia"
        :height="mediaHeight"
        :class="[cardFooter ? null : 'mb-n2']"
        :autoplay="autoplay || hover || focused"
        :controls="$vuetify.breakpoint.xs"
        tabindex="-1"
        preview
      />
    </v-hover>
    <v-card-text v-if="cardFooter" class="pt-4">
      {{ cardFooter }}
    </v-card-text>
  </v-card>
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue'
import { mapGetters } from 'vuex'
import _ from 'lodash'
import SignWord from '~/models/SignWord'
import MediaDisplay from '~/components/MediaDisplay.vue'
import Media from '~/models/Media'
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
      focused: false,
    }
  },
  computed: {
    ...mapGetters('words', ['getPreviewMedia', 'getSlug']),
    ...mapGetters('settings', ['autoplay']),
    previewMedia(): Media | null {
      return this.getPreviewMedia(this.word)
    },
    cardFooter(): string {
      const caption = this.previewMedia ? this.previewMedia.caption : ''
      const textContent = this.word.description || caption

      const footerText = _.truncate(textContent, { length: 50 })
      return footerText
    },
  },
})
</script>
