#!/usr/bin/python
# -*- coding=utf-8 -*-
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )

import unittest

import pyarabic.araby as Araby

class TestSequenceFunctions(unittest.TestCase):

    def test_is_letter(self):

        self.assertTrue(Araby.is_sukun(Araby.SUKUN))
        self.assertTrue(Araby.is_shadda(Araby.SHADDA))
        self.assertTrue(Araby.is_tatweel(Araby.TATWEEL))

        for archar in Araby.TANWIN:
            self.assertTrue(Araby.is_tanwin(archar))

        for archar in Araby.TASHKEEL:
            self.assertTrue(Araby.is_tashkeel(archar))

        for haraka in Araby.HARAKAT:
            self.assertTrue(Araby.is_haraka(haraka))

        for short_haraka in Araby.SHORTHARAKAT:
            self.assertTrue(Araby.is_shortharaka(short_haraka))

        for liguature in Araby.LIGUATURES:
            self.assertTrue(Araby.is_ligature(liguature))

        for hamza in Araby.HAMZAT:
            self.assertTrue(Araby.is_hamza(hamza))

        for alef in Araby.ALEFAT:
            self.assertTrue(Araby.is_alef(alef))

        for yeh in Araby.YEHLIKE:
            self.assertTrue(Araby.is_yehlike(yeh))

        for waw in Araby.WAWLIKE:
            self.assertTrue(Araby.is_wawlike(waw))

        for teh in Araby.TEHLIKE:
            self.assertTrue(Araby.is_teh)

        for small in Araby.SMALL:
            self.assertTrue(Araby.is_small(small))

        for weak in Araby.WEAK:
            self.assertTrue(Araby.is_weak(weak))

        for archar in Araby.MOON:
            self.assertTrue(Araby.is_moon(archar))

        for archar in  Araby.SUN:
            self.assertTrue(Araby.is_sun(archar))

    def test_general_letters(self):

        # test order()
        assert Araby.order(Araby.ALEF) == 1
        assert Araby.order(Araby.HAMZA) == 29
        assert Araby.order(Araby.YEH) == 28
        assert Araby.order(Araby.TEH_MARBUTA) == 3
        assert Araby.order(Araby.TEH) == 3

        # test name()
        assert Araby.name(u"أ") == u'همزة على الألف'
        assert Araby.name(u"ب") == u'باء'
        assert Araby.name(Araby.ALEF_HAMZA_ABOVE) == u'همزة على الألف'
        assert Araby.name(u"ة") == u'تاء مربوطة'

    def test_has_letter(self):

        self.assertTrue(Araby.has_shadda(u'العربيّة'))
        self.assertFalse(Araby.has_shadda(u'العربية'))

    def test_word_text(self):

        # is_vocalized(word)
        self.assertFalse(Araby.is_vocalized(u'العربية'))
        self.assertTrue(Araby.is_vocalized(u'الْعَرَبِيّةُ'))

        # is_vocalized(word)
        self.assertFalse(Araby.is_vocalizedtext(u"العربية لغة جميلة"))
        self.assertTrue(Araby.is_vocalizedtext(u'الْعَرَبيَّة لُغَةٌ جَمِيلَةٌ'))

        # is_arabicstring TODO: add more examples
        self.assertTrue(Araby.is_arabicstring(u'العربية'))

        # is_arabicrange TODO: add test

        # is_arabicword TODO: test other cases

        self.assertFalse(Araby.is_arabicword(u""))

        self.assertFalse(Araby.is_arabicword(u"ْلاندخل")) # start with sukun

        self.assertFalse(Araby.is_arabicword(u'ؤكل')) # start with waw hamza above
        self.assertFalse(Araby.is_arabicword(u'ئكل')) # start with waw hamza above4
        self.assertFalse(Araby.is_arabicword(u'ةدخل')) # start with teh_marbuta

        self.assertTrue(Araby.is_arabicword(u"العربية"))

    def test_char(self):

        # first_char(word)
        assert Araby.first_char(u"محمد") == u'م'

        # second_char(word)
        assert Araby.second_char(u"محمد") == u'ح'

        #  last_char(word)
        assert Araby.last_char(u'محمد') == u'د'

        # secondlast_char
        assert Araby.secondlast_char(u'محمد') == u'م'

    def test_strip(self):

        # strip_harakat(text):
        assert Araby.strip_harakat(u"الْعَرَبِيّةُ") == u'العربيّة'

        # strip_lastharaka(text)
        assert Araby.strip_lastharaka(u"الْعَرَبِيّةُ") == u'الْعَرَبِيّة'

        # strip_tashkeel(text)
        assert Araby.strip_tashkeel(u"الْعَرَبِيّةُ") == u'العربية'

        # strip_tatweel(text):
        assert Araby.strip_tatweel(u"العـــــربية") == u'العربية'

        # strip_shadda(text):
        assert Araby.strip_shadda(u"الشّمسيّة") == u'الشمسية'

    def test_normalization(self):

        # normalize_ligature(text):TODO: fixme gives 'لانها لالء الاسلام'
        # assert  Araby.normalize_ligature( u"لانها لالء الاسلام") == u'لانها لالئ الاسلام'

        # normalize_hamza(word)
        assert Araby.normalize_hamza(u"سئل أحد الأئمة") == u'سءل ءحد الءءمة'

    #def test_separate(self): # TODO: testme

        # separate(word,  extract_shadda = False)

    def test_join(self):

        # joint(letters,  marks)
        marks = u'\u064e\u0652\u064e\u064e\u064e\u064e\u064f'
        assert Araby.joint(u"العربية", marks) == u'اَلْعَرَبَيَةُ'

    def test_vocalizedlike(self):

        # vocalizedlike(word1, word2)
        word1 = u"ضَربٌ"
        word2 = u"ضَرْبٌ"
        self.assertTrue(Araby.vocalizedlike(word1, word2))

    def test_waznlike(self):

        # waznlike(word1, wazn):
        word1 = u"ضارب"
        wazn = u"فَاعِل"
        wazn1 = u"فعال"
        self.assertTrue(Araby.waznlike(word1, wazn))
        self.assertFalse(Araby.waznlike(word1, wazn1))

    def test_shaddalike(self):

        # shaddalike(partial, fully)
        word1 = u"ردّ"
        word2 = u"ردَّ"
        word3 = u"رد"
        self.assertTrue(Araby.shaddalike(word1, word2))
        self.assertFalse(Araby.shaddalike(word1, word3))

    def test_reduce_tashkeel(self):

        # reduce_tashkeel(text)
        word = u"يُتَسََلَّمْنَ"
        assert  Araby.reduce_tashkeel(word) == u'يُتسلّمن'

    def test_vocalized_similarity(self):

        # vocalized_similarity(word1, word2)
        word1 = u"ضَربٌ"
        word2 = u"ضَرْبٌ"
        word3 = u"ضَرْبٍ"
        self.assertTrue(Araby.vocalized_similarity(word1, word2))
        assert  Araby.vocalized_similarity(word1, word3) == -1

    def test_tokenize(self):

        #tokenize(text = u"")

        tests = ['اللُّغَةُ الْعَرَبِيَّةُ جَمِيلَةٌ.',
                 'انما الْمُؤْمِنُونَ اخوه فاصلحوا بَيْنَ اخويكم',
                 'الْعَجُزُ عَنِ الْإِدْرَاكِ إِدْرَاكٌ، وَالْبَحْثَ فِي ذاتِ اللَّه اشراك.',
                 'اللَّهُمُّ اُسْتُرْ عُيُوبَنَا وَأَحْسَنَ خَوَاتِيمَنَا الْكَاتِبِ: نَبِيلُ جلهوم',
                 'الرَّأْي قَبْلَ شَجَاعَة الشّجعَانِ',
                 'فَأَنْزَلْنَا مِنْ السَّمَاء مَاء فَأَسْقَيْنَاكُمُوهُ',
                 'سُئِلَ بَعْضُ الْكُتَّابِ عَنِ الْخَطّ، مَتَى يَسْتَحِقُّ أَنْ يُوصَفَ بِالْجَوْدَةِ ؟'
                 ]

        results = []
        for test in tests:
            result = Araby.tokenize(test)
            results.append(result)

        target = [['اللُّغَةُ', 'الْعَرَبِيَّةُ', 'جَمِيلَةٌ', '.'],
                  ['انما', 'الْمُؤْمِنُونَ', 'اخوه', 'فاصلحوا', 'بَيْنَ', 'اخويكم'],
                  ['الْعَجُزُ', 'عَنِ', 'الْإِدْرَاكِ', 'إِدْرَاكٌ', '،', 'وَالْبَحْثَ', 'فِي', 'ذاتِ', 'اللَّه',
                   'اشراك', '.'],
                  ['اللَّهُمُّ', 'اُسْتُرْ', 'عُيُوبَنَا', 'وَأَحْسَنَ', 'خَوَاتِيمَنَا', 'الْكَاتِبِ', ':', 'نَبِيلُ',
                   'جلهوم'],
                  ['الرَّأْي', 'قَبْلَ', 'شَجَاعَة', 'الشّجعَانِ'],
                  ['فَأَنْزَلْنَا', 'مِنْ', 'السَّمَاء', 'مَاء', 'فَأَسْقَيْنَاكُمُوهُ'],
                  ['سُئِلَ', 'بَعْضُ', 'الْكُتَّابِ', 'عَنِ', 'الْخَطّ', '،', 'مَتَى', 'يَسْتَحِقُّ', 'أَنْ', 'يُوصَفَ',
                   'بِالْجَوْدَةِ', '؟']
                  ]
        self.assertEqual(results, target)

if __name__ == "__main__":
    unittest.main()
