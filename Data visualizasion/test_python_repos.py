import unittest

from python_repos import r, response_dict
class ReposTestCase(unittest.TestCase):

    def test_status_code(self):
        self.assertEqual(r.status_code, 200)

    
    def test_items_presense(self):
        self.assertGreater(len(response_dict['items']), 0)


if __name__ == '__main__':
    unittest.main()
