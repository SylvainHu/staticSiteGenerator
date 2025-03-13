import os
import shutil

from blocks import markdown_to_html_node

def copy_from_static_to_public(src, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    files = os.listdir(src)

    for file in files:
        src_path = os.path.join(src, file)
        dest_path = os.path.join(destination, file)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copying {src_path} to {dest_path}")
        else:
            copy_from_static_to_public(src_path, dest_path)
            
def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith('# '):
            return line.split('# ', 1)[1].strip()
    raise Exception("No h1 headers")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as from_file:
        markdown = from_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    html_node = markdown_to_html_node(markdown)
    content = html_node.to_html()

    title = extract_title(markdown)

    new = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    new = new.replace('href="/', f'href="{basepath}')
    new = new.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as dest_file:
        dest_file.write(new)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    entries = os.listdir(dir_path_content)

    for entry in entries:
        path = os.path.join(dir_path_content, entry)

        if os.path.isfile(path):
            if entry.endswith('.md'):
                rel_path = os.path.relpath(path, dir_path_content)
                rel_path_html = rel_path.replace('.md', '.html')
                dest_path = os.path.join(dest_dir_path, rel_path_html)

                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                generate_page(path, template_path, dest_path, basepath)

        else:
            subdir_path = os.path.join(dest_dir_path, entry)
            os.makedirs(subdir_path, exist_ok=True)
            generate_pages_recursive(path, template_path, subdir_path, basepath)