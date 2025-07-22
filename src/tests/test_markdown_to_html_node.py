import unittest

from utils.markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_heading(self):
        markdown = "## This is a heading2"

        html = markdown_to_html_node(markdown).to_html()
        self.assertEqual(
            html,
            "<div><h2>This is a heading2</h2></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = "> This is a simple quote"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a simple quote</blockquote></div>",
        )

    def test_multiline_quote(self):
        md = """
> Quote line one
> Quote line two
> Quote line three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Quote line one\nQuote line two\nQuote line three</blockquote></div>",
        )

    def test_mixed_quote(self):
        md = """
> Quote line one
> Quote line two

this is another line that is not a quote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Quote line one\nQuote line two</blockquote><p>this is another line that is not a quote</p></div>",
        )

    def test_single_line_unordered_list(self):
        md = "- This is a single line unordered list"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a single line unordered list</li></ul></div>",
        )

    def test_multiline_unordered_list(self):
        md = """
        - List item 1 `inner code block`
        - List item 2 **inner bold**
        - List item 3
        """
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ul><li>List item 1 <code>inner code block</code></li><li>List item 2 <b>inner bold</b></li><li>List item 3</li></ul></div>",
        )

    def test_single_line_ordered_list(self):
        md = "1. This is a single line ordered list"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is a single line ordered list</li></ol></div>",
        )

    def test_multiline_ordered_list(self):
        md = """
        1. List item 1
        2. List item 2
        3. List item 3
        """
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ol><li>List item 1</li><li>List item 2</li><li>List item 3</li></ol></div>",
        )

if __name__ == '__main__':
    unittest.main()



