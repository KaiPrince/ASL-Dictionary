<!--
* Project Name: ASL Dictionary
* File Name: MediaCard.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a component which shows an image or video
	in a Material Design card.
-->

<template>
  <v-card class="d-sm-flex">
    <MediaDisplay
      :item="item"
      :height="mediaHeight"
      :style="{
        borderTopRightRadius: $vuetify.breakpoint.xs ? null : 'revert',
        borderBottomLeftRadius: $vuetify.breakpoint.xs ? null : 'inherit',
      }"
    />
    <v-card-text v-if="item.caption" class="preserve-whitespace">{{
      item.caption
    }}</v-card-text>
  </v-card>
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
