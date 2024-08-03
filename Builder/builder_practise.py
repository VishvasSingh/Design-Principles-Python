class CodeBuilder:
    def __init__(self, root_name):
        self.__root_name = ClassBuilder(root_name)

    def add_field(self, type, name):
        self.__root_name.add_field(type, name)
        return self

    def __str__(self):
        return self.__root_name.__str__()


class ClassBuilder:
    def __init__(self, root_name):
        self.name = root_name
        self.attributes = []

    def add_field(self, type, name):
        self.attributes.append(Attribute(type, name))
        return self

    def __str__(self):
        lines = [f"class {self.name}:"]
        if not self.attributes:
            lines.append("  pass")

        else:
            lines.append("  def __init__(self):")
            for each_attr in self.attributes:
                lines.append(f"    {each_attr.__str__()}")

        return "\n".join(lines)


class Attribute:
    def __init__(self, type, value):
        self.name = type
        self.value = value

    def __str__(self):
        return f"self.{self.name} = {self.value}"


if __name__ == "__main__":
    cb = CodeBuilder("Greetings")
    cb.add_field("hello", "how_are_you?").add_field("i_am_good", "thanks")
    print(cb)
