import unittest
import rectangle

class RectangleTest(unittest.TestCase):
    def test_rectangle1(self):
        res = rectangle.area(0,0)
        self.assertEqual(res,0)

    def test_rectangle2(self):
        res = rectangle.area(2,3)
        self.assertEqual(res,6)

    def test_rectangle3(self):
        res = rectangle.area(40,30)
        self.assertEqual(res,1200)

    def test_rectangle4(self):
        res = rectangle.perimeter(0,0)
        self.assertEqual(res,0)

    def test_rectangle5(self):
        res = rectangle.perimeter(2,3)
        self.assertEqual(res,10)

    def test_rectangle6(self):
        res = rectangle.perimeter(40,30)
        self.assertEqual(res,140)
