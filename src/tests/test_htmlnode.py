import unittest

from classes.htmlnode import HtmlNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        html_node = HtmlNode("div", "I'm a div", None, None)
        self.assertEqual(
            html_node.__repr__(),
            "HTML_NODE(div, I'm a div, None, None)"
        )

    def test_props_to_html(self):
        html_node = HtmlNode(
            "a",
            "google",
            None,
            {
                "href": "http://google.com",
                "class": "link"
            }
        )
        node_attributes = html_node.props_to_html()

        self.assertEqual(node_attributes, ' href="http://google.com" class="link"')

    def test_props_to_html_empty(self):
        html_node = HtmlNode(
            "a",
            "google",
            None,
            None
        )
        node_attributes = html_node.props_to_html()

        self.assertEqual(node_attributes, "")

if __name__ == "__main__":
    unittest.main()
