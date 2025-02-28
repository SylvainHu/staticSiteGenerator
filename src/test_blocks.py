import unittest

from textnode import TextNode, TextType
from blocks import markdown_to_blocks


class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
            # This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
            """
        results = markdown_to_blocks(markdown)
        expected_results = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        ]
        self.assertEqual(results, expected_results)


if __name__ == "__main__":
    unittest.main()