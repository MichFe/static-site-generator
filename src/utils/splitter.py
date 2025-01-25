from classes.textnode import TEXT_TYPE, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        node_text = old_node.text
        new_nodes += split_text(node_text, delimiter, text_type)

    return new_nodes


def split_text(text, delimiter, text_type):
    if not delimiter:
        raise ValueError("A delimiter is required")

    # The splitted array must be a multiple of 3, if not, the markdown is malformed
    splitted = text.split(delimiter)
    is_md_malformed = len(splitted) % 2 == 0 or len(splitted) < 3
    if is_md_malformed:
        raise ValueError("Markdown is malformed")

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




