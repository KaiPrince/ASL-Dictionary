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


class PageScraper(TestCase):
    def test_find_page_from_lifeprint(self):
        # Arrange
        query = "test"

        # Act
        links = search_lifeprint_for_page(query)

        # Assert
        expected = {"https://www.lifeprint.com/asl101/pages-signs/t/test.htm"}
        self.assertSetEqual(links, expected)


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
