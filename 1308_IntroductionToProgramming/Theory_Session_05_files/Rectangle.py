from Shape import Shape

class Rectangle(Shape):
    
    def __init__(self, width=10, height=5, first_color="white", second_color="white"):
        super().__init__()
        self.width = width
        self.height = height
        self.first_color = first_color
        self.second_color = second_color
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def setWidth(self, new_width):
        if(new_width == self.height):
            print("The new width cannot be equal to height")
        else:
            self.width = new_width
    
    def setHeight(self, new_height):
        self.height = new_height
    
    def area(self):
        return self.height*self.width
    
    def __str__(self):
        return "This is a rectangle with color " + self.getColor() + " and area " + str(self.area())
    
    def setColor(self, color1="white", color2="white"):
        self.first_color = color1
        self.second_color = color2
    
    def getColor(self):
        return self.first_color+" and "+self.second_color
        

