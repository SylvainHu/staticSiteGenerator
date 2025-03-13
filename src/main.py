import os
import sys
import shutil
from textnode import TextNode, TextType
from website import copy_from_static_to_public, generate_pages_recursive

static_dir = "./static"
output_dir = "./docs"
content_dir = "./content"
template_path = "./template.html"

basepath = "/"
if len(sys.argv) > 1:
    basepath = sys.argv[1]


def main():

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    copy_from_static_to_public(static_dir, output_dir)
    generate_pages_recursive(content_dir, template_path, output_dir, basepath)

if __name__ == '__main__':
    main()
