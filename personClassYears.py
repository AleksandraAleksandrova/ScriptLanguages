import datetime

class Person:
    def __init__(self,name,year,month,date):
        self.name = name
        self.year = year
        self.month = month
        self.date = date
    def years(self):
        day = datetime.date.today().day
        month = datetime.date.today().month
        year = datetime.date.today().year
        if day < self.date and month <= self.month \
           or day > self.date and month < self.month:
            years = year - self.year - 1
        else:
            years = year - self.year
        return years


p1 = Person("Goshko",2002,4,8)
p2 = Person("Peshko",2001,3,20)
p3 = Person("Ivancho",2008,8,14)
res1=p1.years()
print(res1)
res2=p2.years()
print(res2)
res3=p3.years()
print(res3)
