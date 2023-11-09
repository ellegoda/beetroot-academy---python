class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):

        equivalent_age = self.dog_age * Dog.age_factor
        return equivalent_age


dog_age = Dog(1)
print(f"The dog's age in human equivalent is: {dog_age.human_age()} years")