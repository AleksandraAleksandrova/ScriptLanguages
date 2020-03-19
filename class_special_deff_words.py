class Person:
    def __init__(self,name,age):
        self.age = age
        self.name = name
        
    def __add__(self, other_obj):
        return self.name + other_obj.name

    def __str__(self):
        return "My name is {}" .format(self.name)

p1 = Person("Goshko", 15)
p2 = Person("Peshko", 14)
print(p2)
