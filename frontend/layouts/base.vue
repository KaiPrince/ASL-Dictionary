<!--
* Project Name: ASL Dictionary
* File Name: base.vue
* Programmer: Kai Prince
* Date: Sun, Apr 26, 2020
* Description: This file contains the base layout that all other layouts extend.
-->

<template>
  <v-app>
    <v-progress-linear v-if="loading" indeterminate />
    <slot></slot>
    <ConnectionStatus />
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapActions, mapGetters } from 'vuex'
import ConnectionStatus from '~/components/ConnectionStatus.vue'
export default Vue.extend({
  name: 'BaseLayout',
  components: {
    ConnectionStatus,
  },
  computed: {
    ...mapGetters('words', ['loading']),
  },
  watch: {
    '$nuxt.isOnline'(isOnline, wasOnline): void {
      if (isOnline && !wasOnline) {
        window.location.reload()
      }
    },
  },
  methods: {
    ...mapActions('words', ['fetchWords']),
  },
})
</script>
