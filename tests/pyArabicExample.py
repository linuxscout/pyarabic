#!/usr/bin/env python
# -*- coding: utf-8 -*-

import  pyarabic.araby as araby


for c in araby.arabicrange():
    print c.encode('utf8'),'\t', araby.name(c).encode('utf8'),
    print '\t',
    if araby.is_sukun(c): print "sukun",
    if araby.is_haraka(c): print "haraka",
    if araby.is_shadda(c): print "shadda",
    if araby.is_tatweel(c): print "tatweel",
    if araby.is_tashkeel(c): print "tashkeel",
    if araby.is_tanwin(c): print "tanwin",
    if araby.is_shortharaka(c): print "short haraka",
    if araby.is_ligature(c):print " ligature",
    if araby.is_ligature(c):print 'ligature',
    if araby.is_hamza(c):    print 'hamza',
    if araby.is_alef(c): print 'alef',
    if araby.is_yehlike(c):  print 'yeh',
    if araby.is_wawlike(c):  print 'waw',
    if araby.is_teh(c):  print 'teh',
    if araby.is_small(c):    print 'small',
    if araby.is_weak(c): print 'weak',
    if araby.is_moon(c): print 'moon',
    if araby.is_sun(c):print 'sun',
    print araby.order(c),
    print;
word=u"الْعَرَيِيّةُ"
word_list=[
u"الْعَرَيِيّةُ",
u"العربية",
u"الْعَرَيِيّةُ الفصحى",
u"غير مشكول",
"Taha",
]
word1=u""
for word in word_list:
    print word.encode('utf8'),'\t',
    if araby.is_vocalized(word): print ' is vocalized',
##    if araby.isArabicstring(word): print ' iisArabicstring',
##    else:print ' invalid arabicstring',
    if araby.is_vocalizedtext(word): print ' is vocalized text',
    if araby.is_arabicword(word): print ' is valid word',
    else: print "invalid arabic word",
    print ' strip harakat', araby.strip_harakat(word).encode('utf8'),
    print ' strip tashkeel', araby.strip_tashkeel(word).encode('utf8'),
    print ' strip tatweel',araby.strip_tatweel(word).encode('utf8'),
    print ' normalize ligature ', araby.normalize_ligature(word).encode('utf8'),
    if araby.vocalizedlike(word, word1): print "vocalized_like",
    print;
    word1=word;
if araby.vocalizedlike(u"العربية",u"العرَبية"): print "vocalized_like",

