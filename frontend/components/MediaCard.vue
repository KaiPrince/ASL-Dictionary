<!--
* Project Name: ASL Dictionary
* File Name: MediaCard.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a component which shows an image or video
	in a Material Design card.
-->

<template>
  <v-row justify="center">
    <v-col :class="mediaHeight ? 'flex-grow-0' : null">
      <v-card>
        <MediaDisplay :item="item" :height="mediaHeight" />
        <v-card-text v-if="item.caption" class="preserve-whitespace">{{
          item.caption
        }}</v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue'
import Media from '~/models/Media'
import MediaDisplay from '~/components/MediaDisplay.vue'
export default Vue.extend({
  name: 'MediaCard',
  components: { MediaDisplay },
  props: {
    item: {
      type: Object,
      required: true,
    } as PropOptions<Media>,
    mediaHeight: {
      type: Number,
      default: undefined,
    },
  },
})
</script>
<style lang="sass" scoped>
.preserve-whitespace
  white-space: pre-line
</style>
