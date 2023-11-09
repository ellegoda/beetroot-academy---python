class Person:
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.first_name} {self.last_name} and I am {self.age} years old.")

    def set_name(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


person_carl_johnson = Person("Carl","johnson",26)
person_carl_johnson.talk()
