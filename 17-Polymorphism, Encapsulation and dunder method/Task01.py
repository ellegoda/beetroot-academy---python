class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("Woof woof")


class Cat(Animal):
    def talk(self):
        print("Meow")


def perform_talk(animal_instance):
    animal_instance.talk()


dog_instance = Dog()
cat_instance = Cat()

perform_talk(dog_instance)
perform_talk(cat_instance)
