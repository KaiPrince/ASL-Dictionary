<template>
  <v-app>
    <v-progress-linear v-if="loading" indeterminate />
    <v-content class="pt-12">
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer app tile absolute>
      <span>Made by Kai Prince</span>
    </v-footer>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapGetters } from 'vuex'
export default Vue.extend({
  name: 'DefaultLayout',
  computed: {
    ...mapGetters('words', ['loading']),
  },
})
</script>
