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

    def test_normalize_digits(self):
        nd_text = u'۰۱۲۳۴۵۶۷۸۹ ٠١٢٣٤٥٦٧٨٩ 123456789 نص'
        self.assertEqual(trans.normalize_digits(nd_text, source='all', out='east'), '٠١٢٣٤٥٦٧٨٩ ٠١٢٣٤٥٦٧٨٩ ١٢٣٤٥٦٧٨٩ نص') 
        self.assertEqual(trans.normalize_digits(nd_text, source='all', out='west'), '0123456789 0123456789 123456789 نص') 
        self.assertEqual(trans.normalize_digits(nd_text, source='all', out='persian'), '۰۱۲۳۴۵۶۷۸۹ ۰۱۲۳۴۵۶۷۸۹ ۱۲۳۴۵۶۷۸۹ نص') 
   
        self.assertEqual(trans.normalize_digits(nd_text, source='east', out='east'), '۰۱۲۳۴۵۶۷۸۹ ٠١٢٣٤٥٦٧٨٩ 123456789 نص') 
        self.assertEqual(trans.normalize_digits(nd_text, source='east', out='west'), '۰۱۲۳۴۵۶۷۸۹ 0123456789 123456789 نص') 
        self.assertEqual(trans.normalize_digits(nd_text, source='east', out='persian'), '۰۱۲۳۴۵۶۷۸۹ ۰۱۲۳۴۵۶۷۸۹ 123456789 نص') 

        self.assertEqual(trans.normalize_digits(nd_text, source='west', out='east'), '۰۱۲۳۴۵۶۷۸۹ ٠١٢٣٤٥٦٧٨٩ ١٢٣٤٥٦٧٨٩ نص') 
        self.assertEqual(trans.normalize_digits(nd_text, source='west', out='west'), '۰۱۲۳۴۵۶۷۸۹ ٠١٢٣٤٥٦٧٨٩ 123456789 نص') 
        self.assertEqual(trans.normalize_digits(nd_text, source='west', out='persian'), '۰۱۲۳۴۵۶۷۸۹ ٠١٢٣٤٥٦٧٨٩ ۱۲۳۴۵۶۷۸۹ نص') 

        self.assertEqual(trans.normalize_digits(nd_text, source='persian', out='east'), '٠١٢٣٤٥٦٧٨٩ ٠١٢٣٤٥٦٧٨٩ 123456789 نص') 
        self.assertEqual(trans.normalize_digits(nd_text, source='persian', out='west'), '0123456789 ٠١٢٣٤٥٦٧٨٩ 123456789 نص') 
        self.assertEqual(trans.normalize_digits(nd_text, source='persian', out='persian'), '۰۱۲۳۴۵۶۷۸۹ ٠١٢٣٤٥٦٧٨٩ 123456789 نص') 
    def test_segment_language(self,):
        """ test segment language"""
        text =u"""السلام عليكم how are you, لم اسمع أخبارك منذ مدة, where are you going"""
        
        result = [(u'arabic', u'السلام عليكم'), (u'latin', u' how are you, '), (u'arabic', u'لم اسمع أخبارك منذ مدة'), (u'latin', u', where are you going')]
        self.assertEqual(trans.segment_language(text), result) 

        text =u"""Salam السلام عليكم how are you, لم اسمع أخبارك منذ مدة, where are you going"""
        result = [(u'latin', u'Salam '), (u'arabic', u'السلام عليكم'), (u'latin', u' how are you, '), (u'arabic', u'لم اسمع أخبارك منذ مدة'), (u'latin', u', where are you going')]
        self.assertEqual(trans.segment_language(text), result) 

if __name__ == '__main__':
    unittest.main()
