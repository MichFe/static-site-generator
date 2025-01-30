import re


def extract_markdown_images(text):
    alt_texts =  re.findall(r"!\[(.*?)\]", text)
    urls = re.findall(r"!\[.*?\]\((.*?)\)", text)
    zipped = zip(alt_texts, urls)
    return list(zipped)

