import re
from classes.textnode import TEXT_TYPE, TextNode
from utils.extract_markdown_images import extract_markdown_images
from utils.extract_markdown_links import extract_markdown_links


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

    return new_nodes
