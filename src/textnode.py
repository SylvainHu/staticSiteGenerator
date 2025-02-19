from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        if self.text == node.text and self.text_type == node.text_type and self.url == node.url:
            return True
        
        return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        result = LeafNode(None, text_node.text)
        return result
    
    elif text_node.text_type == TextType.BOLD:
        result = LeafNode('b', text_node.text)
        return result
    
    elif text_node.text_type == TextType.ITALIC:
        result = LeafNode('i', text_node.text)
        return result

    elif text_node.text_type == TextType.CODE:
        result = LeafNode('code', text_node.text)
        return result

    elif text_node.text_type == TextType.LINK:
        result = LeafNode('a', text_node.text, {"href":text_node.url})
        return result

    elif text_node.text_type == TextType.IMAGE:
        result = LeafNode('img', "", {"src":text_node.url, "alt":text_node.text})
        return result

    else:
        raise ValueError("Wrong text type")