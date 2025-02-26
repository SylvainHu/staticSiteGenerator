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


def split_nodes_link(old_nodes):
    nodes = []
    for old_node in old_nodes:
        extract = extract_markdown_links(old_node.text)
        if not extract:
            nodes.append(old_nodes)
            return nodes
        


def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


