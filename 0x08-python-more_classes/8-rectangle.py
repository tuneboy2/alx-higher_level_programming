#!/usr/bin/python3
""" Defines a class for a Rectangle """


class Rectangle:
    """ defines the representation for a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializes the parameters passed"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ returns the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width of a rectangle

        Args:
          value (int): the width to be set

        Raises:
            TypeError - if the value is not of type int
            ValueError - if the value is less than zero
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ rerurns the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height of the rectangle

        Args:
          value (int): the height to be set
          """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ returns the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ Returns the printable representation of an object

           Represents a rectangle with the '#' character"""
        if self.__height == 0 or self.__width == 0:
            return ""

        rect = []
        for no in range(self.__height):
            for num in range(self.width):
                rect.append(str(self.print_symbol))
            if no != self.__height - 1:
                rect.append("\n")

        return "".join(rect)

    def __repr__(self):
        """ returns the string representation of the object code """
        rt = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return rt

    def __del__(self):
        """ deletes an instance of the rectangle class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 0

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        """returns the rectangle with the bigger area"""
        if type(rect1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect1.area() >= rect2.area():
            return rect1
        else:
            return rect2
