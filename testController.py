import shutil
import tempfile
import unittest
from os import path

import QtPad_controller as controller


class TestExample(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_something(self):
        # testfilename
        test_filename = "test.txt"
        # save any kind of data into file
        controller.SaveFile(test_filename, "The owls are not what they seem")
        # just read from file
        body_from_file = controller.ReadFile(test_filename)
        # compare
        self.assertEqual(body_from_file, 'The owls are not what they seem')


if __name__ == '__main__':
    unittest.main()
