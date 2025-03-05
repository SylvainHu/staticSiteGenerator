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
    if not markdown:
        return BlockType.PARAGRAPH

    if markdown[0] == "#":
        heading_level = 0
        for char in markdown:
            if char == '#':
                heading_level += 1
            else:
                break
        if heading_level <= 6 and heading_level > 0 and markdown[heading_level] == " ":
            return BlockType.HEADING
    
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    
    lines = markdown.split("\n")

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    elif all(line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST

    else:
        return BlockType.PARAGRAPH