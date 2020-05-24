<template>
  <v-row v-if="mediaHeight" justify="center">
    <v-col class="flex-grow-0">
      <MediaCard v-if="media" :item="media" :media-height="mediaHeight" />
      <WordCard v-else-if="word" :word="word" :media-height="mediaHeight" />
    </v-col>
  </v-row>
  <MediaCard v-else-if="media" :item="media" :media-height="mediaHeight" />
  <WordCard v-else-if="word" :word="word" :media-height="mediaHeight" />
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue'
import Media from '~/models/Media'
import SignWord from '~/models/SignWord'
import MediaCard from '~/components/MediaCard.vue'
import WordCard from '~/components/WordCard.vue'

export default Vue.extend({
  name: 'SignCard',
  components: {
    MediaCard,
    WordCard,
  },
  props: {
    media: {
      type: Object,
      required: false,
      default: null,
    } as PropOptions<Media | null>,
    word: {
      type: Object,
      required: false,
      default: null,
    } as PropOptions<SignWord | null>,
    mediaHeight: {
      type: Number,
      default: undefined,
    },
  },
})
</script>
