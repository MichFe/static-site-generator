import unittest

from utils.extract_markdown_images import extract_markdown_images



class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_md_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertListEqual(result, expected_result)

    def test_extract_md_with_no_images(self):
        text = "This text do not have any image"
        result = extract_markdown_images(text)
        expected_result = []
        self.assertListEqual(result, expected_result)


