import unittest

from utils.block_to_block_type import BLOCK_TYPES, block_to_block_type

class TestUtils(unittest.TestCase):
    def test_heading_blocks(self):

        heading_blocks = [
            "# h1 heading",
            "## h2 heading",
            "###### h6 heading",
            "not a heading"
        ]

        block_types = list(map(block_to_block_type, heading_blocks))

        expected_result = [
            BLOCK_TYPES.HEADING,
            BLOCK_TYPES.HEADING,
            BLOCK_TYPES.HEADING,
            BLOCK_TYPES.PARAGRAPH
        ]

        self.assertListEqual(block_types, expected_result)

    def test_code_blocks(self):
        code_blocks = [
            "```This is a code block```",
            "```This is not a code block",
            "``` This is another code block```",
            "This is not a code block```"
        ]

        block_types = list(map(block_to_block_type, code_blocks))

        expected_result = [
            BLOCK_TYPES.CODE,
            BLOCK_TYPES.PARAGRAPH,
            BLOCK_TYPES.CODE,
            BLOCK_TYPES.PARAGRAPH
        ]

        self.assertListEqual(block_types, expected_result)

    def test_quote_blocks(self):
        quote_blocks = [
            "> This is a quote block",
            "This is not",
            "> This is a code block"
        ]

        block_types = list(map(block_to_block_type, quote_blocks))

        expected_result = [
            BLOCK_TYPES.QUOTE,
            BLOCK_TYPES.PARAGRAPH,
            BLOCK_TYPES.QUOTE
        ]

        self.assertListEqual(block_types, expected_result)

    def test_unordered_list_blocks(self):
        unordered_list_blocks = [
            "- This is an unordered list",
            "-This is not an unordered list",
            "This is a paragraph"
        ]

        block_types = list(map(block_to_block_type, unordered_list_blocks))

        expected_result = [
            BLOCK_TYPES.UNORDERED_LIST,
            BLOCK_TYPES.PARAGRAPH,
            BLOCK_TYPES.PARAGRAPH
        ]

        self.assertListEqual(block_types, expected_result)

    def test_ordered_list_blocks(self):
        ordered_list_blocks = [
            ". This is an ordered list",
            ".This is not",
            "This is a paragraph"
        ]

        block_types = list(map(block_to_block_type, ordered_list_blocks))

        expected_result = [
            BLOCK_TYPES.ORDERED_LIST,
            BLOCK_TYPES.PARAGRAPH,
            BLOCK_TYPES.PARAGRAPH
        ]

        self.assertListEqual(block_types, expected_result)




if __name__ == '__main__':
    unittest.main()
