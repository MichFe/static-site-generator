import re


def extract_markdown_links(text):
    anchors = re.findall(r"\[(.*?)\]\(", text)
    urls = re.findall(r"\[.*?\]\((.*?)\)", text)
    zipped = zip(anchors, urls)
    return list(zipped)

