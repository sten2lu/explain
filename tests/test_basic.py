import unittest

from explain.main import * 

import os


class TestBasic(unittest.TestCase):

    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.join(self.path, 'fixtures')

    def test_template(self):
        f_path = os.path.join(self.path, 'test_template')
        create_template(f_path)
        self.assertTrue(os.path.exists(f_path))
        os.remove(f_path)
        self.assertFalse(os.path.exists(f_path))

    def test_list(self):
        print("-"*20)
        print("Run Test List")
        list_files(self.path)
        print("-"*20)
        

    def test_search(self):
        print("-"*20)
        print("Run Test Search")
        search_files(self.path)
        print("-"*20)

if __name__ == '__main__':
    unittest.main()

