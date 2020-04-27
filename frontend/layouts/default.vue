<template>
  <BaseLayout>
    <v-content class="pt-12">
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer app tile absolute>
      <span>Made by Kai Prince</span>
    </v-footer>
  </BaseLayout>
</template>

<script lang="ts">
import Vue from 'vue'
import BaseLayout from '~/layouts/base.vue'
export default Vue.extend({
  name: 'DefaultLayout',
  components: {
    BaseLayout,
  },
})
</script>
