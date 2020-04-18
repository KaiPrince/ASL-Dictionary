/*
 * Project Name: ASL Dictionary
 * File Name: SignVideo.ts
 * Programmer: Kai Prince
 * Date: Sat, Apr 11, 2020
 * Description: This file contains the definition of the SignVideo model.
 */

export default interface SignVideo {
  id: string
  altText: string
  caption: string
  videoFile: string
  optimizedVideoFile: string
  thumbnailFile: string
}
