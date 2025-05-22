import unittest
from phishing_detector.detector import is_phishing_url

class TestPhishingDetector(unittest.TestCase):

    def test_safe_url(self):
        result = is_phishing_url("https://www.google.com")
        self.assertFalse(result["is_phishing"])
        self.assertGreater(result["confidence"], 70)

    def test_phishing_url(self):
        result = is_phishing_url("http://secure-paypal-login.com")
        self.assertTrue(result["is_phishing"])
        self.assertGreater(result["confidence"], 70)

    def test_empty_url(self):
        result = is_phishing_url("")
        # Either False with low confidence or a handled edge case
        self.assertIn(result["is_phishing"], [False, True])
        self.assertLess(result["confidence"], 60)

if __name__ == '__main__':
    unittest.main()
