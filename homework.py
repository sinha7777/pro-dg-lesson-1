
class Dog():
    def __init__(self, name, breed, age, color, fav_food):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def bark(self):
        print("Woof! Woof!")

    def showdetails(self):
        print("Dog Details:")
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Age:", self.age)
        print("Color:", self.color)
        print("Favorite Food:", self.fav_food)

    def eat(self):
        print(self.name, "is happily eating", self.fav_food)

dog1 = Dog("Buddy", "Golden Retriever", 3, "Golden", "Chicken")
dog2 = Dog("Rocky", "German Shepherd", 5, "Brown", "Beef")

# Calling functions
dog1.showdetails()
dog1.bark()
dog1.eat()

print()

dog2.showdetails()
dog2.bark()
dog2.eat()
