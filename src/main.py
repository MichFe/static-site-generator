import os, shutil
from classes.textnode import TEXT_TYPE, TextNode
from utils.extract_title import extract_title
from utils.markdown_to_html_node import markdown_to_html_node

def main():
    shutil.rmtree('./public')
    os.mkdir('./public')
    copy_static('static', 'public')

    generate_page("content/index.md", "template.html", "public/index.html")

def copy_static(origin, destination):
    print(f"origin: {origin}, destination: {destination}")
    static_files = os.listdir(origin)

    for path in static_files:
        src_path = f"{origin}/{path}"
        out_path= f"{destination}/{path}"

        is_file = os.path.isfile(src_path)
        print(f"{src_path} is file? {is_file}")

        if is_file:
            shutil.copy(src_path, out_path)
            continue

        os.mkdir(out_path)
        copy_static(src_path, out_path)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    raise NotImplementedError('Generate page recursive is not implemented yet')

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = open(from_path, 'r', encoding='utf-8')
    md_content = md_file.read()
    md_file.close()

    template_file = open(template_path, 'r', encoding='utf-8')
    template_content = template_file.read()

    html_content = markdown_to_html_node(md_content).to_html()

    page_title = extract_title(md_content)

    template_content = template_content.replace("{{ Title }}", page_title)
    template_content = template_content.replace("{{ Content }}", html_content)


    html_file = open(dest_path, 'w', encoding='utf-8')
    html_file.write(template_content)
    html_file.close()


if __name__ == "__main__":
    main()
