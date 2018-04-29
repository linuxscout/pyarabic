#!/usr/bin/python
# -*- coding=utf-8 -*-
import unittest
import sys
import pyarabic.number as nb
import pyarabic.araby as ar

class NumberTestCase(unittest.TestCase):
    """Tests for `number.py`."""

    def test_strip_tashkeel(self):
        """Test striped tashkeel for العربية?"""
        word = u"الْعَرَبِيَّةُ"
        word_nm = u'العربية'
        self.assertEqual(ar.strip_tashkeel(word), word_nm)
        self.assertNotEqual(ar.strip_tashkeel(word), word)
    def test_int2_str(self):
        an = nb.ArNumbers()
        self.assertEqual(an.int2str('125'), u"مئة و خمس و عشرون")

    def test_number2text(self):
        self.assertEqual(nb.number2text('125'), u"مئة و خمس و عشرون")
        self.assertEqual(nb.number2text(125), u"مئة و خمس و عشرون")
        self.assertEqual(nb.number2text(125.5), u"مئة و خمس و عشرون فاصلة خمس")
        self.assertEqual(nb.number2text("125..5"), u"صفر")
if __name__ == '__main__':
    unittest.main()
