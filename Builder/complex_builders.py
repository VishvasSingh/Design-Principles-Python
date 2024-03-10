"""
    How to use several builders to build one object
"""


class Person:
    def __init__(self):
        # address info
        self.address = None
        self.city = None
        self.pin_code = None
        # employment info
        self.company_name = None
        self.position = None
        self.salary = None

    def __str__(self):
        return (f'Person: lives at {self.address} in {self.city} with pin code as {self.pin_code}'
                f'he/she works at {self.company_name} as {self.position} getting a salary of {self.salary}')


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def lives_at(self, address):
        self.person.address = address
        return self

    def add_city(self, city):
        self.person.city = city
        return self

    def add_pin_code(self, pin_code):
        self.person.pin_code = pin_code
        return self


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def works_at(self, company):
        self.person.company_name = company
        return self

    def set_position(self, position):
        self.person.position = position
        return self

    def set_salary(self, salary):
        self.person.salary = salary
        return self


pb = PersonBuilder()
person = ((pb
          .works
          .works_at('Apple')
          .set_position('SDE 2')
          .set_salary(225000)
          .lives
          .lives_at('Some resort')
          .add_city('GOA')
          .add_pin_code('120551'))
          .build())

print(person)
