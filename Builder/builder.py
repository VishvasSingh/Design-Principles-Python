
"""
    Builders are useful when we have complicated construction of objects
    Eg - Construction of HTML elements
"""


class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent: int) -> str:
        """
            Helper function to print the HTML elements recursively since each HTML element might have children
            of its own and this helper will take care of printing them in correct indentation and format
        :param indent: number for indentation required between parent and child elements
        :return: HTML string of indented elements
        """
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent+1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent+1))

        lines.append(f'{i}</{self.name}>')

        return '\n'.join(lines)

    def __str__(self):
        return self.__str(indent=0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def add_nested_child_fluent(self, child_name, child_text):
        self.__root.elements[-1].elements.append(HtmlElement(child_name, child_text))
        return self

    def __str__(self):
        return str(self.__root)


builder = HtmlElement.create('ul')
# builder.add_child('li', 'hello')
# builder.add_child('li', 'how are you ?)

(builder
 .add_child_fluent('li', 'hello')
 .add_nested_child_fluent('p', 'paragraph inside list')
 .add_nested_child_fluent('p', 'second paragraph')
 .add_child_fluent('li', 'how are you?'))

print(builder)
