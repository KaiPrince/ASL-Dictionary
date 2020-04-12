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
    placeholder="Search..."
    autofocus
    auto-select-first
    solo
    prepend-inner-icon="mdi-magnify"
    :search-input.sync="value"
    :hint="hint"
    hide-no-data
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
  },
  data() {
    return {
      value: '',
    }
  },
  computed: {
    hint(): string {
      if (!this.words.length) {
        return ''
      }

      const randomIndex = this.getRandomInt(0, this.words.length)
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
    getRandomInt(min: number, max: number) {
      min = Math.ceil(min)
      max = Math.floor(max)
      // The maximum is exclusive and the minimum is inclusive
      return Math.floor(Math.random() * (max - min)) + min
    },
  },
})
</script>
