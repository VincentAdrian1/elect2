class Fruit:

    def __init__(self):
        self.name = input("Enter the fruit's name:")
        self.color = input("Enter the fruit's color:")
        self.taste = input("Enter the fruit's taste:")

    def describe(self):

        return (f"This is {self.name}, its color is {self.color}, and it taste {self.taste}. ")

fruit1 = Fruit()
fruit2 = Fruit()

print(fruit1.describe())
print(fruit2.describe())