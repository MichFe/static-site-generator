import re
from classes import leafnode, textnode
from classes.htmlnode import HtmlNode
from classes.parentnode import ParentNode
from utils.block_to_block_type import BLOCK_TYPES, block_to_block_type
from utils.splitter import markdown_to_blocks, text_to_textnodes



def markdown_to_html_node(markdown):
    splitted_blocks = markdown_to_blocks(markdown)

    html_nodes = []
    for block in splitted_blocks:
        block_type = block_to_block_type(block)
        html_node = create_html_node(block, block_type)
        html_nodes.append(html_node)

    parent_node = ParentNode("div", html_nodes)
    return parent_node

def create_html_node(markdown, type):
    htmlnode_constructor = {
        BLOCK_TYPES.HEADING: create_html_header,
        BLOCK_TYPES.PARAGRAPH: create_html_paragraph,
        BLOCK_TYPES.CODE: create_html_codeblock,
        BLOCK_TYPES.QUOTE: create_html_quote,
        BLOCK_TYPES.UNORDERED_LIST: create_html_unordered_list,
        BLOCK_TYPES.ORDERED_LIST: create_html_ordered_list,
    }

    return htmlnode_constructor[type](markdown)

# HTML block type creation methods
def create_html_ordered_list(markdown):
    list_items = re.split(r"\d+\.\s", markdown)
    not_empty_list_items = [item.strip() for item in list_items if item.strip()]
    li_items = list(map(lambda x: HtmlNode("li", x), not_empty_list_items))
    ol_element = ParentNode("ol", li_items)
    return ol_element

def create_html_unordered_list(markdown):
    list_items = markdown.split("- ")
    not_empty_list_items = list(filter(lambda x: x.strip(), list_items))
    li_items = list(map(lambda x: HtmlNode('li', x.strip()), not_empty_list_items))
    ul_element = ParentNode("ul",li_items)
    return ul_element

def create_html_header(markdown):
    heading_number = max(min(markdown.count('#'), 6), 1)
    tag = f"h{heading_number}"
    value = markdown[heading_number + 1:]
    html_node = HtmlNode(tag, value)

    return html_node

def create_html_paragraph(md):
    html_nodes = get_inline_nodes(md)

    inner_html = ""
    for leaf_node in html_nodes:
        inner_html += leaf_node.to_html()
    p_node = HtmlNode("p", inner_html)
    return p_node

def create_html_codeblock(md):
    tag = f"pre"
    value = md.strip("```").lstrip("\n")
    html_node = HtmlNode(tag, f"<code>{value}</code>")

    return html_node

def create_html_quote(md):
    tag = "blockquote"
    value = md.replace("> ", "").strip()
    html_node = HtmlNode(tag, value)

    return html_node

# Auxiliar inline text node handling
def get_inline_nodes(md):
    lines = md.split("\n")
    not_empty_lines = list(filter(lambda x: x, lines))
    clean_md_text = " ".join(not_empty_lines)

    text_nodes = text_to_textnodes(clean_md_text)
    html_nodes = list(map(lambda x: x.text_node_to_html_node(), text_nodes))
    return html_nodes

