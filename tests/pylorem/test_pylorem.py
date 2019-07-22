import unittest
try:
    # for python3
    import urllib.request as request
except ImportError:
    # For python2
    import urllib as request

class TestAPIAvailability(unittest.TestCase):

    def test_if_api_is_working(self):
        response = request.urlopen('https://loripsum.net/api/plaintext/')
        self.assertEquals('OK', response.msg)
        self.assertEquals(200, response.getcode())

    def test_if_api_is_generating_lorem_text(self):
        response = request.urlopen('https://loripsum.net/api/plaintext/5')
        self.assertTrue(len(response.read().decode('utf8')) > 10)

