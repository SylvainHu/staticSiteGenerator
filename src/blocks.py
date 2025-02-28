from enum import Enum
from textnode import TextType, TextNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    results = [block.strip() for block in markdown.split("\n\n")]

    return results

def block_to_block_type(markdown):
    if markdown[0] == "#":
        return BlockType.HEADING
    
    elif markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    
    elif markdown[0] == ">":
        return BlockType.QUOTE
    elif markdown[:1] == "- ":
        return BlockType.UNORDERED_LIST
    elif markdown[0].isdigit() and markdown[1:3] == ". ":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH