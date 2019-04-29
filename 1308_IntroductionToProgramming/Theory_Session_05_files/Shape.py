from abc import ABC, abstractmethod

class Shape(ABC):
    
    def __init__(self, class_color="White"):
        self.color = class_color
    
    def getColor(self):
        return self.color
    
    def setColor(self, new_color):
        self.color = new_color
    
    @abstractmethod
    def area(self):
        pass
