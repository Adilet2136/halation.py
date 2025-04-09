'=============================OOP============================='
# OOP - Object_orentated programig 
# OOP - объектно оринтированное програмированиие (парадигма)

# class - это шаблон
# object(instance , экземпляр) - это конечный продукт класса


class Person:
    # переменые внутри класса (объекта )- аттрибуты
    arms = 2 
    legs = 2
    
    def __init__(self, name, age, prof):
        # __init__ - ьетод который будет добавлять в обьект те атрибуты, которые у всех  обьектов разные
        # self - это ссылка на обьект кторый только что создался 
        self.name = name 
        self.age = age 
        self.prof = prof
    # функций внутри класса (объекта ) - методы
    def walk(self):
        print(f'{self.name} ходить')
    def swim(self):
        print(f'{self.name}плавать')

obj1 = Person('katana', 21, 'dev')
obj2 = Person('nick', 21 ,  'dev')
obj3 = Person('laura', 20 ,'senior dev')

 
obj1.walk()
obj1.swim()
obj2.swim()
print(obj1.name)
print(obj1.arms)
print(obj3.name)
print(obj2.age)



print(obj2.legs)



class Calc:
    def add(self, a, b):
        return a + b
    def dif(self, a , b):
        return a - b 
    def div(self,a , b):
        return a / b
    def mult(self, a , b):
        return a * b
    
calc = Calc()
print(calc.add(4,5))
print(calc.dif(10,5))
print(calc.div(4,5))
print(calc.mult(10,5))


