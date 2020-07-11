#!/usr/bin/python
# -*- coding=utf-8 -*-
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )
import unittest
import sys
sys.path.append('../pyarabic')
import pyarabic.trans as trans

class ArabyTestCase(unittest.TestCase):
    """Tests for `trans.py`."""

    def test_encode_tashkeel(self):
        """Test  encode/decode tashkeel"""
        word1 = u"هَارِبًا"
        letters = u"هاربا" 
        encoded_marks = u"a0iA0"
        self.assertEqual(trans.encode_tashkeel(word1), (letters, encoded_marks))
        self.assertEqual(trans.decode_tashkeel(letters, encoded_marks), word1)
        
        encoded_marks = 40610
        self.assertEqual(trans.encode_tashkeel(word1, "decimal"), (letters, encoded_marks))
        self.assertEqual(trans.decode_tashkeel(letters, encoded_marks, "decimal"), word1)


if __name__ == '__main__':
    unittest.main()
