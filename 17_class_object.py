class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def __str__(self):  # asString()
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.age = 40
# del p1.age  # you can delete an attribute
print(p1)
p1.myfunc()
