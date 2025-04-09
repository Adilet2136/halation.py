'===================полиморфизм==============='
# полиморфизм - принцп ООП в котором в разных класс называютя одинаково но реализация разная 
# (один интерефейс разных фуекионал)

class Dog:
    def voice(self):
        print('гав-гав')

class Cat:
    def voice(self):
        print('мяу-мяу')
class Dag:
    def voice(self):
        print('кря-кря')

objects = [Dog(), Cat() ,Dag() ,Cat()]
for obj in objects:
    obj.voice()