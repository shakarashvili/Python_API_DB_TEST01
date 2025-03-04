import unittest
import cv2
import numpy as np

class TestOpenCVFunctions(unittest.TestCase):

    def setUp(self):
        """Setup test: Load or create an image before running tests"""
        self.image = np.zeros((500, 500, 3), dtype=np.uint8)  # Black image for testing
        cv2.putText(self.image, "OpenCV", (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    def test_read_write_image(self):
        """Test image read and write"""
        cv2.imwrite("test_image.jpg", self.image)
        loaded_image = cv2.imread("test_image.jpg")
        self.assertIsNotNone(loaded_image, "Failed to load image")

    def test_resize_image(self):
        """Test image resizing"""
        resized = cv2.resize(self.image, (250, 250))
        self.assertEqual(resized.shape[:2], (250, 250), "Image resizing failed")

    def test_convert_grayscale(self):
        """Test converting image to grayscale"""
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.assertEqual(len(gray.shape), 2, "Grayscale image should have 2 dimensions")

    def test_blur_image(self):
        """Test image blurring"""
        blurred = cv2.GaussianBlur(self.image, (5, 5), 0)
        self.assertEqual(blurred.shape, self.image.shape, "Blurring did not preserve dimensions")

    def test_canny_edge_detection(self):
        """Test edge detection"""
        edges = cv2.Canny(self.image, 100, 200)
        self.assertEqual(len(edges.shape), 2, "Edge-detected image should be 2D")

    def test_find_contours(self):
        """Test contour detection"""
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.assertGreater(len(contours), 0, "No contours found")

    def test_draw_shapes(self):
        """Test drawing a rectangle"""
        output = self.image.copy()
        cv2.rectangle(output, (50, 50), (200, 200), (0, 255, 0), 3)
        self.assertEqual(output.shape, self.image.shape, "Drawing shape altered image size")

    def test_histogram_equalization(self):
        """Test histogram equalization on grayscale image"""
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        equalized = cv2.equalizeHist(gray)
        self.assertEqual(equalized.shape, gray.shape, "Histogram equalization failed")

    def test_perspective_transform(self):
        """Test perspective transformation"""
        pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
        pts2 = np.float32([[10, 100], [180, 50], [100, 250], [250, 200]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        transformed = cv2.warpPerspective(self.image, matrix, (500, 500))
        self.assertEqual(transformed.shape, self.image.shape, "Perspective transform failed")

if __name__ == "__main__":
    unittest.main()
