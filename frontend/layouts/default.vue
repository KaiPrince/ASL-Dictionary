<template>
  <BaseLayout>
    <v-content class="pt-12">
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <BasicFooter />
  </BaseLayout>
</template>

<script lang="ts">
import Vue from 'vue'
import BaseLayout from '~/layouts/base.vue'
import BasicFooter from '~/components/BasicFooter.vue'
export default Vue.extend({
  name: 'DefaultLayout',
  components: {
    BaseLayout,
    BasicFooter,
  },
})
</script>
