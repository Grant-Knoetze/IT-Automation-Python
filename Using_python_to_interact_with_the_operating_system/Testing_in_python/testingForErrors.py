#!/usr/bin/env python3

import unittest

from validations import validate_user

class testValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("valid_user", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)

unittest.main()
