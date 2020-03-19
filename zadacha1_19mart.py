class Person:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def __add__(self, other_obj):
        p3 = Person("Ivancho", self.age + other_obj.age)
        return p3

p1 = Person("Goshko", 15)
p2 = Person("Peshko", 13)
