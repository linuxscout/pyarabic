#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
Arabic Transliteration routins
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@license: GPL
@date:2018/08/146
@version: 0.1
"""
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )

import sys
import re
import pyarabic.araby as ar

t2a_table = { 
'A': ar.ALEF, 
'b': ar.BEH,
't': ar.TEH,
'p': ar.TEH_MARBUTA,
'v': ar.THEH,
'j': ar.JEEM,
'H': ar.HAH,
'x': ar.KHAH,
'd': ar.DAL,
'*': ar.THAL,
'r': ar.REH,
'z': ar.ZAIN,
's': ar.SEEN,
'$': ar.SHEEN,
'S': ar.SAD,
'D': ar.DAD,
'T': ar.TAH,
'Z': ar.ZAH,
'E': ar.AIN,
'g': ar.GHAIN,
'f': ar.FEH,
'q': ar.QAF,
'k': ar.KAF,
'l': ar.LAM,
'm': ar.MEEM,
'n': ar.NOON,
'h': ar.HEH,
'w': ar.WAW,
'y': ar.YEH,
'Y': ar.ALEF_MAKSURA,
'\'': ar.HAMZA,
'&': ar.WAW_HAMZA,
'>': ar.ALEF_HAMZA_ABOVE,
'<': ar.ALEF_HAMZA_BELOW,
'|': ar.ALEF_MADDA,
'}': ar.YEH_HAMZA,
'_': ar.TATWEEL,
'a': ar.FATHA,
'F': ar.FATHATAN,
'i': ar.KASRA,
'K': ar.KASRATAN,
'u': ar.DAMMA,
'N': ar.DAMMATAN,
'~': ar.SHADDA,
'o': ar.SUKUN,
'`': ar.MINI_ALEF,
#~ '{': ar.ALEF_WASLA
'{': ar.ALEF
}


# conversion Tablke from the tim bulwalter represetation 
# into sampa notation
t2sampa_table = { 
'A': "a:",#ALEF, 
'b': 'b', #BEH
't': 't', #TEH
'p': 'h', #TEH_MARBUTA,
'v': 'T', #THEH
'j': 'g', #JEEM,
'H': 'x',# HAH,
'x': 'X',# KHAH,
'd': 'd',# DAL,
'*': 'D',# THAL,
'r': 'r',# REH,
'z': 'z',# ZAIN,
's': 's',# SEEN,
'$': 'S',# SHEEN,
'S': "s'",# SAD,
'D': "d'",# DAD,
'T': "t'",# TAH,
'Z': "D'",# ZAH,
'E': "?'",# AIN,
'g': 'G',# GHAIN,
'f': 'f',# FEH,
'q': 'q',# QAF,
'k': 'k',# KAF,
'l': 'l',# LAM,
'm': 'm',# MEEM,
'n': 'n',# NOON,
'h': 'h',# HEH,
'w': 'w',# WAW,
'y': 'j',# YEH,
'Y':  ':',#ALEF_MAKSURA,
'\'': '?',# HAMZA,
'&': '?',# WAW_HAMZA,
'>': '?',# ALEF_HAMZA_ABOVE,
'<': '?',# ALEF_HAMZA_BELOW,
'|': '?a:',# ALEF_MADDA,
'}': '?',# YEH_HAMZA,
'_': '',# '',#TATWEEL,
'a': 'a',# FATHA,
'F': 'an',# FATHATAN,
'i': 'i',# KASRA,
'K': 'in',# KASRATAN,
'u': 'u',# DAMMA,
'N': 'un',# DAMMATAN,
'~': ar.SHADDA,
'o': '',# SUKUN,
'`': 'a:', #MINI_ALEF,
'{': '',#ALEF_WASLA, 
}

a2t_table = {v: k for k, v in t2a_table.iteritems()}
# correct case
a2t_table[ar.ALEF] = 'A'

def tim2utf8(s):
    "Tranliteration to UTF-8 conversion of a string"
    mystr = u''
    for mychar in s:
        mystr += t2a_table.get(mychar, mychar);
    return mystr
    
def utf82tim(s):
    "Tranliteration to Tim Buckwalter conversion of a string"
    mystr = u''
    for mychar in s:
        mystr += a2t_table.get(mychar, mychar);
    return mystr

def convertShadda(word, shadda='~'):
    if word[0]==shadda:
        # to avoid that shadda is present in the begining   
        word=word[1:]
    while shadda in word:
        i= word.index(shadda);
        if i-1>=0:
            # replace the letter before shadda to double
            #replace the first one only
            word=word.replace(shadda,word[i-1],1)
    return word;

def tim2sampa(s):
    """Tranliteration to SAMPA code phonemes conversion of a string
    We suppose that all words are full vocalized.
    We convert according to t2s table,
    and the shadda is converted to double letter
    """
    mystr = u''
    # convert shadda 
    # the conversion is made before translatiration,
    # to avoid errors on phonems which have two letters as s[ or gH
    s = convertShadda(s);   
    for mychar in s:
        mystr += t2sampa_table.get(mychar, mychar);

    #convert waw and yeh after damma and kasra
    mystr = re.sub('(?<=u)w',':',mystr);
    mystr = re.sub('(?<=i)j',':',mystr);
    return mystr
def convert(text, code_from, code_to):
    """
    convert text from code_from to code_to
    
    """
    code1 = code_from.lower()
    code2 = code_to.lower()
    if code1 in ('utf', 'utf8', 'arabic'):
        if code2 in ("tim", "buckwalter"):
            return utf82tim(text)
        #~ elif code2 == 'sampa':
            #~ return tim2sampa(text)
        else: 
            return text

    if code1 in ("tim", "buckwalter"):
        if code2 in ('utf', 'utf8', 'arabic'):
            return tim2utf8(text)
        elif code2 == 'sampa':
            return tim2sampa(text)
        else: 
            return text
    
    
    
    
    
if __name__ == '__main__':
    
    words =u"""qulo
>aEuw*u
bi
rab~i
{l
n~aAsi
maliki
{l
n~aAsi
<ila`hi
{l
n~aAsi
min
$ar~i
{lo
wasowaAsi
{lo
xan~aAsi
{l~a*iY
yuwasowisu
fiY
Suduwri
{l
n~aAsi
mina
{lo
jin~api
wa
{l
n~aAsi""".split('\n')
    for word in words:
        arabic = tim2utf8(word)
        timu   = utf82tim(arabic)
        sampa  = tim2sampa(word)
        arabic2 = convert(word, 'tim','utf')
        timu2   = convert(arabic2, 'utf','tim')#utf82tim(arabic)
        sampa2  = convert(word, 'tim','sampa')#tim2sampa(word)
        print(u'\t'.join([word, arabic, timu, sampa , arabic2, timu2, sampa2 , str(timu==word), str(arabic2==arabic), str(timu2==timu), str(sampa2==sampa) ]).encode('utf8'))
        #~ print(u'\t'.join([word, tim2sampa(word)]).encode('utf8'))
        
    utf2tim_table = {v: k for k, v in t2a_table.iteritems()}
    print(utf2tim_table)
