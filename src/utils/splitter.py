from classes.textnode import TEXT_TYPE, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        node_text = old_node.text
        new_nodes += split_text(node_text, delimiter, text_type)

    print(f"Given old_nodes: {old_nodes}, delimiter: {delimiter}, text_type: {text_type}")
    print(f"new_nodes: {new_nodes}")
    return new_nodes


def split_text(text, delimiter, text_type):
    splitted = text.split(delimiter)
    new_nodes = []

    for i, item in enumerate(splitted):
        is_text = i % 2 == 0

        new_node = None
        if is_text:
            new_node = TextNode(item, TEXT_TYPE.TEXT, None)
        else:
            new_node = TextNode(item, text_type, None)

        new_nodes.append(new_node)
    return new_nodes




