#!/usr/bin/python3
"""
creating a class call base
"""
import json
import csv

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"

        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dicts = []

        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""

        filename = cls.__name__ + ".json"

        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                list_dicts = cls.from_json_string(file.read())
                return \
                    [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def _to_csv(rectangle):
        """Return the CSV string representation of rectangle."""
        if isinstance(rectangle, Rectangle):
            return "{},{},{},{},{}".format(rectangle.id, rectangle.width,
                                           rectangle.height, rectangle.x,
                                           rectangle.y)
        elif isinstance(rectangle, Square):
            return "{},{},{},{}".format(rectangle.id, rectangle.size,
                                         rectangle.x, rectangle.y)

    @staticmethod
    def _from_csv(row):
        """Return a Rectangle or Square instance from a CSV row."""
        fields = row.split(",")
        if len(fields) == 5:
            # Rectangle: <id>,<width>,<height>,<x>,<y>
            return Rectangle(int(fields[0]), int(fields[1]), int(fields[2]),
                              int(fields[3]), int(fields[4]))
        elif len(fields) == 4:
            # Square: <id>,<size>,<x>,<y>
            return Square(int(fields[0]), int(fields[1]), int(fields[2]),
                           int(fields[3]))
        else:
            raise ValueError("Invalid CSV row: {}".format(row))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + '.csv'
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    writer.writerow\
                        ([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == 'Square':
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances from a CSV file."""
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                instances = []
                for row in reader:
                    data = {field: int(value) for field, value in zip(fields, row)}
                    instance = cls.create(**data)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
