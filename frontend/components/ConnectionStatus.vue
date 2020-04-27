<!--
* Project Name: ASL Dictionary
* File Name: ConnectionStatus.vue
* Programmer: Kai Prince
* Date: Sun, Apr 26, 2020
* Description: This file contains a snackbar that display online status text.
-->

<template>
  <div>
    <v-snackbar v-model="$nuxt.isOffline" left :timeout="0">
      You're offline.
    </v-snackbar>
    <v-snackbar v-model="showOnline" left color="info" :timeout="2000">
      Back online.
    </v-snackbar>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'ConnectionStatus',
  data() {
    return {
      showOnline: false,
    } as { showOnline: Boolean }
  },
  watch: {
    '$nuxt.isOnline'(isOnline, wasOnline): void {
      if (isOnline && !wasOnline) {
        this.showOnline = true
      } else {
        this.showOnline = false
      }
    },
  },
})
</script>
