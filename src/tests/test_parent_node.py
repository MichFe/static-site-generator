import unittest

from src.classes.leafnode import LeafNode
from src.classes.parentnode import ParentNode



class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        parent_node_a = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            parent_node_a.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

    def test_nested_parent_node(self):
        parent_node_b = ParentNode(
            "div",
            [
                LeafNode("h1", "Shopping list", {"class": "title"}),
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "List item 1"),
                        LeafNode("li", "List item 2"),
                        LeafNode("li", "List item 3"),
                        LeafNode("li", "List item 4"),
                        LeafNode("li", "List item 5"),
                    ]

                ),
                LeafNode("hr", "---", None)
            ]
        )

        self.assertEqual(
            parent_node_b.to_html(),
            '<div><h1 class="title">Shopping list</h1><ul><li>List item 1</li><li>List item 2</li><li>List item 3</li><li>List item 4</li><li>List item 5</li></ul><hr>---</hr></div>'
        )

    def test_no_children(self):
        parent_node_c = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node_c.to_html()

    def test_no_tag(self):
        parent_node_d = ParentNode(None, [])
        with self.assertRaises(ValueError):
            parent_node_d.to_html()

if __name__ == "__main__":
    unittest.main()
