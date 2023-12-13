class Human:
    def __init__(self, name="Human"):
        self.name = name

class Animal:
    def __init__(self, name="Animal"):
        self.name = name

class Model:
    def __init__(self, name="Model"):
        self.name = name

class Auto1:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
        self.animals = []
        self.models = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_animal_names(self):
        if self.animals:
            print(f"Animals in {self.brand}:")
            for animal in self.animals:
                print(animal.name)
        else:
            print(f"There are no animals in {self.brand}")

    def add_model(self, model):
        self.models.append(model)

    def print_model_names(self):
        if self.models:
            print(f"Models in {self.brand}:")
            for model in self.models:
                print(model.name)
        else:
            print(f"There are no models in {self.brand}")

class Auto2:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
        self.animals = []
        self.models = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_animal_names(self):
        if self.animals:
            print(f"Animals in {self.brand}:")
            for animal in self.animals:
                print(animal.name)
        else:
            print(f"There are no animals in {self.brand}")

    def add_model(self, model):
        self.models.append(model)

    def print_model_names(self):
        if self.models:
            print(f"Models in {self.brand}:")
            for model in self.models:
                print(model.name)
        else:
            print(f"There are no models in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
anton = Human("Anton")
marco = Human("Marco")

MercedesIQS = Model("MercedesIQS")
bmw530d = Model("BMW530d")

dog = Animal("dog")
cat = Animal("cat")

car1 = Auto1("BMW")
car2 = Auto2("Mercedes-Benz")

car1.add_animal(dog)
car1.add_passenger(nick)
car1.add_passenger(kate)
car2.add_passenger(anton)
car2.add_passenger(marco)
car2.add_animal(cat)
car1.add_model(MercedesIQS)
car2.add_model(bmw530d)

car1.print_passengers_names()
car2.print_passengers_names()
car1.print_animal_names()
car2.print_animal_names()
car1.print_model_names()
car2.print_model_names()
