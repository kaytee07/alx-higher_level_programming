import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):

    def test_id_assigned_explicitly(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_id_assigned_implicitly(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string_valid(self):
        r1 = Rectangle(10, 2, 0, 0)
        r2 = Rectangle(2, 3, 0, 0)
        s1 = Square(5, 1, 0)
        s2 = Square(7, 2, 1)
        dictionary_list = [r1.to_dictionary(), r2.to_dictionary(),
                           s1.to_dictionary(), s2.to_dictionary()]
        json_string = Base.to_json_string(dictionary_list)
        self.assertEqual(type(json_string), str)

    def test_to_json_string_empty(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        with open("Rectangle.json", "r") as file:
            json_string = file.read()
        expected = Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()])
        self.assertEqual(json_string, expected)

        s1 = Square(10, 2, 1)
        s2 = Square(2)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        with open("Square.json", "r") as file:
            json_string = file.read()
        expected = Base.to_json_string([s1.to_dictionary(), s2.to_dictionary()])
        self.assertEqual(json_string, expected)

        os.remove("Rectangle.json")
        os.remove("Square.json")

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            json_string = file.read()
        self.assertEqual(json_string, "[]")

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            json_string = file.read()
        self.assertEqual(json_string, "[]")

        os.remove("Rectangle.json")
        os.remove("Square.json")

    def test_from_json_string_valid(self):
        json_string = '[{"id": 1, "width": 10, "height": 20, "x": 1, "y": 2}, {"id": 2, "width": 5, "height": 15, "x": 3, "y": 4}]'
        expected = [{"id": 1, "width": 10, "height": 20, "x": 1, "y": 2}, {"id": 2, "width": 5, "height": 15, "x": 3, "y": 4}]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected)

    def test_from_json_string_empty(self):
        json_string = ''
        expected = []
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected)

    def test_from_json_string_none(self):
        json_string = None
        expected = []
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected)

    def test_create_rectangle(self):
        r_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 0, 'y': 0}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_create_square(self):
        s_dict = {'id': 2, 'size': 7, 'x': 2, 'y': 4}
        s = Square.create(**s_dict)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 4)

    def test_create_with_extra_attributes(self):
        r_dict = {'id': 3, 'width': 3, 'height': 3, 'x': 1, 'y': 1, 'color': 'red', 'border': 'dashed'}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.id, 3)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertFalse(hasattr(r, 'color'))
        self.assertFalse(hasattr(r, 'border'))

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[0].height, 7)
        self.assertEqual(rectangles[0].x, 2)
        self.assertEqual(rectangles[0].y, 8)
        self.assertEqual(rectangles[1].width, 2)
        self.assertEqual(rectangles[1].height, 4)
        self.assertEqual(rectangles[1].x, 0)
        self.assertEqual(rectangles[1].y, 0)
        os.remove("Rectangle.json")



if __name__ == "__main__":
    unittest.main()
