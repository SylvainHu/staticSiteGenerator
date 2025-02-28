import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

if __name__ == "__main__":
    unittest.main()