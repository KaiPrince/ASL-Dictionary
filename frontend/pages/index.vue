<template>
  <v-container>
    <v-autocomplete
      :items="words"
      :item-text="itemText"
      placeholder="Search..."
      autofocus
      auto-select-first
      solo
      prepend-inner-icon="mdi-magnify"
      :search-input.sync="filterText"
      :hint="hint"
      hide-no-data
    />
    <v-row
      class="mt-10"
      align="center"
      justify="space-around"
      align-content="space-around"
    >
      <v-progress-circular v-if="loading" indeterminate />
      <v-col v-for="word in filterWords" :key="word.id">
        <v-slide-y-reverse-transition>
          <v-card
            class="mx-auto"
            :max-width="cardWidth"
            raised
            nuxt
            :to="{ name: 'detail', query: { id: word.id } }"
          >
            <v-card-title>
              {{ word.label }}
            </v-card-title>
            <MediaDisplay
              :item="getPreviewMedia(word)"
              :video-width="cardWidth"
            />
            <v-card-text class="text-truncate">
              {{ word.description }}
            </v-card-text>
          </v-card>
        </v-slide-y-reverse-transition>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapActions, mapGetters } from 'vuex'
import SignWord from '~/models/SignWord'
import Media, { fromImage, fromVideo } from '~/models/Media'
import MediaDisplay from '~/components/MediaDisplay.vue'
export default Vue.extend({
  name: 'IndexPage',
  components: { MediaDisplay },
  data() {
    return {
      filterText: '',
    }
  },
  computed: {
    ...mapGetters('words', ['words', 'loading']),
    filterWords(): Array<SignWord> {
      if (!this.filterText) {
        return this.words
      }

      return this.words.filter((word: SignWord) =>
        word.label.toLowerCase().includes(this.filterText.toLowerCase())
      )
    },
    hint(): string {
      if (!this.words.length) {
        return ''
      }

      return `Try "${this.words[0].label}"...`
    },
    cardWidth(): number {
      return 350
    },
  },
  mounted() {
    this.fetchWords()
  },
  methods: {
    ...mapActions('words', ['fetchWords']),
    itemText(item: SignWord): string {
      return item.label
    },
    getPreviewMedia(word: SignWord): Media {
      if (word.images.length) {
        const image = word.images[0]
        return fromImage(image)
      } else {
        const video = word.videos[0]
        return fromVideo(video)
      }
    },
  },
})
</script>
