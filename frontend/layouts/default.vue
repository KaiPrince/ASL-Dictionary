<template>
  <v-app>
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

<script>
export default {
  name: 'DefaultLayout',
}
</script>
