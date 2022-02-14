import unittest

from run import api_parser


class TestApiFunc(unittest.TestCase):
    url_current = 'https://api.thedogapi.com/v1/breeds/1'
    url_wrong = 'https://www.youtube.com/'

    def test_api_parse_current(self):
        response, request = api_parser(self.url_current)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get("Content-Type"), 'application/json; charset=utf-8')
        self.assertEqual(dict, type(request))

    def test_api_parse_uncurrent(self):
        response, request = api_parser(self.url_wrong)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get("Content-Type"), 'text/html; charset=utf-8')

if __name__ == '__main__':
    unittest.main()

