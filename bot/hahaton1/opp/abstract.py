'===============Абстракция=============='
# Абстракция - это принцип ооп, в которм мы создаем класс пустышку, где задаем название аттрибутов и 
# методотов, для того чтобы в дочерных классах не забыть их преопредилить



from abc import ABC, abstractmethod,abstractproperty

class AbstractAnimal(ABC):
    @property
    @abstractmethod
    def legs(self):
        ...
    @abstractmethod
    def voice(self):
        ...

class Dog(AbstractAnimal):
    ...

obj1 = Dog() # ошибка потому что нужно преопредилять в классе dog метод voice и аттрибут legs


class Dog(AbstractAnimal):
    def voice(self):
        print('гав-гав')