import unittest

from classes.textnode import TEXT_TYPE, TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node_a = TextNode("This is a text node", TEXT_TYPE.BOLD)
        node_b = TextNode("This is a text node", TEXT_TYPE.BOLD)
        self.assertEqual(node_a, node_b)

    def test_not_eq(self):
        node_a = TextNode("This is a text node", TEXT_TYPE.BOLD)
        node_b = TextNode("This is a text node", TEXT_TYPE.ITALIC)
        self.assertNotEqual(node_a, node_b)

    def test_comparisson(self):
        node_a = TextNode("sample node", TEXT_TYPE.ITALIC)
        node_b = TextNode("sample node", TEXT_TYPE.ITALIC)

        self.assertTrue(node_a.__eq__(node_b))
        self.assertTrue(node_b.__eq__(node_a))

        node_c = TextNode("node c", TEXT_TYPE.BOLD)
        node_d = TextNode("node d", TEXT_TYPE.CODE)

        self.assertFalse(node_c.__eq__(node_d))
        self.assertFalse(node_d.__eq__(node_c))

    def test_representatino(self):
        node_a = TextNode("sample node", TEXT_TYPE.ITALIC)

        self.assertEqual(node_a.__repr__(), "TextNode(sample node, italic, None)")

    def test_text_to_html_node(self):
        image_text_node = TextNode("Image 1", TEXT_TYPE.IMAGE, "http://google.com/image1.jpg")
        transformed_to_html = image_text_node.text_node_to_html_node()

        # Testing image text type
        self.assertEqual(transformed_to_html.tag, 'img')
        self.assertDictEqual(
            getattr(transformed_to_html, "props"),
            {"src": image_text_node.url, "alt": image_text_node.text}
        )

        # Testing code text type
        code_text_node = TextNode("code line 1", TEXT_TYPE.CODE, None)
        converted = code_text_node.text_node_to_html_node()
        self.assertEqual(converted.tag, "code")
        self.assertEqual(converted.value, "code line 1")

if __name__ == "__main__":
    unittest.main()

