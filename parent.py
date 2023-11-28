class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.relationship = self.label_relationship()
        self.saying = self.say()
    def say(self):
        return("Hello I am a " + self.relationship)
    def label_relationship(self):
        return "Parent"
    def display(self):
        print(self.name)
        print(self.age)
        print(self.say())