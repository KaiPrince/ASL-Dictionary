/*
 * Project Name: ASL Dictionary
 * File Name: Media.ts
 * Programmer: Kai Prince
 * Date: Sun, Apr 12, 2020
 * Description: This file contains the definition of the Media model.
 */

export default interface Media {
  id: number
  altText: string
  caption: string
  src: string
  type: 'image' | 'video'
}
