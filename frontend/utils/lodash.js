import _ from 'lodash'
import humps from 'lodash-humps'
import createHumps from 'lodash-humps/lib/createHumps'

export const toCamelCase = humps

export const toSnakeCase = createHumps(_.snakeCase)
