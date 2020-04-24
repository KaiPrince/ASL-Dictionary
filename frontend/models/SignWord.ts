/*
 * Project Name: ASL Dictionary
 * File Name: SignWord.ts
 * Programmer: Kai Prince
 * Date: Sat, Apr 11, 2020
 * Description: This file contains the definition of the SignWord model.
 */

import SignImage from '~/models/SignImage'
import SignVideo from '~/models/SignVideo'

export default interface SignWord {
  id: number
  label: string
  description: string
  synonyms: string
  images: Array<SignImage>
  videos: Array<SignVideo>
  seeAlso: Array<number>
}
