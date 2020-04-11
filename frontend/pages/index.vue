<template>
  <v-container>
    <v-autocomplete :items="words" :item-text="itemText" />
    <v-layout column justify-center align-center>
      <v-card
        v-for="word in words"
        :key="word.id"
        class="mx-auto"
        max-width="350"
        raised
      >
        <v-card-title>
          {{ word.label }}
        </v-card-title>
        <v-img
          v-for="image in word.images"
          :key="image.id"
          :src="image.imageFile"
        />
        <v-card-text class="text-truncate">
          {{ word.description }}
        </v-card-text>
      </v-card>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapActions, mapGetters } from 'vuex'
import SignWord from '~/models/SignWord'
export default Vue.extend({
  components: {},
  computed: {
    ...mapGetters('words', ['words']),
  },
  mounted() {
    this.fetchWords()
  },
  methods: {
    ...mapActions('words', ['fetchWords']),
    itemText(item: SignWord) {
      return item.label
    },
  },
})
</script>
