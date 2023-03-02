class Animal:
    def __init__(self, number_of_legs, number_of_eyes):
        self.number_of_legs = number_of_legs
        self.number_of_eyes = number_of_eyes

    def breathe(self):
        print("Inhale and exhale...")

    def walk(self):
        print("Animal walks using its legs.")

    def summary(self):
        print(
            f"This animal has {self.number_of_legs} legs and {self.number_of_eyes} eyes.")


class Dog(Animal):
    def __init__(self, number_of_legs, number_of_eyes, can_bark, can_bite):
        super().__init__(number_of_legs, number_of_eyes)
        self.can_bark

    def breathe(self):
        print("Dogs love to breathe with their mouths open.")

    def walk(self):
        print("Dogs love to run.")

    def summary(self):
        print(
            f"This animal has {self.number_of_legs} legs and {self.number_of_eyes} eyes.")
