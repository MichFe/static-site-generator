import re
from enum import Enum

class BLOCK_TYPES(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block_md_text):
    type_patterns = {
        BLOCK_TYPES.HEADING: r"^#{1,6}",
        BLOCK_TYPES.CODE: r"^```[\s\S]*?```$",
        BLOCK_TYPES.QUOTE: r"^>",
        BLOCK_TYPES.UNORDERED_LIST: r"^- ",
        BLOCK_TYPES.ORDERED_LIST: r"^. ",
        BLOCK_TYPES.PARAGRAPH: r"",
    }

    stripped_md = block_md_text.strip("\n")
    for type, pattern in type_patterns.items():
        is_type = re.match(pattern, stripped_md) is not None

        if is_type:
            return type

    return None

