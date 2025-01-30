import unittest

from classes.textnode import TextNode, TEXT_TYPE
from utils.splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestUtils(unittest.TestCase):
    def test_splitter(self):
        node = TextNode("This is text with a `code block` word", TEXT_TYPE.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TEXT_TYPE.CODE)
        expected_result = [
            TextNode("This is text with a ", TEXT_TYPE.TEXT),
            TextNode("code block", TEXT_TYPE.CODE),
            TextNode(" word", TEXT_TYPE.TEXT),
        ]

        self.assertListEqual(new_nodes, expected_result)

    def test_splitter_multiple(self):
        node = TextNode("This is `code a` and this is `code b` and this is `code c`, terrific", TEXT_TYPE.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TEXT_TYPE.CODE)
        expected_result = [
            TextNode("This is ", TEXT_TYPE.TEXT),
            TextNode("code a", TEXT_TYPE.CODE),
            TextNode(" and this is ", TEXT_TYPE.TEXT),
            TextNode("code b", TEXT_TYPE.CODE),
            TextNode(" and this is ", TEXT_TYPE.TEXT),
            TextNode("code c", TEXT_TYPE.CODE),
            TextNode(", terrific", TEXT_TYPE.TEXT),
        ]

        self.assertListEqual(new_nodes, expected_result)

    def test_splitter_bold(self):
        node = TextNode("This is a text with **bold** text", TEXT_TYPE.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TEXT_TYPE.BOLD)
        expected_result = [
            TextNode("This is a text with ", TEXT_TYPE.TEXT),
            TextNode("bold", TEXT_TYPE.BOLD),
            TextNode(" text", TEXT_TYPE.TEXT),
        ]

        self.assertListEqual(new_nodes, expected_result)

    def test_splitter_malformed_md(self):
        node = TextNode("This is a malformed md *bold is not closed", TEXT_TYPE.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "*", TEXT_TYPE.BOLD)

    def test_splitter_no_delimiter(self):
        node = TextNode("This is text with a `code block` word", TEXT_TYPE.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "", TEXT_TYPE.CODE)

class TestImageSplitter(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TEXT_TYPE.TEXT,
        )
        result = split_nodes_link([node])
        expected_result = [
            TextNode("This is text with a link ", TEXT_TYPE.TEXT),
            TextNode("to boot dev", TEXT_TYPE.LINK, "https://www.boot.dev"),
            TextNode(" and ", TEXT_TYPE.TEXT),
            TextNode(
                "to youtube", TEXT_TYPE.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertListEqual(result, expected_result)

class TestSlitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TEXT_TYPE.TEXT,
        )
        result = split_nodes_link([node])
        expected_result =[
            TextNode("This is text with a link ", TEXT_TYPE.TEXT),
            TextNode("to boot dev", TEXT_TYPE.LINK, "https://www.boot.dev"),
            TextNode(" and ", TEXT_TYPE.TEXT),
            TextNode(
                "to youtube", TEXT_TYPE.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertListEqual(result, expected_result)

    def test_split_nodes_link_text_without_links(self):
        node = TextNode("This text do not have any links", TEXT_TYPE.TEXT)
        result = split_nodes_link([node])
        expected_result = [
            TextNode("This text do not have any links", TEXT_TYPE.TEXT)
        ]
        self.assertListEqual(result, expected_result)

    def test_split_nodes_link_empty_node_list(self):
        nodes = []
        result = split_nodes_link(nodes)
        expected_result = []
        self.assertListEqual(result, expected_result)

class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode(
            "This is a ![image one](https://my-first-image.com) text with ![image two](https://my-second-image.com)",
            TEXT_TYPE.TEXT
        )
        result = split_nodes_image([node])
        expected_result = [
            TextNode("This is a ", TEXT_TYPE.TEXT),
            TextNode("image one", TEXT_TYPE.IMAGE, "https://my-first-image.com"),
            TextNode(" text with ", TEXT_TYPE.TEXT),
            TextNode("image two", TEXT_TYPE.IMAGE, "https://my-second-image.com"),
        ]
        self.assertListEqual(result, expected_result)

    def test_split_nodes_image_text_without_images(self):
        node = TextNode("This text do not have any images", TEXT_TYPE.TEXT)
        result = split_nodes_image([node])
        expected_result = [
            TextNode("This text do not have any images", TEXT_TYPE.TEXT)
        ]
        self.assertListEqual(result, expected_result)

    def test_split_nodes_image_empty_node_list(self):
        nodes = []
        result = split_nodes_image(nodes)
        expected_result = []
        self.assertListEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
