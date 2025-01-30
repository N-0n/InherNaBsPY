from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class human(Animal):
    def move(self):
        print("I can walk and run 👶")

class snake(Animal):
     def move(self):
        print("I can crawl 🤷‍♂️")

class crow(Animal):
     def move(self):
        print("I can fly betch 🤴🐦‍⬛")

o1=human()
o1.move()

o2=snake()
o2.move()

o3=crow()
o3.move()

