"""
* Project Name: ASL Dictionary
* File Name: tests.py
* Programmer: Kai Prince
* Date: Fri, Apr 10, 2020
* Description: This file contains TDD tests for the webscraper app.
"""


from django.test import TestCase
from .service import (
    get_images_from_lifeprint,
    search_lifeprint_for_page,
    search_lifeprint_for_images,
    search_handspeak_for_page,
    get_images_from_handspeak,
)


class ImageScraper(TestCase):
    def test_get_all_images_from_lifeprint(self):
        # Arrange
        url = "https://www.lifeprint.com/asl101/pages-signs/t/test.htm"

        # Act
        lifeprint_links = get_images_from_lifeprint(url)

        # Assert
        expected = [
            "https://www.lifeprint.com/asl101/gifs/t/test.gif",
            "https://www.lifeprint.com/asl101/signjpegs/t/test1.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test2.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test3.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test4.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test-quiz1.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test-quiz2.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test-quiz3.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test-quiz4.jpg",
            "https://www.lifeprint.com/asl101/gifs/t/test-2.gif",
        ]
        self.assertCountEqual(lifeprint_links, expected)

    def test_get_all_images_from_lifeprint(self):
        # Arrange
        url = "https://www.handspeak.com/word/search/index.php?id=2180"

        # Act
        image_links = get_images_from_handspeak(url)

        # Assert
        expected = ["https://www.handspeak.com/word/img/t/test.jpg"]
        self.assertCountEqual(image_links, expected)


class PageScraper(TestCase):
    def test_find_page_from_lifeprint(self):
        # Arrange
        query = "test"

        # Act
        links = search_lifeprint_for_page(query)

        # Assert
        expected = {"https://www.lifeprint.com/asl101/pages-signs/t/test.htm"}
        self.assertSetEqual(links, expected)

    def test_find_page_from_handspeak(self):
        # Arrange
        query = "test"

        # Act
        link = search_handspeak_for_page(query)

        # Assert
        expected = [
            "https://www.handspeak.com/word/search/index.php?id=8254",
            "https://www.handspeak.com/word/search/index.php?id=6273",
            "https://www.handspeak.com/word/search/index.php?id=5486",
            "https://www.handspeak.com/word/search/index.php?id=5784",
            "https://www.handspeak.com/word/search/index.php?id=7196",
            "https://www.handspeak.com/word/search/index.php?id=2499",
            "https://www.handspeak.com/word/search/index.php?id=7197",
            "https://www.handspeak.com/word/search/index.php?id=1741",
            "https://www.handspeak.com/word/search/index.php?id=4350",
            "https://www.handspeak.com/word/search/index.php?id=2180",  # test
            "https://www.handspeak.com/word/search/index.php?id=2181",
            "https://www.handspeak.com/word/search/index.php?id=4985",
            "https://www.handspeak.com/word/search/index.php?id=2182",
            "https://www.handspeak.com/word/search/index.php?id=7998",
            "https://www.handspeak.com/word/search/index.php?id=4986",
            "https://www.handspeak.com/word/search/index.php?id=6031",
        ]
        self.assertCountEqual(link, expected)


class SearchForImages(TestCase):
    def test_search_for_images_from_lifeprint(self):
        # Arrange
        query = "test"

        lifeprint_links = search_lifeprint_for_images(query)

        # Assert
        expected = [
            "https://www.lifeprint.com/asl101/gifs/t/test.gif",
            "https://www.lifeprint.com/asl101/signjpegs/t/test1.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test2.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test3.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test4.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test-quiz1.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test-quiz2.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test-quiz3.jpg",
            "https://www.lifeprint.com/asl101/signjpegs/t/test-quiz4.jpg",
            "https://www.lifeprint.com/asl101/gifs/t/test-2.gif",
        ]
        self.assertCountEqual(lifeprint_links, expected)
