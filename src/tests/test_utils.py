import unittest

from classes.textnode import TextNode, TEXT_TYPE
from utils.splitter import split_nodes_delimiter

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


if __name__ == "__main__":
    unittest.main()
