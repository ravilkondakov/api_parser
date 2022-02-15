import unittest

from run import api_parser


class TestApiFunc(unittest.TestCase):

    def setUp(self) -> None:
        self.url_current = 'https://api.thedogapi.com/v1/breeds/1'
        self.response_current, self.request_current = api_parser(self.url_current)
        self.url_wrong = 'https://www.youtube.com/'
        self.response_uncurrent, self.request_uncurrent = api_parser(self.url_wrong)

    def test_api_parse_status_code_200(self):
        self.assertEqual(self.response_current.status_code, 200)

    def test_api_parse_headers(self):
        self.assertEqual(self.response_current.headers.get("Content-Type"), 'application/json; charset=utf-8')

    def test_api_parse_json(self):
        self.assertEqual(dict, type(self.request_current))

    def test_api_parse_uncurrent_status_code(self):
        self.assertEqual(self.response_uncurrent.status_code, 200)

    def test_api_parse_uncurrent_content_type(self):
        self.assertEqual(self.response_uncurrent.headers.get("Content-Type"), 'text/html; charset=utf-8')


if __name__ == '__main__':
    unittest.main()
