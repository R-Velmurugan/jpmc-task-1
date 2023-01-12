import unittest

import client


class ClientTesting(unittest.TestCase):
    def test_zeroDivisibility(self):
        failure_message = "cannot divide by zero"
        self.assertTrue(client.denominator != 0)
        self.assertFalse(client.denominator == 0 , failure_message)  # add assertion here


if __name__ == '__main__':
    unittest.main()
