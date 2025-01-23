from enum import Enum

from src.classes.leafnode import LeafNode



class TEXT_TYPE(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def text_node_to_html_node(self):
        match self.text_type:
            case TEXT_TYPE.TEXT:
                return LeafNode(None, self.text, None)
            case TEXT_TYPE.BOLD:
                return LeafNode("b", self.text, None)
            case TEXT_TYPE.ITALIC:
                return LeafNode("i", self.text, None)
            case TEXT_TYPE.CODE:
                return LeafNode("code", self.text, None)
            case TEXT_TYPE.LINK:
                return LeafNode("a", self.text, {"href": self.url})
            case TEXT_TYPE.IMAGE:
                return LeafNode("img", None, {"src": self.url, "alt": self.text})
            case _:
                raise ValueError()

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

