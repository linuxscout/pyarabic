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


a2en_table= {'ء': "2",
 'آ': 'A',
 'أ': 'A',
 'ؤ': '2',
 'إ': '2',
 'ئ': '2',
 'ا': 'A',
 'ب': 'b',
 'ة': 't',
 'ت': 't',
 'ث': 'th',
 'ج': 'j',
 'ح': 'H',
 'خ': 'kh',
 'د': 'd',
 'ذ': 'dh',
 'ر': 'r',
 'ز': 'z',
 'س': 's',
 'ش': 'sh',
 'ص': 'S',
 'ض': 'D',
 'ط': 'T',
 'ظ': 'zh',
 'ع': 'E',
 'غ': 'g',
 'ـ': '',
 'ف': 'f',
 'ق': 'q',
 'ك': 'k',
 'ل': 'l',
 'م': 'm',
 'ن': 'n',
 'ه': 'h',
 'و': 'w',
 'ى': 'a',
 'ي': 'y',
 'ً': 'an',
 'ٌ': 'un',
 'ٍ': 'in',
 'َ': 'a',
 'ُ': 'u',
 'ِ': 'i',
 'ّ': '',
 'ْ': '',
 'ٰ': 'a'}

a2t_table = {v: k for k, v in t2a_table.items()}
# correct case
a2t_table[ar.ALEF] = 'A'

if (sys.version_info > (3, 0)):
    # Python 3 code in this block
    T2D_TRANS= str.maketrans(ar.NOT_DEF_HARAKA + ar.TASHKEEL_STRING, "012345678")
    T2A_TRANS= str.maketrans(ar.NOT_DEF_HARAKA + ar.TASHKEEL_STRING, "0AUIauio3")
    D2T_TRANS= str.maketrans("012345678"  , ar.NOT_DEF_HARAKA + ar.TASHKEEL_STRING)
    A2T_TRANS= str.maketrans("0AUIauio3"  , ar.NOT_DEF_HARAKA + ar.TASHKEEL_STRING)
    # -------------- Digits Trans -------------- # 
    E2W_TRANS = str.maketrans("".join(ar.NUMBERS_EAST), "".join(ar.NUMBERS_WEST))
    E2P_TRANS = str.maketrans("".join(ar.NUMBERS_EAST), "".join(ar.NUMBERS_PERS))
    W2E_TRANS = str.maketrans("".join(ar.NUMBERS_WEST), "".join(ar.NUMBERS_EAST))
    W2P_TRANS = str.maketrans("".join(ar.NUMBERS_WEST), "".join(ar.NUMBERS_PERS))
    P2E_TRANS = str.maketrans("".join(ar.NUMBERS_PERS), "".join(ar.NUMBERS_EAST))
    P2W_TRANS = str.maketrans("".join(ar.NUMBERS_PERS), "".join(ar.NUMBERS_WEST))

    def translate(word, table):
        """ translate a word accoring to table"""
        return word.translate(table)
else:
    #~ T2D_TRANS= {ord(c): ord(t) for c, t in zip(ar.NOT_DEF_HARAKA + ar.TASHKEEL_STRING, u"012345678")}
    #~ T2A_TRANS= {ord(c): ord(t) for c, t in zip(ar.NOT_DEF_HARAKA + ar.TASHKEEL_STRING, u"0AUIauio3")}
    #~ D2T_TRANS= {ord(c): ord(t) for c, t in zip(u"012345678"  , ar.NOT_DEF_HARAKA + ar.TASHKEEL_STRING)}
    #~ A2T_TRANS= {ord(c): ord(t) for c, t in zip(u"0AUIauio3"  , ar.NOT_DEF_HARAKA + ar.TASHKEEL_STRING)}
    T2D_TRANS= {c:t for c, t in zip(ar.NOT_DEF_HARAKA + ar.TASHKEEL_STRING, u"012345678")}
    T2A_TRANS= {c:t for c, t in zip(ar.NOT_DEF_HARAKA + ar.TASHKEEL_STRING, u"0AUIauio3")}
    D2T_TRANS= {c:t for c, t in zip(u"012345678"  , ar.NOT_DEF_HARAKA + ar.TASHKEEL_STRING)}
    A2T_TRANS= {c:t for c, t in zip(u"0AUIauio3"  , ar.NOT_DEF_HARAKA + ar.TASHKEEL_STRING)}

    E2W_TRANS = {c:t for c, t in zip(ar.NUMBERS_EAST, ar.NUMBERS_WEST)}
    E2P_TRANS = {c:t for c, t in zip(ar.NUMBERS_EAST, ar.NUMBERS_PERS)}
    W2E_TRANS = {c:t for c, t in zip(ar.NUMBERS_WEST, ar.NUMBERS_EAST)}
    W2P_TRANS = {c:t for c, t in zip(ar.NUMBERS_WEST, ar.NUMBERS_PERS)}
    P2E_TRANS = {c:t for c, t in zip(ar.NUMBERS_PERS, ar.NUMBERS_EAST)}
    P2W_TRANS = {c:t for c, t in zip(ar.NUMBERS_PERS, ar.NUMBERS_WEST)}

    def translate(word, table):
        """ translate a word accoring to table"""
        mystr = u''
        for mychar in word:
            mystr += table.get(mychar, mychar);
        return mystr
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
    

def utf82latin(s):
    "Tranliteration from UTF-8  to latin with plain english no symbol"
    mystr = u''
    for mychar in s:
        mystr += a2en_table.get(mychar, mychar);
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
        elif code2 == 'sampa':
            return tim2sampa(utf82tim(text))
        elif code2 in ('latin', 'ascii'):
            return utf82latin(text)
        else: 
            return text

    if code1 in ("tim", "buckwalter"):
        if code2 in ('utf', 'utf8', 'arabic'):
            return tim2utf8(text)
        elif code2 == 'sampa':
            return tim2sampa(text)
        else: 
            return text
    
    
def segment_language(text):
    """
    Detect language
    """
    if not text: return text
    resultlist = []
    if re.search(u"[\u0600-\u06ff]", text[0]):
    #~ if re.search(u"[\u0600-\u06ff]", text):
        arabic = True
    else:
        arabic = False
    actual_text = u""
    for  k in text:
        if re.search(u"[\u0600-\u06ff]", k):
            if arabic:
                actual_text += k
            else:
                resultlist.append(('latin', actual_text))
                arabic = True
                actual_text = k
        elif re.search(u"[\s\d\?, :\!\(\)]", k):
            actual_text += k
        else:
            if arabic:
                i = len(actual_text)
                temp_text = u""
                while not re.search(u"[\u0600-\u06ff]", actual_text[i:i+1]):
                    i -= 1
                temp_text = actual_text[i+1:]
                actual_text = actual_text[:i+1]
                resultlist.append(('arabic', actual_text))
                arabic = False
                actual_text = temp_text+k
            else:
                actual_text += k
    if arabic:
        resultlist.append(('arabic', actual_text))
    else:
        resultlist.append(('latin', actual_text))
    return resultlist
    
def delimite_language(text, language = "arabic", start="<", end=">"):
    new_chunks_list = [] 
    chunks = segment_language(text)
    for (lang, chunk) in chunks:
        if lang == language:
             new_chunks_list.append("%s%s%s"%(start,chunk, end))
        else:
            new_chunks_list.append(chunk)
    return u" ".join(new_chunks_list)    


    
    
def normalize_digits(text, source='all', out='west'):
    """
    Normalize digits to and from the following writing systems:
    west:    Western Arabic numerals                (0123456789)
    east:    Eastern Arabic (Hindu-Arabic) numerals (٠١٢٣٤٥٦٧٨٩)
    persian: Persian/Urdu numerals                  (۰۱۲۳۴۵۶۷۸۹) 
    
    if `source = all`, then all digits contained in the text 
    will be normalized into `out` writing system.
    Otherwise digits written in `source` will be normalized
    without affecting the rest of the digits. 

    Example:
        >>> text = u'۰۱۲۳۴۵۶۷۸۹ ٠١٢٣٤٥٦٧٨٩ 123456789'
        >>> normalize_digits(text, source='all', out='west')
        '0123456789 0123456789 0123456789' 
        >>> normalize_digits(text, source='persian', out='west')
        >>> '0123456789 ٠١٢٣٤٥٦٧٨٩ 0123456789' 

    @param text: unnormalized text.
    @type text: unicode.
    @param source: Writing system for the digits to be normalized.
                   (default is all).
    @type source: string
    @param out: Intended writing system for source.
                (default is west)
    @return: returns a normalized text.
    @rtype: unicode.
    """
    source = source.lower()
    out = out.lower()
    assert source in ['all', 'west', 'east', 'persian'], 'Invalid option for `source`: %s' % source
    assert out in ['west', 'east', 'persian'], 'Invalid option for `out`: %s' % out
    if source == out:
        return text
    source_to_out_tbl = {
        'west': {'east': W2E_TRANS, 'persian': W2P_TRANS},
        'east': {'west': E2W_TRANS, 'persian': E2P_TRANS},
        'persian': {'west': P2W_TRANS, 'east': P2E_TRANS}
    }
    if source == 'all':
        del source_to_out_tbl[out]
        for tbl in source_to_out_tbl.values():
            text = translate(text, tbl[out])
        return text
    return translate(text, source_to_out_tbl[source][out])

def encode_tashkeel(word, method = "ascii"):
    """
    Encode word marks into decimal or Ascii string to be saved as integer
    
    Example:
        >>> import pyarabic.trans
        >>> word1 = u"هَارِبًا"
        >>> pyarabic.trans.encode_tashkeel(word1)
        ('هاربا', 'a0iA0')
        >>> pyarabic.trans.encode_tashkeel(word1, "decimal")
        ('هاربا', 40610)
        >>> letters = u"هاربا" 
        >>> encoded_marks = u"a0iA0"
        >>> pyarabic.trans.decode_tashkeel(letters, encoded_marks)
        'هَارِبًا'
        >>> letters = u"هاربا" 
        >>> encoded_marks = 40610
        >>> pyarabic.trans.decode_tashkeel(letters, encoded_marks, "decimal")
        'هَارِبًا'


    @input word: diacritized arabic diacritcs
    @type word: unicode
    @return:  (letters, encoded) zero if fails
    @rtype: (letters, encoded) ttring/ integer
    """
    letters, marks = ar.separate(word)

    if method == "decimal":
        transed = translate(marks, T2D_TRANS)
    elif method == "ascii":
        transed = translate(marks, T2A_TRANS)
    else:
        transed = translate(marks, T2A_TRANS)


    if method == "decimal":
        try:
            transed = int(transed)
        except:
            return word, ""
    return letters, transed



def decode_tashkeel(word, marks, method = "ascii"):
    """ decode tashkeel"""
    """
    decode marks from decimal/ascii string to be joint on word
    @input word: undiacritized arabic diacritcs
    @type word: unicode
    @input marks: encoded marks
    @type marks: unicode/integer
    @return:  diacritized word
    @rtype: unicode
    """
    if type(marks) != (str):
        marks = str(marks)
    # zeros can be removed in int code, then we must add them to left
    marks = marks.rjust(len(word),str("0"))
    if method == "decimal":
        transed = translate(marks, D2T_TRANS)
    elif method == "ascii":
        transed = translate(marks, A2T_TRANS)
    else:
        transed = translate(marks, A2T_TRANS)        
    word2 = ar.joint(word, transed)
    return word2    
    
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
        
    utf2tim_table = {v: k for k, v in t2a_table.items()}
    print(utf2tim_table)
    
    from arabrepr import arepr
    # test detect language
    text =u"""السلام عليكم how are you, لم اسمع أخبارك منذ مدة, where are you going"""
    print(arepr(segment_language(text)))
    text_out= delimite_language(text, start='\RL{', end="}")
    print(text_out.encode('utf8'))
    text_out= delimite_language(text, start="<arabic>", end="</arabic>")
    print(text_out.encode('utf8'))
