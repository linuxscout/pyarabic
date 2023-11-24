#!/usr/bin/python
# -*- coding=utf-8 -*-
import unittest
import pyarabic.soundex as soundex

class SoundexTestCase(unittest.TestCase):
    """Tests for `number.py`."""

    def test_soundex(self):
        self.assertEqual(soundex.soundex("عدي",4),"A300")


if __name__ == '__main__':
    unittest.main()
