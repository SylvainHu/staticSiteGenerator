import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from functions import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_selfComparison(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://test.com")
        self.assertEqual(node, node)

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_defaultURL(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_explicitNoneURL(self):
        node = TextNode("A text node", TextType.BOLD, None)
        node2 = TextNode("A text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_differentURL(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://notest.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://test.com")
        self.assertNotEqual(node, node2)

    def test_differentText(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://test.com")
        node2 = TextNode("This is not a text node", TextType.BOLD, "https://test.com")
        self.assertNotEqual(node, node2)

    def test_emptyText(self):
        node = TextNode("", TextType.BOLD, "https://test.com")
        node2 = TextNode("This is not a text node", TextType.BOLD, "https://test.com")
        self.assertNotEqual(node, node2)
    
    def test_CaseText(self):
        node = TextNode("this is a text node", TextType.BOLD, "https://test.com")
        node2 = TextNode("This is not a text node", TextType.BOLD, "https://test.com")
        self.assertNotEqual(node, node2)

    def test_spaceText(self):
        node = TextNode(" This is a text node", TextType.BOLD, "https://test.com")
        node2 = TextNode("This is not a text node", TextType.BOLD, "https://test.com")
        self.assertNotEqual(node, node2)

    def test_differentType(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        # Test regular text
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello, world!")

        # Test bold text
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

        # Test link with URL
        text_node = TextNode("Click me", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props["href"], "https://example.com")

        # Test image
        text_node = TextNode("Alt text", TextType.IMAGE, "image.jpg")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "image.jpg")
        self.assertEqual(html_node.props["alt"], "Alt text")

    def test_split_nodes_delimiter(self):
        # Test 1: Basic split with code
        node = TextNode("This is `code` here", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(nodes) == 3
        assert nodes[0].text == "This is "
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[1].text == "code"
        assert nodes[1].text_type == TextType.CODE
        assert nodes[2].text == " here"
        assert nodes[2].text_type == TextType.TEXT
        
        
        # Test 2: Bold text split
        node = TextNode("Hello **world** today", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert len(nodes) == 3
        assert nodes[0].text == "Hello "
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[1].text == "world"
        assert nodes[1].text_type == TextType.BOLD
        assert nodes[2].text == " today"
        assert nodes[2].text_type == TextType.TEXT
        
        # Test 3: Multiple delimiters
        node = TextNode("Hello `code` and `more code` here", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(nodes) == 5
        assert nodes[0].text == "Hello "
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[1].text == "code"
        assert nodes[1].text_type == TextType.CODE
        assert nodes[2].text == " and "
        assert nodes[2].text_type == TextType.TEXT
        assert nodes[3].text == "more code"
        assert nodes[3].text_type == TextType.CODE
        assert nodes[4].text == " here"
        assert nodes[4].text_type == TextType.TEXT

        # Test 4: Invalid markdown (missing closing delimiter)
        node = TextNode("Hello `world", TextType.TEXT)
        try:
            nodes = split_nodes_delimiter([node], "`", TextType.CODE)
            assert False, "Expected exception for invalid markdown"
        except Exception:
            assert True
        
        # Test 5: Node that's already special type (shouldn't split)
        node = TextNode("Already `special`", TextType.BOLD)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(nodes) == 1
        assert nodes[0].text == "Already `special`"
        assert nodes[0].text_type == TextType.BOLD
        
    def test_extract(self):
        # Images
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
        
        # Links
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

if __name__ == "__main__":
    unittest.main()