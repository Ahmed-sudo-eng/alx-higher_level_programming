#!/usr/bin/python3
"""
This module contains an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """An empty class Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the attributes"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Calculate and return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """print the rectangle with '#'"""
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            for h in range(self.__height):
                for w in range(self.__width):
                    print('#', end='')
                if h < (self.__height - 1):
                    print()
                else:
                    pass
            return ' '

    def __repr__(self):
        """Return a string representation of the rectangle"""
        w = str(self.__width)
        h = str(self.__height)
        return "Rectangle(" + w + ", " + h + ")"

    def __del__(self):
        """Deleting a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
