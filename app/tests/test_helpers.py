#!/usr/bin/python3
""" Tests for all helper scripts
"""

import unittest

from app.utils.helpers import hash_password, verify_password


class TestHelpers(unittest.TestCase):
    """ """

    def setUp(self):
        self.pass_hash = hash_password("testing")

    def test_hash_password(self):
        self.assertNotEqual(self.pass_hash, "testing")
        self.assertIn("argon", self.pass_hash)
        self.assertIsInstance(self.pass_hash, str)

    def test_verify_password(self):
        right_pass = verify_password("testing", self.pass_hash)
        wrong_pass = verify_password("test", self.pass_hash)

        self.assertNotEqual(self.pass_hash, "testing")
        self.assertIn("argon", self.pass_hash)
        self.assertIsInstance(self.pass_hash, str)
        self.assertTrue(right_pass)
        self.assertFalse(wrong_pass)


if __name__ == "__main__":
    unittest.main()
