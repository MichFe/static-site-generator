class HtmlNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("All html nodes must have a value.")
        if self.tag is None:
            raise ValueError("All html nodes must have a tag.")
        html = f"<{self.tag + self.props_to_html()}>{self.value}</{self.tag}>"
        return html

    def props_to_html(self):
        if self.props is None:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTML_NODE({self.tag}, {self.value}, {self.children}, {self.props})"
