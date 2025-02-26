import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_onlyValue(self):
        node = LeafNode(None, "Hello word")
        self.assertEqual(node.to_html(), "Hello word")

    def test_tagAndValue(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), '<p>This is a paragraph</p>')

    def test_all(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "class": "link"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" class="link">Click me!</a>')

    def test_noValue(self):
        with self.assertRaises(ValueError):
            node = LeafNode(None, None)
            node.to_html()

if __name__ == "__main__":
    unittest.main()