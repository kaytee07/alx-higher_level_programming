import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):

    def test_creation(self):
        r = Rectangle(20, 30, 12, 14)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 14)
        self.assertIsNotNone(r.id)

    def test_setters(self):
        r = Rectangle(20, 30, 12, 14)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.width = "a"
        with self.assertRaises(ValueError):
            r.height = -8
        with self.assertRaises(TypeError):
            r.height = False
        with self.assertRaises(ValueError):
            r.x = -10
        with self.assertRaises(TypeError):
            r.x = "b"
        with self.assertRaises(ValueError):
            r.y = -2
        with self.assertRaises(TypeError):
            r.y = "b"

    def test_width(self):
        r = Rectangle(20, 30, 12, 14)
        r.width = 45
        self.assertEqual(r.width, 45)

    def test_height(self):
        r = Rectangle(20, 30, 12, 14)
        r.height = 15
        self.assertEqual(r.height, 15)

    def test_x(self):
        r = Rectangle(20, 30, 12, 14)
        r.x = 23
        self.assertEqual(r.x, 23)

    def test_y(self):
        r = Rectangle(20, 30, 12, 14)
        r.y = 44
        self.assertEqual(r.y, 44)

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        r = Rectangle(4, 2)
        expected_output = "####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_width(self):
        r = Rectangle(12, 13, id=12)
        r.update(45, 12, 34, 23, 7)
        self.assertEqual(r.width, 12)

    def test_update_height(self):
        r = Rectangle(12, 13, id=12)
        r.update(45, 12, 34, 23, 7)
        self.assertEqual(r.height, 34)

    def test_update_id(self):
        r = Rectangle(12, 13, id=12)
        r.update(45, 12, 34, 23, 7)
        self.assertEqual(r.id, 45)

    def test_update_x(self):
        r = Rectangle(12, 13, id=12)
        r.update(45, 12, 34, 23, 7)
        self.assertEqual(r.x, 23)

    def test_update_y(self):
        r = Rectangle(12, 13, id=12)
        r.update(45, 12, 34, 23, 7)
        self.assertEqual(r.y, 7)

    def test_update_errors(self):
        r = Rectangle(20, 30, 12, 14, 45)
        with self.assertRaises(ValueError):
            r.update(1, -5)
        with self.assertRaises(TypeError):
            r.update(3, "boy go")
        with self.assertRaises(ValueError):
            r.update(23, -5)
        with self.assertRaises(TypeError):
            r.update(22, 44, 33, 12, "boy aloha")
        with self.assertRaises(ValueError):
            r.update(22, 44, -3, 12, 42)
        with self.assertRaises(TypeError):
            r.update(22, 44, "lamer", 12, 29)
        with self.assertRaises(ValueError):
            r.update(22, 44, 33, -2, 67)
        with self.assertRaises(TypeError):
            r.update(22, 44, 33, "123", 67)

    def test_update_kwargs_width(self):
        r = Rectangle(20, 30, 12, 14, 45)
        r.update(width=37)
        self.assertEqual(r.width, 37)

    def test_update_kwargs_height(self):
        r = Rectangle(20, 30, 12, 14, 45)
        r.update(height=3)
        self.assertEqual(r.height, 3)

    def test_update_kwargs_id(self):
        r = Rectangle(20, 30, 12, 14, 45)
        r.update(id=109)
        self.assertEqual(r.id, 109)

    def test_update_kwargs_x(self):
        r = Rectangle(20, 30, 12, 14, 45)
        r.update(x=24)
        self.assertEqual(r.x, 24)

    def test_update_kwargs_y(self):
        r = Rectangle(20, 30, 12, 14, 45)
        r.update(x=6)
        self.assertEqual(r.x, 6)

    def test_update_kwargs_errors(self):
        r = Rectangle(20, 30, 12, 14, 45)
        with self.assertRaises(ValueError):
            r.update(x=-11)
        with self.assertRaises(TypeError):
            r.update(y="boy go")
        with self.assertRaises(ValueError):
            r.update(width=-2)
        with self.assertRaises(TypeError):
            r.update(x=False)
        with self.assertRaises(ValueError):
            r.update(height=-6)
        with self.assertRaises(TypeError):
            r.update(width="width")
        with self.assertRaises(ValueError):
            r.update(y=-2)
        with self.assertRaises(TypeError):
            r.update(height="height")

    if __name__ == '__main__':
        unittest.main()
