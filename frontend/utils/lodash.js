import _ from 'lodash'

export function toCamelCase(object, whitelist) {
  // export function toCamelCase (object) {
  // whitelist is intended to be an object. Future support intended
  // to provide callable functions as values in the object.
  let camelCaseObject = _.cloneDeep(object)
  whitelist = whitelist || {}

  if (_.isArray(camelCaseObject)) {
    return _.map(camelCaseObject, function (tcc) {
      return toCamelCase(tcc, whitelist)
    })
  } else {
    camelCaseObject = _.mapKeys(camelCaseObject, (value, key) => {
      if (key in whitelist) {
        return key
      }
      return _.camelCase(key)
    })
    // Recursively apply throughout object
    return _.mapValues(camelCaseObject, (value) => {
      if (_.isPlainObject(value)) {
        return toCamelCase(value, whitelist)
      } else if (_.isArray(value)) {
        // Without this logic, arrays with primitives
        // have their values replaced with empty objects :/
        return value.map(function (subvalue) {
          if (_.isPlainObject(subvalue)) {
            return toCamelCase(subvalue, whitelist)
          }
          return subvalue
        })
      } else {
        return value
      }
    })
  }
}

export function toSnakeCase(object, whitelist) {
  // whitelist is intended to be an object. Future support intended
  // to provide callable functions as values in the object.
  let snakeCaseObject = _.cloneDeep(object)
  whitelist = whitelist || {}

  if (_.isArray(snakeCaseObject)) {
    return _.map(snakeCaseObject, function (tsc) {
      return toSnakeCase(tsc, whitelist)
    })
  } else {
    snakeCaseObject = _.mapKeys(snakeCaseObject, (value, key) => {
      if (key in whitelist) {
        return key
      }
      return _.snakeCase(key)
    })

    // Recursively apply throughout object
    return _.mapValues(snakeCaseObject, (value) => {
      if (_.isPlainObject(value)) {
        return toSnakeCase(value, whitelist)
      } else if (_.isArray(value)) {
        // Without this logic, arrays with primitives
        // have their values replaced with empty objects :/
        return value.map(function (subvalue) {
          if (_.isPlainObject(subvalue)) {
            return toSnakeCase(subvalue, whitelist)
          }
          return subvalue
        })
      } else {
        return value
      }
    })
  }
}
