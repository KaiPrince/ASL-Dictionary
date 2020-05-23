import colors from 'vuetify/es5/util/colors'
import axios from 'axios'
import { toCamelCase } from './utils/lodash'
import { wordToSlug } from './utils/_wordToSlug'

export const META_DESCRIPTION = 'An American Sign Language dictionary'
export const FRONTEND_BASE_URL = 'https://asl-dictionary.web.app/'
export const BACKEND_BASE_URL = 'https://asl-dictionary.herokuapp.com/api/' // 'http://localhost:8000/api/'

export default {
  mode: 'universal',
  env: {
    baseUrl: process.env.BASE_URL || FRONTEND_BASE_URL,
    apiUrl: process.env.BACKEND_URL || BACKEND_BASE_URL,
  },
  /*
   ** Headers of the page
   */
  head: {
    title: 'ASL Dictionary',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: META_DESCRIPTION,
      },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: colors.blue },
  /*
   ** Global CSS
   */
  css: [],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: ['~/plugins/axios'],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: ['@nuxt/typescript-build', '@nuxtjs/vuetify'],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
  ],
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    baseURL: BACKEND_BASE_URL,
  },
  /*
   ** vuetify module configuration
   ** https://github.com/nuxt-community/vuetify-module
   */
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },
  pwa: {
    manifest: {
      name: 'ASL Dictionary',
      short_name: 'ASL',
      display: 'fullscreen',
      description: META_DESCRIPTION,
    },
    meta: {
      description: META_DESCRIPTION,
      ogHost: FRONTEND_BASE_URL,
      ogImage: true,
    },
    workbox: {
      // Cache all optimized videos in service worker
      runtimeCaching: [{ urlpattern: /optimized/i }],
      cachingExtensions: '@/plugins/workbox-range-request.js',
    },
  },
  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    extend(_config, _ctx) {},
  },
  generate: {
    async routes() {
      const { data } = await axios.get(BACKEND_BASE_URL + 'signwords/')

      const words = toCamelCase(data)

      return [
        ...words.map((word) => ({
          route: '/detail/' + word.id,
          payload: words,
        })),
        ...words.map((word) => ({
          route: '/detail/' + wordToSlug(word, words),
          payload: words,
        })),
      ]
    },
  },
}
