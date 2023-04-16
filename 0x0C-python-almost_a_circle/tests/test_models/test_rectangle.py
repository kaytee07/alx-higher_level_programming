import unittest
from models.rectangle import Rectangle


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
            r.height = "b"
        with self.assertRaises(ValueError):
            r.x = -1
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
        output = "\n ####\n ####\n"

    if __name__ == '__main__':
        unittest.main()
