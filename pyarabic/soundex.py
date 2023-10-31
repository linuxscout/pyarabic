#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
soundex
Utility functions used by to encode homophones to the same representation so that they can be matched despite minor differences in spelling (Method was imitated with the one in phpAr)
@author: Odai Alghamdi <odai-alghamdi at outlook dot com>
@author: Odai Alghamdi
@contact: Odai Alghamdi at outlook dot com
@copyright: Arabtechies, Arabeyes, Taha Zerrouki
@license: GPL
@date:2023/10/31
@version:0.3
"""
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
)
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
)
SOUNDEX_CODE = {
    u'\u0627' : "0",
    u'\u0648' : "0",
    u'\u064a' : "0",
    u'\u0639' : "0",
    u'\u062d' : "0",
    u'\u0647' : "0",
    u'\u0641' : "1",
    u'\u0628' : "1",
    u'\u062e' : "2",
    u'\u062c' : "2",
    u'\u0632' : "2",
    u'\u0633' : "2",
    u'\u0635' : "2",
    u'\u0638' : "2",
    u'\u0642' : "2",
    u'\u0643' : "2",
    u'\u063a' : "2",
    u'\u0634' : "2",
    u'\u062a' : "3",
    u'\u062b' : "3",
    u'\u062f' : "3",
    u'\u0630' : "3",
    u'\u0636' : "3",
    u'\u0637' : "3",
    u'\u0629' : "3",
    u'\u0644' : "4",
    u'\u0645' : "5",
    u'\u0646' : "5",
    u'\u0631' : "6",
}

SOUNDEX_TRANSLATION = {
    u'\u0627' : "A", # أ
    u'\u0628' : "B", # ب
    u'\u062a' : "T", # ت
    u'\u062b' : "T", # ث
    u'\u062c' : "J", # ج
    u'\u062d' : "H", # ح
    u'\u062e' : "K", # خ
    u'\u062f' : "D", # د
    u'\u0630' : "Z", # ذ
    u'\u0631' : "R", # ر
    u'\u0632' : "Z", # ز
    u'\u0633' : "S", # س
    u'\u0634' : "S", # ش
    u'\u0635' : "S", # ص
    u'\u0636' : "D", # ض
    u'\u0637' : "T", # ط
    u'\u0638' : "Z", # ظ
    u'\u0639' : "A", # ع
    u'\u063a' : "G", # غ
    u'\u0641' : "F", # ف
    u'\u0642' : "Q", # ق
    u'\u0643' : "K", # ك
    u'\u0644' : "L", # ل
    u'\u0645' : "M", # م
    u'\u0646' : "N", # ن
    u'\u0647' : "H", # ه
    u'\u0648' : "W", # و
    u'\u064a' : "Y", # ي
}



def arSoundexMapCode(word):

    encodedWord = ''
    wordLength = len(word)

    for i in range(wordLength):
        char = word[i]
        if char in SOUNDEX_CODE:
            encodedWord += SOUNDEX_CODE[char]
        else:
            encodedWord+= str(0)
        
    return encodedWord


def arSoundexTrimRep(word):

    lastChar  = None
    cleanWord = ""
    wordLength = len(word)

    for i in range(wordLength):
        char = word[i]
        if char != lastChar:
            cleanWord+= char
        lastChar = char
    return cleanWord


def soundex(word , length = 6):
    soundex = word[0]
    soundex = SOUNDEX_TRANSLATION[soundex]
    rest = word[1:]

    encodedRest = arSoundexMapCode(rest)
    cleanEncodedRest = arSoundexTrimRep(encodedRest)
    
    soundex += cleanEncodedRest
    soundex = soundex.replace("0","")
    totalLen = len(soundex)

    if totalLen > length :
        soundex = soundex[0:length]
    else:
        soundex += "0"*(length - totalLen)
    return soundex
