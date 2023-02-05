from abc import ABC, abstractclassmethod, abstractmethod

class Animal(ABC):
    @property
    def food_eaten(self):
        return self._food

    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"You can't feed this animal with {food}")
    
    @property
    @abstractmethod
    def diet(self):
        pass
    
    @abstractmethod
    def feed(self, time):
        pass

class Lion(Animal):
    @property
    def diet(self):
        return ["antelope", "cheetah", "buffaloe"]

    def feed(self, time):
        print(f"Feeding a lion with {self._food} meat! At {time}")

    
class Snake(Animal):
    @property                 
    def diet(self):     
        return ["frog", "rabbit"]

    def feed(self, time): 
        print(f"Feeding a snake with {self._food} meat! At {time}") 

if __name__ == '__main__':
    leo = Lion()
    leo.food_eaten = "buffaloe" 
    leo.feed("10:10 AM")
    
    adam = Snake()
    adam.food_eaten = "frog"
    adam.feed("10:20 AM")

    bob = Lion()
    bob.food_eaten = "carrot"
    bob.feed("20:10 Uhr")

    
