import unittest

from classes.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf_node_p = LeafNode("p", "This is a paragraph of text.")
        leaf_node_a = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(leaf_node_p.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(leaf_node_a.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_no_tag(self):
        leaf_node_no_tag = LeafNode(None, "Just some random text")

        self.assertEqual(leaf_node_no_tag.to_html(), "Just some random text")

    def test_no_value(self):
        leaf_node_no_value = LeafNode("p")

        with self.assertRaises(ValueError):
            leaf_node_no_value.to_html()

if __name__ == "__main__":
    unittest.main()
