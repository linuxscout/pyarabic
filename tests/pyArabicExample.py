#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from  pyarabic import araby


for c in araby.arabicrange():
    print (c,'\t', araby.name(c))
    print ('\t')
    if araby.is_sukun(c): print ("sukun")
    if araby.is_haraka(c): print ("haraka")
    if araby.is_shadda(c): print ("shadda")
    if araby.is_tatweel(c): print ("tatweel")
    if araby.is_tashkeel(c): print ("tashkeel")
    if araby.is_tanwin(c): print ("tanwin")
    if araby.is_shortharaka(c): print ("short haraka"),
    if araby.is_ligature(c):print (" ligature"),
    if araby.is_ligature(c):print ('ligature'),
    if araby.is_hamza(c):    print ('hamza'),
    if araby.is_alef(c): print ('alef'),
    if araby.is_yehlike(c):  print ('yeh'),
    if araby.is_wawlike(c):  print ('waw'),
    if araby.is_teh(c):  print ('teh'),
    if araby.is_small(c):    print ('small'),
    if araby.is_weak(c): print ('weak'),
    if araby.is_moon(c): print ('moon'),
    if araby.is_sun(c):print ('sun'),
    print (araby.order(c)),
    print ();
word=u"الْعَرَيِيّةُ"
word_list=[
u"الْعَرَيِيّةُ",
u"العربية",
u"الْعَرَيِيّةُ الفصحى",
u"غير مشكول",
"Taha",
u"سئل لأنه يؤم الإمام"
]
word1=u""
for word in word_list:
    print (word)
    if araby.is_vocalized(word): print (' is vocalized')
    if araby.is_vocalizedtext(word): print (' is vocalized text')
    if araby.is_arabicword(word): print (' is valid word')
    else: print ("invalid arabic word")
    print (' strip harakat', araby.strip_harakat(word))
    print (' strip tashkeel', araby.strip_tashkeel(word))
    print (' strip tatweel',araby.strip_tatweel(word))
    print (' normalize ligature ', araby.normalize_ligature(word))
    print (' normalize hamza', araby.normalize_hamza(word))
    if araby.vocalizedlike(word, word1): print ("vocalized_like")
    word1=word;
if araby.vocalizedlike(u"العربية",u"العرَبية"): print ("vocalized_like")

