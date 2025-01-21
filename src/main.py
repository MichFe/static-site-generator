from textnode import TEXT_TYPE, TextNode
def main():
    text_node = TextNode("Hello", TEXT_TYPE.BOLD, "http://google.com")
    print(text_node.__repr__())

if __name__ == "__main__":
    main()
