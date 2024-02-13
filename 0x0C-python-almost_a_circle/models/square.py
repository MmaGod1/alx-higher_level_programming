#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override __str__ method to return formatted string."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
