#?/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

rectangle = Rectangle(2,4)
print("Area: {} - Perimeter: {}".format(rectangle.area(), rectangle.perimeter()))

rectangle = Rectangle(3,10)
print("Area: {} - Perimeter: {}".format(rectangle.area(), rectangle.perimeter()))
