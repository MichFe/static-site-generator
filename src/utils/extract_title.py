import re

def extract_title(markdown):
    titles = re.findall(r"^\s*#\s[^#].*$", markdown, re.MULTILINE)

    if len(titles) == 0:
        raise ValueError("No title found in the markdown")

    title = titles[0]
    title_text = title.split('# ')[1].strip()
    return title_text
