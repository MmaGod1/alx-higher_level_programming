#!/usr/bin/python3
"""Module for Base class."""
import json
import csv
import turtle


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Return list of dictionaries from JSON string representation."""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create instance with attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Dummy Square instance

        dummy_instance.update(**dictionary)  # Update attributes using dictionary
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return list of instances from file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                data = file.read()
                dictionaries = cls.from_json_string(data)
                return [cls.create(**dictionary) for dictionary in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from CSV file."""
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                elif cls.__name__ == "Square":
                    instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                instances.append(instance)
        return instances

     @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all the Rectangles and Squares."""
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.title("Drawing Rectangles and Squares")

        # Draw Rectangles
        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.color("blue")  # Example color
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.right(90)
                turtle.forward(rectangle.height)
                turtle.right(90)
            turtle.end_fill()

        # Draw Squares
        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color("red")  # Example color
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.end_fill()

        turtle.done()
