/*
 * Project Name: ASL Dictionary
 * File Name: constants.js
 * Programmer: Kai Prince
 * Date: Sun, Apr 12, 2020
 * Description: This file contains app-wide constants.
 */

const MEDIA_CARD_WIDTH = 400
const MEDIA_CARD_HEIGHT = 400
const MEDIA_CARD_IMAGE_HEIGHT_RATIO = 3 / 4 // Amount of Card space for image.
const MEDIA_CARD_IMAGE_HEIGHT =
  MEDIA_CARD_IMAGE_HEIGHT_RATIO * MEDIA_CARD_HEIGHT
export const MEDIA_CARD = {
  width: MEDIA_CARD_WIDTH,
  imageHeight: MEDIA_CARD_IMAGE_HEIGHT,
  imageHeightRatio: MEDIA_CARD_IMAGE_HEIGHT_RATIO,
}

export default { MEDIA_CARD }
