'================Принципы ООП=============='
# Наследование
# Инкапсуляция
# Полиморфизм 
# Абстракция
# Ассоциация (Агрегация, Композиция)


'==============Наследование==============='
# Наследование - принцип ООП, в котором мы можем унаследовать, переопределить и использовать в дочернем классе все аттрибуты и методы родительского класса

class A:
    var = 'a'
    def method(self):
        print('метод в классе А')
    
obj_a = A()
obj_a.method() # метод в классе А

class B(A):
    var = 'b'

obj_b = B()
obj_b.method()

class C(A):
    var = 'c'
    def method(self):
        print('метод в классе С')

obj_c = C()
obj_c.method()
print(obj_c.var)



class Animal:
    price = 100000

    def voice(self):
        return 'Звуки животных'


class Dog(Animal):
    def voice(self):
        return 'Гав-гав'

class Cat(Animal):
    def voice(self):
        return 'Мяу'

class Duck(Animal):
    def voice(self):
        return 'Кря-кря'


Bobik = Dog()
Barsik = Cat()
Donald = Duck()

print(f'Бобик стоит - {Bobik.price} сом, он умеет {Bobik.voice()}')

print(f'Барсик стоит - {Barsik.price} сом, он умеет {Barsik.voice()}')

print(f'Дональд стоит - {Donald.price} сом, он умеет {Donald.voice()}')


Marusa = Cat()
print(Marusa.price)


# одиночное наследование (1 род - 1 дочь)
class A:
    ...

class B(A):
    ...

'------------------------------'
#иерархическое наследование (1 род - много дочь)
class A:
    ...

class B(A):
    ...

class C(A):
    ...

class D(A):
    ...

'---------------------------------'
# множественное наследование (много род - 1 дочь)
class A:
    ...

class B:
    ...

class C(A, B):
    ...

'-----------------------------'
# многоуровневое наследование - (цепочкой, род->доч/род->доч/род->доч)
class A:
    ...

class B(A):
    ...

class C(B):
    ...

class D(C):
    ...


'----------------------------'
# гибридное наследование - (смесь видов наследования)
class A:
    ...
class B(A):
    ...
class C(A):
    ...
class E:
    ...
class D(C, E):
    ...



class A:
    attr = 12

    
class B(A):
    def func(self):
        return super().attr ** 2
    

obj = B()
print(obj.func())
__dict__ 

object
