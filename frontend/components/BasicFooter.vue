<template>
  <v-footer app tile absolute>
    <span>Made by Kai Prince</span>
    <v-spacer />
    <v-switch v-model="$vuetify.theme.dark" label="Dark mode" dense />
  </v-footer>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'BasicFooter',
})
</script>
