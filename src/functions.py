from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.TEXT:
            sentence = old_node.text.split(delimiter)
            if len(sentence) % 2 == 0:
                raise Exception("Invalid Markdown syntax")
            for index, text in enumerate(sentence):
                if index % 2 == 0:
                    nodes.append(TextNode(text, TextType.TEXT))
                else:
                    nodes.append(TextNode(text, text_type))

        else:
            nodes.append(old_node)

    return nodes


def split_nodes_image(old_nodes):
    nodes = []
    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        if not images:
            nodes.append(old_node)
            continue
        
        current_text = old_node.text

        for img_text, img_url in images:
            markdown_link = f"![{img_text}]({img_url})"
            pos = current_text.find(markdown_link)

            if pos == -1:
                continue

            before = current_text[:pos]
            if before:
                nodes.append(TextNode(before, TextType.TEXT))

            nodes.append(TextNode(img_text, TextType.IMAGE, img_url))

            current_text = current_text[pos + len(markdown_link):]
        
        if current_text:
            nodes.append(TextNode(current_text, TextType.TEXT))

    return nodes
        


def split_nodes_link(old_nodes):
    nodes = []
    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        if not links:
            nodes.append(old_node)
            continue
        
        current_text = old_node.text

        for link_text, link_url in links:
            markdown_link = f"[{link_text}]({link_url})"
            pos = current_text.find(markdown_link)

            if pos == -1:
                continue

            before = current_text[:pos]
            if before:
                nodes.append(TextNode(before, TextType.TEXT))

            nodes.append(TextNode(link_text, TextType.LINK, link_url))

            current_text = current_text[pos + len(markdown_link):]
        
        if current_text:
            nodes.append(TextNode(current_text, TextType.TEXT))

    return nodes
        


def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes