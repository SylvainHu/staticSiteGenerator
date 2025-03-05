import unittest

from blocks import markdown_to_blocks, block_to_block_type, BlockType


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


    def test_paragraph(self):
        markdown = "This is a regular paragraph."
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)
        
        # Edge case: empty string should be a paragraph
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)
    
    def test_heading(self):
        # Test heading levels 1-6
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Heading 4"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Heading 5"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        
        # Invalid headings (no space or too many #)
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("####### Too Many"), BlockType.PARAGRAPH)
    
    def test_code(self):
        self.assertEqual(block_to_block_type("```\ncode block\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```\n```"), BlockType.CODE)
        
        # Invalid code block (missing closing backticks)
        self.assertEqual(block_to_block_type("```\nunclosed code"), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()