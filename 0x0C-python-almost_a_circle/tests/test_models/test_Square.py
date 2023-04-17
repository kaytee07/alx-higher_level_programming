#!/usr/bin/python3
"""Python tests for class Square"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_Square_class_creation(self):
        s = Square(12, 1, 2, 10)
        self.assertEqual(s.width, 12)
        self.assertEqual(s.height, 12)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)

    def test_Suare_class_creation_No_Id(self):
        s = Square(12, 1, 2)
        self.assertIsNotNone(s.id)

    def test_Square_size_width_setter(self):
        s = Square(1, 3, 5, 7)
        s.size = 23
        self.assertEqual(s.width, 23)

    def test_Square_size_height_setter(self):
        s = Square(1, 3, 5, 7)
        s.size = 40
        self.assertEqual(s.width, 40)

    def test_Square_size_width_setter_TypeError_strings(self):
        s = Square(1, 3, 5, 7)
        with self.assertRaises(TypeError):
            s.size = "boy get out the way"

    def test_Square_size_width_setter_TypeError_boolean(self):
        s = Square(1, 3, 5, 7)
        with self.assertRaises(TypeError):
            s.size = False

    def test_Square_size_width_setter_TypeError_float(self):
        s = Square(1, 3, 5, 7)
        with self.assertRaises(TypeError):
            s.size = 2.5

    def test_Square_size_width_setter_ValueError(self):
        s = Square(1, 3, 5, 7)
        with self.assertRaises(ValueError):
            s.size = -1

    def test_update_width_args(self):
        s = Square(1, 3, 5, 7)
        s.update(4, 12, 8, 9)
        self.assertEqual(s.width, 12)

    def test_update_height_args(self):
        s = Square(1, 3, 5, 7)
        s.update(4, 12, 8, 9)
        self.assertEqual(s.width, 12)

    def test_update_x_args(self):
        s = Square(1, 3, 5, 7)
        s.update(4, 12, 8, 9)
        self.assertEqual(s.x, 8)

    def test_update_y_args(self):
        s = Square(1, 3, 5, 7)
        s.update(4, 12, 8, 9)
        self.assertEqual(s.y, 9)

    def test_update_id_args(self):
        s = Square(1, 3, 5, 7)
        s.update(4, 12, 8, 9)
        self.assertEqual(s.id, 4)

    def test_update_width_kwargs(self):
        s = Square(1, 3, 5, 7)
        s.update(size=15)
        self.assertEqual(s.width, 15)

    def test_update_height_kwargs(self):
        s = Square(1, 3, 5, 7)
        s.update(size=100)
        self.assertEqual(s.height, 100)

    def test_update_x_kwargs(self):
        s = Square(1, 3, 5, 7)
        s.update(x=12)
        self.assertEqual(s.x, 12)

    def test_update_y_kwargs(self):
        s = Square(1, 3, 5, 7)
        s.update(y=10)
        self.assertEqual(s.y, 10)

    def test_update_id_kwargs(self):
        s = Square(1, 3, 5, 7)
        s.update(id=11)
        self.assertEqual(s.id, 11)

    def test_update_width_args_typeError(self):
        s = Square(1, 3, 5, 7)
        with self.assertRaises(TypeError):
            s.update(13, False, 8, 9)

    def test_update_height_args_ValueError(self):
        s = Square(1, 3, 5, 7)
        with self.assertRaises(ValueError):
            s.update(13, -12, 8, 9)

    def test_update_x_args_TypeError(self):
        s = Square(1, 3, 5, 7)
        with self.assertRaises(TypeError):
            s.update(123, 12, 3.7, 9)

    def test_update_y_args_ValueError(self):
        s = Square(1, 3, 5, 7)
        with self.assertRaises(ValueError):
            s.update(123, 12, 3, -1)

    def test_update_width_kwargs_ValueError(self):
        s = Square(1, 3, 5, 7)
        with self.assertRaises(ValueError):
            s.update(size=-4)

    def test_update_height_kwargs_TypeError(self):
        s = Square(1, 3, 5, 7)
        with self.assertRaises(TypeError):
            s.update(size=True)

    def test_update_x_kwargs_ValueError(self):
        s = Square(1, 3, 5, 7)
        with self.assertRaises(ValueError):
            s.update(x=-4)

    def test_update_y_kwargs_TypeError(self):
        s = Square(1, 3, 5, 7)
        with self.assertRaises(TypeError):
            s.update(size="twenty")

    def test_to_dictionary(self):
        """Test the to_dictionary method of Square"""
        s = Square(10, 20, 6, 7)
        d = {'id': 7, 'width': 10, 'height': 10, 'x': 20, 'y': 6}
        self.assertEqual(s.to_dictionary(), d)
