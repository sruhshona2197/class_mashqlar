# 1
class Student:
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def introduce(self):
        print(f"mening ismmim {self.name}, yshm {self.age}")

s1 = Student("Ali", 20)
s1.introduce()

# 2
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print(f"model =   {self.model}, color = {self.color}")
c1 = Car("Cobalt",  "oq")
c1.info()


# 3
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_price(self):
        print(f"brend =   {self.brand}, narx = {self.price}")
x1 = Phone("iPhone ",  "1200$")
x1.show_price()



