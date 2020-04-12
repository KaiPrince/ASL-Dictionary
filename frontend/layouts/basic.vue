<!--
* Project Name: ASL Dictionary
* File Name: basic.vue
* Programmer: Kai Prince
* Date: Sun, Apr 12, 2020
* Description: This file contains a simple layout with a navbar.
-->

<template>
  <v-app>
    <v-app-bar dense flat fixed>
      <v-btn icon to="/" nuxt>
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
    </v-app-bar>
    <v-content class="pt-12">
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer app>
      <span>Made by Kai Prince</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'BasicLayout',
}
</script>
