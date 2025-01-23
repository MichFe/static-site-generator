import unittest

from src.classes.textnode import TextNode, TEXT_TYPE
from src.utils.splitter import split_nodes_delimiter

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
        node = TextNode("This is `code a` and this is `code b` and this is `code c`, tremendo", TEXT_TYPE.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TEXT_TYPE.CODE)
        expected_result = [
            TextNode("This is ", TEXT_TYPE.TEXT),
            TextNode("code a", TEXT_TYPE.CODE),
            TextNode(" and this is ", TEXT_TYPE.TEXT),
            TextNode("code b", TEXT_TYPE.CODE),
            TextNode(" and this is ", TEXT_TYPE.TEXT),
            TextNode("code c", TEXT_TYPE.CODE),
            TextNode(", tremendo", TEXT_TYPE.TEXT),
        ]

        self.assertListEqual(new_nodes, expected_result)

    def test_splitter_no_delimiter(self):
        node = TextNode("This is text with a `code block` word", TEXT_TYPE.TEXT)
        new_nodes = split_nodes_delimiter([node], "", TEXT_TYPE.CODE)
        expected_result = [
            TextNode("This is text with a `code block` word", TEXT_TYPE.CODE),
        ]

        self.assertListEqual(new_nodes, expected_result)


