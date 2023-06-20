import unittest

from pip_install_from_gh_producer_private import test_function_private

class TestTestFunctionPrivate(unittest.TestCase):
    """ Test the test_function_private function """
    def test_should_exist(self) -> None:
        """ it should exist """
        self.assertIsNotNone(test_function_private)
