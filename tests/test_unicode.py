#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )
import sys
sys.path.append("../")
import  pyarabic.araby as araby

for c in araby.arabicrange():
    print(c,'\t', araby.name(c),end=" ")
    print('\t',end=" ")
    if araby.is_sukun(c): print("sukun", end=" ")
    if araby.is_haraka(c): print("haraka", end=" ")
    if araby.is_shadda(c): print("shadda",end=" ")
    if araby.is_tatweel(c): print("tatweel",end=" ")
    if araby.is_tashkeel(c): print("tashkeel",end=" ")
    if araby.is_tanwin(c): print("tanwin",end=" ")
    if araby.is_shortharaka(c): print("short haraka",end=" ")
    if araby.is_ligature(c):print(" ligature",end=" ")
    if araby.is_ligature(c):print('ligature',end=" ")
    if araby.is_hamza(c):    print('hamza',end=" ")
    if araby.is_alef(c): print('alef',end=" ")
    if araby.is_yehlike(c):  print('yeh',end=" ")
    if araby.is_wawlike(c):  print('waw',end=" ")
    if araby.is_teh(c):  print('teh',end=" ")
    if araby.is_small(c):    print('small',end=" ")
    if araby.is_weak(c): print('weak',end=" ")
    if araby.is_moon(c): print('moon',end=" ")
    if araby.is_sun(c):print('sun',end=" ")
    print(araby.order(c),end=" ")
    print()
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
    print(word,'\t',end=" ")
    if araby.is_vocalized(word): print(' is vocalized',end=" ")
    if araby.is_vocalizedtext(word): print(' is vocalized text',end=" ")
    if araby.is_arabicword(word): print(' is valid word',end=" ")
    else: print("invalid arabic word",end=" ")
    print(' strip harakat', araby.strip_harakat(word),end=" ")
    print(' strip tashkeel', araby.strip_tashkeel(word),end=" ")
    print(' strip tatweel',araby.strip_tatweel(word),end=" ")
    print(' normalize ligature ', araby.normalize_ligature(word),end=" ")
    if araby.vocalizedlike(word, word1): print("vocalized_like",end=" ")
    print()
    word1=word;
if araby.vocalizedlike(u"العربية",u"العرَبية"): print("vocalized_like",end=" ")
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
    print(word,'\t',end=" ")
    if araby.is_vocalized(word): print(' is vocalized',end=" ")
##    if araby.isArabicstring(word): print(' iisArabicstring',
##    else:print(' invalid arabicstring',
    if araby.is_vocalizedtext(word): print(' is vocalized text',end=" ")
    if araby.is_arabicword(word): print(' is valid word',end=" ")
    else: print("invalid arabic word",end=" ")
    #~ print(' strip harakat', araby.strip_harakat(word),end=" ")
    #~ print(' strip tashkeel', araby.strip_tashkeel(word),end=" ")
    #~ print(' strip tatweel',araby.strip_tatweel(word),end=" ")
    #~ print(' normalize ligature ', araby.normalize_ligature(word),end=" ")
    #~ if araby.vocalizedlike(word, word1): print("vocalized_like",end=" ")
    print(' strip harakat', araby.strip_harakat(word),end=" ")
    print(' strip tashkeel', araby.strip_tashkeel(word),end=" ")
    print(' strip tatweel',araby.strip_tatweel(word),end=" ")
    print(' normalize ligature ', araby.normalize_ligature(word),end=" ")
    if araby.vocalizedlike(word, word1): print("vocalized_like",end=" ")
    print();
    word1=word;
if araby.vocalizedlike(u"العربية",u"العرَبية"): print("vocalized_like",end=" ")

