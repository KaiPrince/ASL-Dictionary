/*
 * Project Name: Salseros Attendance
 * File Name: axios.js
 * Programmer: Kai Prince
 * Date: Sun, Apr 05, 2020
 * Description: This file contains Axios interceptors.
 */

import { toCamelCase, toSnakeCase } from '~/utils/lodash'

export default function ({ $axios }) {
  $axios.onRequest((config) => {
    config.data = toSnakeCase(config.data)
  })

  $axios.onResponse((response) => {
    response.data = toCamelCase(response.data)
  })
}
