import unittest

from utils.extract_markdown_links import extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdon_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertListEqual(result, expected_result)
