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
import pyarabic.araby as ar

class ArabyTestCase(unittest.TestCase):
    """Tests for `araby.py`."""

    def test_strip_tashkeel(self):
        """Test striped tashkeel for العربية?"""
        word = u"الْعَرَبِيَّةُ"
        word_nm = u'العربية'
        self.assertEqual(ar.strip_tashkeel(word), word_nm)
        self.assertNotEqual(ar.strip_tashkeel(word), word)
    def test_strip_harakat(self):
        """Test striped tashkeel for العربية?"""
        word = u"الْعَرَبِيَّةُ"
        word_nm = u'العربيّة'
        self.assertEqual(ar.strip_harakat(word), word_nm)
        self.assertNotEqual(ar.strip_harakat(word), word)
        
    def test_waznlike(self):
        """Test if wazn like?"""
        word = u"ضارب"
        wazn = u"فَاعِل"
        self.assertTrue(ar.waznlike(word, wazn))

    def test_shaddalike(self):
        """Test if shadda  like?"""
        word1 = u"ردّ"
        word2=u"ردَّ"
        self.assertTrue(ar.shaddalike(word1, word2))
                
    def test_joint(self):
        """Test Join function ?"""
        letters = u"العربية"
        marks = u'\u064e\u0652\u064e\u064e\u064e\u064e\u064f'
        self.assertEqual(ar.joint(letters, marks), u"اَلْعَرَبَيَةُ")
    def test_seperate(self):
        """Test Separate function ?"""
        letters = u"العربية"
        marks = u'\u064e\u0652\u064e\u064e\u064e\u064e\u064f'
        word = u"اَلْعَرَبَيَةُ"
        l, m= ar.separate(word)
        
        self.assertEqual(ar.joint(l,m), word)
        self.assertEqual(ar.separate(ar.joint(letters,marks)), (letters,marks))
    
    def test_vocalized_similarity(self):
        """Test vocalized_similarity function ?"""
        word1 = u"ضَربٌ"
        word2 = u"ضَرْبٌ"
        self.assertTrue(ar.vocalizedlike(word1, word2))
        self.assertNotEqual(ar.vocalized_similarity(word1, word2), -2)
        self.assertTrue(ar.vocalized_similarity(word1, word2))
        
    def test_vocalizedlike(self):
        """Test vocalizedlike function ?"""
        word1 = u"ضَربٌ"
        word2 = u"ضَرْبٌ"
        self.assertTrue(ar.vocalizedlike(word1, word2))
        
    def test_normalize_hamza(self):
        """Test normalize_hamzafunction ?"""
        text1 = u"جاء سؤال الأئمة عن الإسلام آجلا"
        text2 = u'جاء سءال الءءمة عن الءسلام ءءجلا'
        self.assertEqual(ar.normalize_hamza(text1), text2)
        text1 = u"جاء سؤال الأئمة عن الإسلام آجلا"
        text3 = u"جاء سوال الايمة عن الاسلام اجلا"
        self.assertEqual(ar.normalize_hamza(text1, method="tasheel"), text3)
        
    def test_normalize_alefat(self):
        """Test normalize_alefat ?"""
        text1 = u"بِٱلْهُدَىٰ"
        text2 = u"بِالْهُدَا"
        self.assertEqual(ar.normalize_alef(text1), text2)
        
    def test_reduce_tashkeel(self):
        """Test reduce_tashkeel function ?"""
        word1 = u"يُتَسََلَّمْنَ"
        word2 = u"يُتسلّمن"
        self.assertEqual(ar.reduce_tashkeel(word1), word2, msg=u"%s :"%ar.reduce_tashkeel(word1))
        
        
    def test_tokenize(self):
        """Test  tokenize function ?"""
        text1 = u"العربية: لغة جميلة."
        wordlist = [u'العربية',u":", u"لغة", u"جميلة", u"."]
        self.assertEqual(ar.tokenize(text1), wordlist)
        
    def test_fix_spaces(self):
        """Test  fix spaces function ?"""
        text1 = u"كل فرد في الأمة مجند لمعركة المصير: الفلاح في حقله، والعامل في مصنعه، والطالب في معهده، والموظف في ديوانه..."
        text2 = u"كل فرد في الأمة مجند لمعركة المصير: الفلاح في حقله، والعامل في مصنعه، والطالب في معهده، والموظف في ديوانه..."
        self.assertEqual(ar.fix_spaces(text1), text2)
        
    def test_autocorrect(self):
        """Test  auto correct"""
        word1 = u"مُُضاعَفة"
        word2 = u"مُضاعَفة"
        self.assertEqual(ar.autocorrect(word1), word2)
        text1 = u"حَرَكَة مُُضاعَفة َسابقة  قبل شَّدة سابقاً"
        text2 = u"حَرَكَة مُضاعَفة سابقة  قبل شّدة سابقًا"
        self.assertEqual(ar.autocorrect(text1), text2)

    def test_spellit(self):
        """Test  spellit"""
        word1 = u"مُضاّعَفة"
        word2 = u"ميم, ضمة, ضاد, ألف, شدة, عين, فتحة, فاء, تاء مربوطة"
        word3 = u"ARABIC LETTER MEEM, ARABIC DAMMA, ARABIC LETTER DAD, ARABIC LETTER ALEF, ARABIC SHADDA, ARABIC LETTER AIN, ARABIC FATHA, ARABIC LETTER FEH, ARABIC LETTER TEH MARBUTA"
        self.assertEqual(ar.spellit(word1), word2)
        self.assertEqual(ar.spellit(word1, "unicode"), word3)

    def test_sentence_tokenize(self):
        """Test  sentence tokenize function ?"""
        text1 = u"العربية لغة جميلة. والبلاد بعيدة، والشوق زائد"
        sentences =['العربية لغة جميلة.', 'والبلاد بعيدة،', 'والشوق زائد']
        self.assertEqual(ar.sentence_tokenize(text1), sentences)        

if __name__ == '__main__':
    unittest.main()
