<!--
* Project Name: ASL Dictionary
* File Name: WordSearchBar.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a component for searching a SignWords list.
-->

<template>
  <v-autocomplete
    :items="words"
    :item-text="itemText"
    :item-value="itemValue"
    placeholder="Search..."
    aria-label="Search"
    auto-select-first
    solo
    prepend-inner-icon="mdi-magnify"
    :search-input.sync="value"
    :hint="hint"
    hide-no-data
    :filter="filter"
    :dense="appBar"
    :flat="appBar"
    :hide-details="appBar"
    @change="onChange"
  />
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue'
import SignWord from '~/models/SignWord'
export default Vue.extend({
  name: 'WordSearchBar',
  props: {
    words: {
      type: Array,
      required: true,
    } as PropOptions<Array<SignWord>>,
    onChange: {
      type: Function,
      default: () => {},
    },
    appBar: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      value: '',
    }
  },
  computed: {
    hint(): string | undefined {
      if (this.appBar || !this.words.length) {
        return undefined
      }

      // To generate the hint, get a random word's label (except the top)
      const randomIndex = this.getRandomInt(1, this.words.length)
      const label = this.words[randomIndex].label
      return `Try "${label}"...`
    },
  },
  watch: {
    value(newVal): void {
      this.$emit('update:value', newVal)
    },
  },
  methods: {
    itemText(item: SignWord): string {
      return item.label
    },
    itemValue(item: SignWord): number {
      return item.id
    },
    filter(item: SignWord, queryText: string, itemText: string): Boolean {
      const query = queryText.toUpperCase()

      const textMatch = itemText.toUpperCase().includes(query)

      const imagesMatch = item.images.some((image) =>
        image.altText.toUpperCase().includes(query)
      )
      const videosMatch = item.videos.some((video) =>
        video.altText.toUpperCase().includes(query)
      )

      const synonymsMatch = item.synonyms
        ? item.synonyms.toUpperCase().includes(query)
        : false

      return textMatch || imagesMatch || videosMatch || synonymsMatch
    },
    getRandomInt(min: number, max: number) {
      min = Math.ceil(min)
      max = Math.floor(max)
      // The maximum is exclusive and the minimum is inclusive
      return Math.floor(Math.random() * (max - min)) + min
    },
  },
})
</script>
