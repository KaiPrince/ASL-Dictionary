/*
 * Project Name: ASL Dictionary
 * File Name: Media.ts
 * Programmer: Kai Prince
 * Date: Sun, Apr 12, 2020
 * Description: This file contains the definition of the Media model.
 */

import SignImage from '~/models/SignImage'
import SignVideo from '~/models/SignVideo'

export default interface Media {
  id: string
  altText: string
  caption: string
  src: string
  type: 'image' | 'video'
}

export const fromImage = (image: SignImage): Media => ({
  id: 'img' + image.id,
  altText: image.altText,
  caption: image.caption,
  src: image.imageFile,
  type: 'image',
})

export const fromVideo = (video: SignVideo): Media => ({
  id: 'vid' + video.id,
  altText: video.altText,
  caption: video.caption,
  src: video.videoFile,
  type: 'video',
})
