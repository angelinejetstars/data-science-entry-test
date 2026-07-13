class Car:

    # define a class named Car with attributes: make, model, year

    # initialise the attributes in the __init_ method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # add a method named describe_car() that prints out the car's details
    def describe_car(self):
        print(f"This car is a {self.year} {self.make} {self.model}.")


# create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# call describe_car method
my_car.describe_car()
