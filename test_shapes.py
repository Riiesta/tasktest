import unittest
from shapes import Circle, Triangle

class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.area(), 12.56637061435, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6, places=5)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_triangle())

if __name__ == '__main__':
    unittest.main()
