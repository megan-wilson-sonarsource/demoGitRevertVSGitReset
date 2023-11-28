from parent import Parent

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)
    def label_relationship(self):
        return "Child"