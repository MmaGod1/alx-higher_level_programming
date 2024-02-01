#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Defines a rectangle with width and height attributes."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            """Retrieve the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            """Set the height of the rectangle."""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            """Calculate the area of the rectangle."""
            return self.width * self.height

        def perimeter(self):
            """Calculate the perimeter of the rectangle."""
            if self.width == 0 or self.height == 0:
                return 0
            return 2 * (self.width + self.height)

        def __str__(self):
            """Return a string representation of the rectangle using #."""
            if self.width == 0 or self.height == 0:
                return ""
            rectangle_str = ""
            for _ in range(self.height):
                rectangle_str += "#" * self.width + "\n"
                return rectangle_str[:-1]

        def __repr__(self):
            """Return a string representation of the rectangle."""
            return f"Rectangle({self.width}, {self.height})"

        def __del__(self):
            """Print a message when an instance of Rectangle is deleted..."""
            Rectangle.number_of_instances -= 1
            print("Bye rectangle...")
