class Country:
    def __init__(self, continent, country_name):
        self.continent = continent
        self.country_name = country_name
    def __str__(self):
        return f"{self.continent}, {self.country_name}"
class City(Country):
    def __init__(self, continent, country_name, city_name):
        super().__init__(continent, country_name)
        self.city_name = city_name
    def __str__(self):
        return f"{self.continent}, {self.country_name}, {self.city_name}"
class Building(City):
    def __init__(self, continent, country_name, city_name, street, number_of_building, entrance, floor, apartment_number):
        super().__init__(continent, country_name, city_name)
        self.street = street
        self.number_of_building = number_of_building
        self.entrance = entrance
        self.floor = floor
        self.apartment_number = apartment_number
    def __str__(self):
        return f"{self.continent}, {self.country_name}, {self.city_name}, street {self.street}, building {self.number_of_building}, entrance {self.entrance}, floor {self.floor}, aparment {self.apartment_number}"

class Person(Building):
    def __init__(self, continent, country_name, city_name, street, number_of_building, entrance, floor, apartment_number, firstname, lastname, age):
        super().__init__(continent, country_name, city_name, street, number_of_building, entrance, floor, apartment_number)
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def __str__(self):
        return f"Im living in {self.continent}. In country named {self.country_name}. In bueatiful city {self.city_name}. My addess is {self.street} street, building number {self.number_of_building}, entance {self.entrance}, floor {self.floor}, apartment {self.apartment_number}. My name is {self.firstname} {self.lastname}, and im {self.age}."


x1 = Country("Europe", "Ukraine")
x2 = City("Europe", "Ukraine", "Kiyv")
x3 = Building("Europe", "Ukraine", "Kiyv", "Urlivska", 17, 2, 3, 146)
x4 = Person("Europe", "Ukraine", "Kiyv", "Urlivska", 17, 2, 3, 146, "Marko", "Makovyak", 32)
print(x1)
print(x2)
print(x3)
print(x4)

continent = input("Type continent, where you live: ")
country = input("Type country, where you live: ")
city = input("Type city, where you live: ")
street = input("Type street, where you live: ")
building = input("Type number of building, where you live: ")
entrance = input("Type number of your entrance in your building: ")
floor = input("Type floor where you live: ")
apartment = input("Type the number of your aparment: ")
firstname = input("Type your firstname: ")
lastname = input("Type your lastname: ")
age = input("Type your age: ")
livingin = Person(continent,country,city,street,building,entrance,floor,apartment,firstname,lastname,age)
print(livingin)