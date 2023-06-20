import unittest

from pip_install_from_gh_producer import test_function

class TestTestFunction(unittest.TestCase):
    """ Test the test_function """
    def test_should_work(self) -> None:
        """ It should exist """
        self.assertIsNotNone(test_function)

