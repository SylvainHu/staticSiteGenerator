from textnode import TextNode, TextType

def main():
    text = TextNode("This is a text node", TextType.bold, "https://www.boot.dev")
    print(text)

if __name__ == '__main__':
    main()
