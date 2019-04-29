from Shape import Shape
from Rectangle import Rectangle

#a = Shape()
#print(a.getColor())

#a.setColor("Green")
#print(a.getColor())

r = Rectangle()
r.setColor("Blue")
print(r.getColor())

r.setWidth(5)
print(r.getWidth())

print("Area:", r.area())

#print("This is a rectangle with color",r.getColor(),"and area",r.area())
print(r)