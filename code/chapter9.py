class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        return f"Our {self.name} restaurant with {self.cuisine_type} food welcome!"

    @staticmethod
    def open_restaurant():
        return f"Our restaurant is opening!"

    def read_number_served(self):
        return f"There was {self.number_served} served in restaurant"

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    def __init__(self, name: str, cuisine_type: str, flavor: list):
        super().__init__(name, cuisine_type)
        self.flavor = flavor

    def display_flavor(self):
        return f"We have {', '.join(self.flavor)} ice cream"


ice_cream_1 = IceCreamStand("Mini Stop", "Fast food", ["strawberry", "chocolate", "vani"])
print(ice_cream_1.display_flavor())


class Users:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.login_attempts = 0

    def describe_users(self):
        return f"Last name of user is: {self.last_name!r} and first name is {self.first_name!r}"

    def greet_user(self):
        return f"Welcome Mrs/Miss: {self.last_name} {self.first_name}!!"

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(Users):
    def __init__(self, first, last, privileges):
        super().__init__(first, last)
        self.privileges = Privileges(privileges)


class Privileges:
    def __init__(self, privileges: list):
        self.privileges = privileges

    def show_privileges(self):
        return f"Your privileges is: {', '.join(self.privileges)}"


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWH battery.")

    def get_range(self):
        if self.battery_size == 75:
            _range = 260
        elif self.battery_size == 100:
            _range = 315

        print(f"This car can go about {_range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size <= 100:
            self.battery_size = 100


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_restaurant_1 = Restaurant("Beauty Beast", "Vietnamese")
my_restaurant_2 = Restaurant("Blink Planet", "Chinese")
my_restaurant_3 = Restaurant("Black Pearl", "Eastern")


user_1 = Users("Tuan", "Trinh Nguyen")
user_2 = Users("Kien", "Pham Quoc")
"""
print(user_1.describe_users())
print(user_2.greet_user())

my_restaurant_1.set_number_served(4)
print(my_restaurant_1.read_number_served())
my_restaurant_1.increment_number_served(10)
print(my_restaurant_1.read_number_served())
"""
admin_1 = Admin("Kean", "jason", ['can delete post', 'can add post'])
# print(admin_1.privileges.show_privileges())

# my_tesla = ElectricCar('telsa', 'model S', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()
