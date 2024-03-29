#!/usr/bin/env/python3

from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Dude, Grant"
        expected = "Grant Dude"
        self.assertEqual(rearrange_name(testcase), expected)

# Add an edge case.
    def test_empty_string(self):
        """This edge case tests what will happen when an
        empty string is passed into the function as a testcase"""
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

# Additional cases.
    def test_double_name(self):
        """Tests if someone with more than one given name still gets their name
        rearranged."""
        testcase = "Knoetze, Grant A."
        expected = "Grant A. Knoetze"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_single_name(self):
        """Tests what will happen if someone with a single name
        is present"""
        testcase = "Grant"
        expected = "Grant"
        self.assertEqual(rearrange_name(testcase), expected)





