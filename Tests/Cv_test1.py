import unittest
import cv2
import numpy as np

class TestOpenCV(unittest.TestCase):

    def setUp(self):
        """ Setup test: Load an image before running tests """
        self.image_path = r"C:\Users\user\Desktop\New folder\376852600_10210871287973598_1462141267209980510_n.jpg"  # Ensure this file exists in your working directory
        self.image = cv2.imread(self.image_path)

    def test_image_load(self):
        """ Test if image loads successfully """
        self.assertIsNotNone(self.image, "Failed to load image!")

    def test_image_dimensions(self):
        """ Test if image has valid dimensions """
        height, width, channels = self.image.shape
        self.assertGreater(height, 0, "Image height should be greater than 0")
        self.assertGreater(width, 0, "Image width should be greater than 0")
        self.assertEqual(channels, 3, "Image should have 3 channels (RGB)")

    def test_grayscale_conversion(self):
        """ Test if image converts to grayscale correctly """
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.assertEqual(len(gray_image.shape), 2, "Grayscale image should have 2 dimensions")

    def test_edge_detection(self):
        """ Test Canny edge detection on the image """
        edges = cv2.Canny(self.image, 100, 200)
        self.assertIsInstance(edges, np.ndarray, "Edge detection should return a NumPy array")
        self.assertEqual(len(edges.shape), 2, "Edge-detected image should have 2 dimensions")

if __name__ == "__main__":
    unittest.main()
