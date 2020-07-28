<template>
  <BaseLayout>
    <v-app-bar flat app dense color="transparent">
      <v-spacer />
      <v-btn
        icon
        aria-label="Toggle dark mode"
        :aria-checked="$vuetify.theme.dark.toString()"
        @click.stop="toggleDarkMode"
      >
        <v-icon>mdi-theme-light-dark</v-icon>
      </v-btn>
      <v-btn
        icon
        aria-label="Toggle auto play"
        :aria-checked="autoplay.toString()"
        @click.stop="autoplay = !autoplay"
      >
        <v-icon>{{
          autoplay ? 'mdi-play-circle' : 'mdi-play-circle-outline'
        }}</v-icon>
      </v-btn>
      <v-btn
        icon
        aria-label="Show settings"
        @click.stop="rightDrawer = !rightDrawer"
      >
        <v-icon>mdi-cog</v-icon>
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer v-model="rightDrawer" right temporary fixed>
      <v-list>
        <v-list-item>
          <v-switch
            v-model="$vuetify.theme.dark"
            label="Dark mode"
            @change="storeDarkModePreference"
          />
        </v-list-item>
        <v-list-item>
          <v-switch v-model="autoplay" label="Autoplay" />
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main class="pt-12">
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <BasicFooter />
  </BaseLayout>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapActions, mapGetters } from 'vuex'
import BaseLayout from '~/layouts/base.vue'
import BasicFooter from '~/components/BasicFooter.vue'
export default Vue.extend({
  name: 'DefaultLayout',
  components: {
    BaseLayout,
    BasicFooter,
  },
  data() {
    return {
      rightDrawer: false,
    }
  },
  computed: {
    ...mapGetters('settings', ['settings']),
    autoplay: {
      get(): Boolean {
        return this.settings.autoplay
      },
      set(value) {
        this.updateSettings({ autoplay: value })
      },
    },
  },
  methods: {
    ...mapActions('settings', ['updateSettings']),
    toggleDarkMode() {
      const newVal = !this.$vuetify.theme.dark
      this.$vuetify.theme.dark = newVal

      this.storeDarkModePreference(newVal)
    },
    storeDarkModePreference(val: Boolean) {
      const theme = val ? 'dark' : 'light'

      // Save the current preference to localStorage
      localStorage.setItem('theme', theme)
    },
  },
})
</script>
