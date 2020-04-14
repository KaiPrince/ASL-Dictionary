<!--
* Project Name: ASL Dictionary
* File Name: MediaDisplay.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a component which displays an image or video.
-->

<template>
  <div>
    <v-img
      v-if="item.type === 'image'"
      :src="item.src"
      :alt="item.altText"
      contain
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
    <div v-else-if="item.type === 'video'" class="d-flex">
      <video
        class="flex-shrink-1"
        :width="videoWidth"
        :controls="videoControls"
        autoplay
        loop
        muted
      >
        <source :src="item.src" type="video/mp4" />
        {{ item.altText }}
      </video>
    </div>
  </div>
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue'
import Media from '~/models/Media'
export default Vue.extend({
  name: 'MediaDisplay',
  props: {
    item: {
      type: Object,
      required: true,
    } as PropOptions<Media>,
  },
  computed: {
    onMobile(): boolean {
      // Typescript doesn't recognize $vuetify
      const _this: any = this
      return _this.$vuetify.breakpoint.smAndDown
    },
    videoWidth(): number | undefined {
      // Typescript doesn't recognize $vuetify
      const _this: any = this
      const screenWidth = _this.$vuetify.breakpoint.width
      return this.onMobile ? screenWidth - 48 : undefined
    },
    videoControls(): boolean {
      return this.onMobile
    },
  },
})
</script>
