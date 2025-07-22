import re
from classes.textnode import TEXT_TYPE, TextNode
from utils.extract_markdown_images import extract_markdown_images
from utils.extract_markdown_links import extract_markdown_links

def markdown_to_blocks(md):
    splitted = md.split("\n\n")
    whitespace_removed = list(map(lambda x: x.strip(), splitted))
    final = filter(lambda x: x, whitespace_removed)

    return list(final)

def text_to_textnodes(text):
    md_delimiters = {
        TEXT_TYPE.BOLD: "**",
        TEXT_TYPE.ITALIC: "_",
        TEXT_TYPE.CODE: "`",
    }

    nodes = [TextNode(text, TEXT_TYPE.TEXT)]

    for text_type, delimiter in md_delimiters.items():
        nodes = split_nodes_delimiter(nodes, delimiter, text_type)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TEXT_TYPE.TEXT:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        new_nodes += split_text(node_text, delimiter, text_type)

    return new_nodes


def split_text(text, delimiter, text_type):
    if not delimiter:
        raise ValueError("A delimiter is required")
    if delimiter not in text:
        return [TextNode(text, TEXT_TYPE.TEXT)]

    # The splitted array must be a multiple of 3, if not, the markdown is malformed
    splitted = text.split(delimiter)
    is_md_malformed = len(splitted) % 2 == 0 or len(splitted) < 3
    if is_md_malformed:
        raise ValueError(f"Markdown is malformed with text: {text} delimiter: {delimiter} text_type: {text_type}")

    new_nodes: list[TextNode] = []
    for i, item in enumerate(splitted):
        is_text = i % 2 == 0
        node_type = TEXT_TYPE.TEXT if is_text else text_type

        new_node = TextNode(item, node_type, None)
        new_nodes.append(new_node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TEXT_TYPE.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_nodes.append(node)
            continue

        for anchor, url in links:
            before_match, after_match = text.split(f"[{anchor}]({url})", 1)

            if before_match:
                new_nodes.append(TextNode(before_match, TEXT_TYPE.TEXT))

            new_nodes.append(TextNode(anchor, TEXT_TYPE.LINK, url))
            text = after_match

        if len(text) > 0:
            new_nodes.append(TextNode(text, TEXT_TYPE.TEXT))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TEXT_TYPE.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_nodes.append(node)
            continue

        for alt_text, url in images:
            before_match, after_match = text.split(f"![{alt_text}]({url})")

            if before_match:
                new_nodes.append(TextNode(before_match, TEXT_TYPE.TEXT))

            new_nodes.append(TextNode(alt_text, TEXT_TYPE.IMAGE, url))
            text = after_match

        if len(text) > 0:
            new_nodes.append(TextNode(text, TEXT_TYPE.TEXT))

    return new_nodes
