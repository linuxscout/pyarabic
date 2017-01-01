#!/usr/bin/python2
# -*- coding=utf-8 -*-
#---
#
# ------------
# Description:
# ------------
#
# Arabic codes
#
# (C) Copyright 2010, Taha Zerrouki
# -----------------
#  $Date: 2010/03/01
#  $Author: Taha Zerrouki$
#  $Revision: 0.1 $
#  This program is written under the Gnu Public License.
#
"""
Arabic module
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Arabtechies, Arabeyes,  Taha Zerrouki
@license: GPL
@date:2010/03/01
@version: 0.1
"""
import re
from stack import *
#class araby:
"""
the arabic chars contains all arabic letters, a sub class of unicode,
"""

COMMA            = u'\u060C'
SEMICOLON        = u'\u061B'
QUESTION         = u'\u061F'
HAMZA            = u'\u0621'
ALEF_MADDA       = u'\u0622'
ALEF_HAMZA_ABOVE = u'\u0623'
WAW_HAMZA        = u'\u0624'
ALEF_HAMZA_BELOW = u'\u0625'
YEH_HAMZA        = u'\u0626'
ALEF             = u'\u0627'
BEH              = u'\u0628'
TEH_MARBUTA      = u'\u0629'
TEH              = u'\u062a'
THEH             = u'\u062b'
JEEM             = u'\u062c'
HAH              = u'\u062d'
KHAH             = u'\u062e'
DAL              = u'\u062f'
THAL             = u'\u0630'
REH              = u'\u0631'
ZAIN             = u'\u0632'
SEEN             = u'\u0633'
SHEEN            = u'\u0634'
SAD              = u'\u0635'
DAD              = u'\u0636'
TAH              = u'\u0637'
ZAH              = u'\u0638'
AIN              = u'\u0639'
GHAIN            = u'\u063a'
TATWEEL          = u'\u0640'
FEH              = u'\u0641'
QAF              = u'\u0642'
KAF              = u'\u0643'
LAM              = u'\u0644'
MEEM             = u'\u0645'
NOON             = u'\u0646'
HEH              = u'\u0647'
WAW              = u'\u0648'
ALEF_MAKSURA     = u'\u0649'
YEH              = u'\u064a'
MADDA_ABOVE      = u'\u0653'
HAMZA_ABOVE      = u'\u0654'
HAMZA_BELOW      = u'\u0655'
ZERO             = u'\u0660'
ONE              = u'\u0661'
TWO              = u'\u0662'
THREE            = u'\u0663'
FOUR             = u'\u0664'
FIVE             = u'\u0665'
SIX              = u'\u0666'
SEVEN            = u'\u0667'
EIGHT            = u'\u0668'
NINE             = u'\u0669'
PERCENT          = u'\u066a'
DECIMAL          = u'\u066b'
THOUSANDS        = u'\u066c'
STAR             = u'\u066d'
MINI_ALEF        = u'\u0670'
ALEF_WASLA       = u'\u0671'
FULL_STOP        = u'\u06d4'
BYTE_ORDER_MARK  = u'\ufeff'

# Diacritics
FATHATAN         = u'\u064b'
DAMMATAN         = u'\u064c'
KASRATAN         = u'\u064d'
FATHA            = u'\u064e'
DAMMA            = u'\u064f'
KASRA            = u'\u0650'
SHADDA           = u'\u0651'
SUKUN            = u'\u0652'

# Small Letters
SMALL_ALEF      =u"\u0670"
SMALL_WAW       =u"\u06E5"
SMALL_YEH       =u"\u06E6"
#Ligatures
LAM_ALEF                    =u'\ufefb'
LAM_ALEF_HAMZA_ABOVE        =u'\ufef7'
LAM_ALEF_HAMZA_BELOW        =u'\ufef9'
LAM_ALEF_MADDA_ABOVE        =u'\ufef5'
simple_LAM_ALEF             =u'\u0644\u0627'
simple_LAM_ALEF_HAMZA_ABOVE =u'\u0644\u0623'
simple_LAM_ALEF_HAMZA_BELOW =u'\u0644\u0625'
simple_LAM_ALEF_MADDA_ABOVE =u'\u0644\u0622'
# groups
LETTERS=u''.join([
        ALEF , BEH , TEH  , TEH_MARBUTA  , THEH  , JEEM  , HAH , KHAH ,
        DAL   , THAL  , REH   , ZAIN  , SEEN   , SHEEN  , SAD , DAD , TAH   , ZAH   ,
        AIN   , GHAIN   , FEH  , QAF , KAF , LAM , MEEM , NOON, HEH , WAW, YEH  ,
        HAMZA  ,  ALEF_MADDA , ALEF_HAMZA_ABOVE , WAW_HAMZA   , ALEF_HAMZA_BELOW  , YEH_HAMZA  ,
        ])

TASHKEEL =(FATHATAN, DAMMATAN, KASRATAN,
            FATHA,DAMMA,KASRA,
            SUKUN,
            SHADDA);
HARAKAT =(  FATHATAN,   DAMMATAN,   KASRATAN,
            FATHA,  DAMMA,  KASRA,
            SUKUN
            );
SHORTHARAKAT =( FATHA,  DAMMA,  KASRA, SUKUN);

TANWIN =(FATHATAN,  DAMMATAN,   KASRATAN);

NOT_DEF_HARAKA = TATWEEL
LIGUATURES=(
            LAM_ALEF,
            LAM_ALEF_HAMZA_ABOVE,
            LAM_ALEF_HAMZA_BELOW,
            LAM_ALEF_MADDA_ABOVE,
            );
HAMZAT=(
            HAMZA,
            WAW_HAMZA,
            YEH_HAMZA,
            HAMZA_ABOVE,
            HAMZA_BELOW,
            ALEF_HAMZA_BELOW,
            ALEF_HAMZA_ABOVE,
            );
ALEFAT=(
            ALEF,
            ALEF_MADDA,
            ALEF_HAMZA_ABOVE,
            ALEF_HAMZA_BELOW,
            ALEF_WASLA,
            ALEF_MAKSURA,
            SMALL_ALEF,

        );
WEAK   = ( ALEF, WAW, YEH, ALEF_MAKSURA);
YEHLIKE= ( YEH,  YEH_HAMZA,  ALEF_MAKSURA,   SMALL_YEH  );

WAWLIKE     =   ( WAW,  WAW_HAMZA,  SMALL_WAW );
TEHLIKE     =   ( TEH,  TEH_MARBUTA );

SMALL   =( SMALL_ALEF, SMALL_WAW, SMALL_YEH)
MOON =(HAMZA            ,
        ALEF_MADDA       ,
        ALEF_HAMZA_ABOVE ,
        ALEF_HAMZA_BELOW ,
        ALEF             ,
        BEH              ,
        JEEM             ,
        HAH              ,
        KHAH             ,
        AIN              ,
        GHAIN            ,
        FEH              ,
        QAF              ,
        KAF              ,
        MEEM             ,
        HEH              ,
        WAW              ,
        YEH
    );
SUN=(
        TEH              ,
        THEH             ,
        DAL              ,
        THAL             ,
        REH              ,
        ZAIN             ,
        SEEN             ,
        SHEEN            ,
        SAD              ,
        DAD              ,
        TAH              ,
        ZAH              ,
        LAM              ,
        NOON             ,
    );
AlphabeticOrder={
                ALEF             : 1,
                BEH              : 2,
                TEH              : 3,
                TEH_MARBUTA      : 3,
                THEH             : 4,
                JEEM             : 5,
                HAH              : 6,
                KHAH             : 7,
                DAL              : 8,
                THAL             : 9,
                REH              : 10,
                ZAIN             : 11,
                SEEN             : 12,
                SHEEN            : 13,
                SAD              : 14,
                DAD              : 15,
                TAH              : 16,
                ZAH              : 17,
                AIN              : 18,
                GHAIN            : 19,
                FEH              : 20,
                QAF              : 21,
                KAF              : 22,
                LAM              : 23,
                MEEM             : 24,
                NOON             : 25,
                HEH              : 26,
                WAW              : 27,
                YEH              : 28,
                HAMZA            : 29,

                ALEF_MADDA       : 29,
                ALEF_HAMZA_ABOVE : 29,
                WAW_HAMZA        : 29,
                ALEF_HAMZA_BELOW : 29,
                YEH_HAMZA        : 29,
                }
NAMES ={
                ALEF             :  u"ألف",
                BEH              : u"باء",
                TEH              : u'تاء' ,
                TEH_MARBUTA      : u'تاء مربوطة' ,
                THEH             : u'ثاء' ,
                JEEM             : u'جيم' ,
                HAH              : u'حاء' ,
                KHAH             : u'خاء' ,
                DAL              : u'دال' ,
                THAL             : u'ذال' ,
                REH              : u'راء' ,
                ZAIN             : u'زاي' ,
                SEEN             : u'سين' ,
                SHEEN            : u'شين' ,
                SAD              : u'صاد' ,
                DAD              : u'ضاد' ,
                TAH              : u'طاء' ,
                ZAH              : u'ظاء' ,
                AIN              : u'عين' ,
                GHAIN            : u'غين' ,
                FEH              : u'فاء' ,
                QAF              : u'قاف' ,
                KAF              : u'كاف' ,
                LAM              : u'لام' ,
                MEEM             : u'ميم' ,
                NOON             : u'نون' ,
                HEH              : u'هاء' ,
                WAW              : u'واو' ,
                YEH              : u'ياء' ,
                HAMZA            : u'همزة' ,

                TATWEEL          : u'تطويل' ,
                ALEF_MADDA       : u'ألف ممدودة' ,
                ALEF_MAKSURA      : u'ألف مقصورة' ,
                ALEF_HAMZA_ABOVE : u'همزة على الألف' ,
                WAW_HAMZA        : u'همزة على الواو' ,
                ALEF_HAMZA_BELOW : u'همزة تحت الألف' ,
                YEH_HAMZA        : u'همزة على الياء' ,
                FATHATAN         : u'فتحتان',
                DAMMATAN         : u'ضمتان',
                KASRATAN         : u'كسرتان',
                FATHA            : u'فتحة',
                DAMMA            : u'ضمة',
                KASRA            : u'كسرة',
                SHADDA           : u'شدة',
                SUKUN            : u'سكون',
                }

# regular expretion

HARAKAT_pattern =re.compile(ur"["+u"".join(HARAKAT)+u"]", re.UNICODE)
""" pattern to strip Harakat"""
LASTHARAKA_pattern =re.compile(ur"["+u"".join(HARAKAT)+u"]$|["+u''.join(TANWIN)+"]", re.UNICODE)
""" Pattern to strip only the last haraka """
SHORTHARAKAT_pattern =re.compile(ur"["+u"".join(SHORTHARAKAT)+u"]", re.UNICODE)
""" Pattern to lookup Short Harakat (Fatha,Damma, Kasra, sukun, tanwin), but not shadda"""
TASHKEEL_pattern =re.compile(ur"["+u"".join(TASHKEEL)+u"]", re.UNICODE)
""" Harakat and shadda pattern  """
HAMZAT_pattern =re.compile(ur"["+u"".join(HAMZAT)+u"]", re.UNICODE);
""" all hamzat pattern"""
ALEFAT_pattern =re.compile(ur"["+u"".join(ALEFAT)+u"]", re.UNICODE);
""" all alef like letters """
LIGUATURES_pattern =re.compile(ur"["+u"".join(LIGUATURES)+u"]", re.UNICODE);
""" all liguatures pattern """
TOKEN_pattern=re.compile(u"[^\w\u064b-\u0652']+",re.UNICODE);
""" pattern to tokenize a text"""
################################################
#{ is letter functions
################################################
def isSukun(archar):
    """Checks for Arabic Sukun Mark.
    @param archar: arabic unicode char
    @type archar: unicode
    """
    return  archar==SUKUN;
        #return True;
	#    else: return False;

def isShadda(archar):
    """Checks for Arabic Shadda Mark.
    @param archar: arabic unicode char
    @type archar: unicode
    """
    return archar==SHADDA;
    #    return True;
    #else: return False;

def isTatweel(archar):
    """Checks for Arabic Tatweel letter modifier.
    @param archar: arabic unicode char
    @type archar: unicode
    """
    if archar==TATWEEL:
        return True;
    else: return False;
def isTanwin(archar):
    """Checks for Arabic Tanwin Marks (FATHATAN, DAMMATAN, KASRATAN).
    @param archar: arabic unicode char
    @type archar: unicode
    """
    if archar in TANWIN:
        return True;
    else: return False;

def isTashkeel(archar):
    """Checks for Arabic Tashkeel Marks (FATHA,DAMMA,KASRA, SUKUN, SHADDA, FATHATAN,DAMMATAN, KASRATAn).
    @param archar: arabic unicode char
    @type archar: unicode
    """
    if  archar in  TASHKEEL:
        return True;
    else: return False;

def isHaraka(archar):
    """Checks for Arabic Harakat Marks (FATHA,DAMMA,KASRA,SUKUN,TANWIN).
    @param archar: arabic unicode char
    @type archar: unicode
    """
    return archar in HARAKAT;


def isShortharaka(archar):
    """Checks for Arabic  short Harakat Marks (FATHA,DAMMA,KASRA,SUKUN).
    @param archar: arabic unicode char
    @type archar: unicode
    """
	
    return archar in SHORTHARAKAT;


def isLigature(archar):
    """Checks for Arabic  Ligatures like LamAlef.
    (LAM_ALEF, LAM_ALEF_HAMZA_ABOVE, LAM_ALEF_HAMZA_BELOW, LAM_ALEF_MADDA_ABOVE)
    @param archar: arabic unicode char
    @type archar: unicode
    """
    return  archar in LIGUATURES;

def isHamza(archar):
    """Checks for Arabic  Hamza forms.
    HAMZAT are (HAMZA, WAW_HAMZA, YEH_HAMZA, HAMZA_ABOVE, HAMZA_BELOW,ALEF_HAMZA_BELOW, ALEF_HAMZA_ABOVE )
    @param archar: arabic unicode char
    @type archar: unicode
    """
    return archar in HAMZAT;

def isAlef(archar):
    """Checks for Arabic Alef forms.
    ALEFAT=(ALEF, ALEF_MADDA, ALEF_HAMZA_ABOVE, ALEF_HAMZA_BELOW,ALEF_WASLA, ALEF_MAKSURA );
    @param archar: arabic unicode char
    @type archar: unicode
    """
    return archar in ALEFAT;

def isYehlike(archar):
    """Checks for Arabic Yeh forms.
    Yeh forms : YEH, YEH_HAMZA, SMALL_YEH, ALEF_MAKSURA
    @param archar: arabic unicode char
    @type archar: unicode
    """
    if archar in YEHLIKE:
        return True;
    else: return False;

def isWawlike(archar):
    """Checks for Arabic Waw like forms.
    Waw forms : WAW, WAW_HAMZA, SMALL_WAW
    @param archar: arabic unicode char
    @type archar: unicode
    """
    if archar in WAWLIKE:
        return True;
    else: return False;

def isTeh(archar):
    """Checks for Arabic Teh forms.
    Teh forms : TEH, TEH_MARBUTA
    @param archar: arabic unicode char
    @type archar: unicode
    """
    if archar in TEHLIKE:
        return True;
    else: return False;
def isSmall(archar):
    """Checks for Arabic Small letters.
    SMALL Letters : SMALL ALEF, SMALL WAW, SMALL YEH
    @param archar: arabic unicode char
    @type archar: unicode
    """
    if archar in SMALL:
        return True;
    else: return False;

def isWeak(archar):
    """Checks for Arabic Weak letters.
    Weak Letters : ALEF, WAW, YEH, ALEF_MAKSURA
    @param archar: arabic unicode char
    @type archar: unicode
    """
    if archar in WEAK:
        return True;
    else: return False;

def isMoon(archar):
    """Checks for Arabic Moon letters.
    Moon Letters :
    @param archar: arabic unicode char
    @type archar: unicode
    """

    if archar in MOON:
        return True;
    else: return False;

def isSun(archar):
    """Checks for Arabic Sun letters.
    Moon Letters :
    @param archar: arabic unicode char
    @type archar: unicode
    """
    if archar in SUN:
        return True;
    else: return False;
#####################################
#{ general  letter functions
#####################################
def order(archar):
    """return Arabic letter order between 1 and 29.
    Alef order is 1, Yeh is 28, Hamza is 29.
    Teh Marbuta has the same ordre with Teh, 3.
    @param archar: arabic unicode char
    @type archar: unicode
    @return: arabic order.
    @rtype: integer;
    """
    if AlphabeticOrder.has_key(archar):
        return AlphabeticOrder[archar];
    else: return 0;

def name(archar):
    """return Arabic letter name in arabic.
    Alef order is 1, Yeh is 28, Hamza is 29.
    Teh Marbuta has the same ordre with Teh, 3.
    @param archar: arabic unicode char
    @type archar: unicode
    @return: arabic name.
    @rtype: unicode;
    """
    if NAMES.has_key(archar):
        return NAMES[archar];
    else:
        return u'';

def arabicrange(self):
    """return a list of arabic characteres .
    Return a list of characteres between \u060c to \u0652
    @return: list of arabic characteres.
    @rtype: unicode;
    """
    mylist=[];
    for i in range(0x0600, 0x00653):
        try :
            mylist.append(unichr(i));
        except ValueError:
            pass;
    return mylist;


#####################################
#{ Has letter functions
#####################################
def hasShadda(word):
    """Checks if the arabic word  contains shadda.
    @param word: arabic unicode char
    @type word: unicode
    """
    if re.search(SHADDA,word):
        return True;
    else:
        return False;

#####################################
#{ word and text functions
#####################################
def isVocalized(word):
    """Checks if the arabic word is vocalized.
    the word musn't  have any spaces and pounctuations.
    @param word: arabic unicode char
    @type word: unicode
    """
    if word.isalpha(): return False;
#        n (FATHA,DAMMAN,KASRA):
    else:
        if re.search(HARAKAT_pattern,word):
            return True;
        else:
            return False;
def isVocalizedtext(text):
    """Checks if the arabic text is vocalized.
    The text can contain many words and spaces
    @param text: arabic unicode char
    @type text: unicode
    """
    if re.search(HARAKAT_pattern,text):
        return True;
    else:
        return False;
def isArabicstring(text):
    """ Checks for an  Arabic standard Unicode block characters;
    An arabic string can contain spaces, digits and pounctuation.
    but only arabic standard characters, not extended arabic
    @param text: input text
    @type text: unicode
    @return: True if all charaters are in Arabic block
    @rtype: Boolean
    """
    if re.search(u"([^\u0600-\u0652%s%s%s\s\d])"%(LAM_ALEF, LAM_ALEF_HAMZA_ABOVE,LAM_ALEF_MADDA_ABOVE),text):
        return False;
    return True;

def isArabicrange(text):
    """ Checks for an  Arabic Unicode block characters;
    @param text: input text
    @type text: unicode
    @return: True if all charaters are in Arabic block
    @rtype: Boolean
    """
    if re.search(u"([^\u0600-\u06ff\ufb50-\ufdff\ufe70-\ufeff\u0750-\u077f])",text):
        return False;
    return True;

def isArabicword(word):
    """ Checks for an valid Arabic  word.
    An Arabic word not contains spaces, digits and pounctuation
    avoid some spelling error,  TEH_MARBUTA must be at the end.
    @param word: input word
    @type word: unicode
    @return: True if all charaters are in Arabic block
    @rtype: Boolean
    """
    if len(word)==0 : return False;
    elif re.search(u"([^\u0600-\u0652%s%s%s])"%(LAM_ALEF, LAM_ALEF_HAMZA_ABOVE,LAM_ALEF_MADDA_ABOVE),word):
        return False;
    elif isHaraka(word[0]) or word[0] in (WAW_HAMZA,YEH_HAMZA):
        return False;
#  if Teh Marbuta or Alef_Maksura not in the end
    elif re.match(u"^(.)*[%s](.)+$"%ALEF_MAKSURA,word):
        return False;
    elif re.match(u"^(.)*[%s]([^%s%s%s])(.)+$"%(TEH_MARBUTA,DAMMA,KASRA,FATHA),word):
        return False;
    else:
        return True;
#####################################
#{Char functions
#####################################
def firstChar(word):
	"""
	Return the first char
	@param word: given word;
	@type word: unicode;
	@return: the first char
	@rtype: unicode char;
	"""
	return word[0];
def secondChar(word):
	"""
	Return the second char
	@param word: given word;
	@type word: unicode;
	@return: the first char
	@rtype: unicode char;
	"""
	return word[1:2];	
def lastChar(word):
	"""
	Return the last letter
	example: zerrouki; 'i' is the last.	
	@param word: given word;
	@type word: unicode;
	@return: the last letter
	@rtype: unicode char;
	"""
	return word[-1:];
def secondlastChar(word):
	"""
	Return the second last letter
	example: zerrouki; 'k' is the second last.
	@param word: given word;
	@type word: unicode;
	@return: the second last letter
	@rtype: unicode char;
	"""
	return word[-2:-1]
#####################################
#{Strip functions
#####################################
def stripHarakat(text):
	"""Strip Harakat from arabic word except Shadda.
	The striped marks are :
		- FATHA, DAMMA, KASRA
		- SUKUN
		- FATHATAN, DAMMATAN, KASRATAN, , , .
	Example:
		>>> text=u"الْعَرَبِيّةُ"
		>>> stripTashkeel(text)
		العربيّة

	@param text: arabic text.
	@type text: unicode.
	@return: return a striped text.
	@rtype: unicode.
	"""
	if text:
		return  re.sub(HARAKAT_pattern,u'',text)
	return text;
def stripLastHaraka(text):
	"""Strip the last Haraka from arabic word except Shadda.
	The striped marks are :
		- FATHA, DAMMA, KASRA
		- SUKUN
		- FATHATAN, DAMMATAN, KASRATAN, , , .
	Example:
		>>> text=u"الْعَرَبِيّةُ"
		>>> stripTashkeel(text)
		الْعَرَبِيّة

	@param text: arabic text.
	@type text: unicode.
	@return: return a striped text.
	@rtype: unicode.
	"""
	if text:
		return  re.sub(LASTHARAKA_pattern,u'',text)
	return text;

def stripTashkeel(text):
	"""Strip vowels from a text, include Shadda.
	The striped marks are :
		- FATHA, DAMMA, KASRA
		- SUKUN
		- SHADDA
		- FATHATAN, DAMMATAN, KASRATAN, , , .
	Example:
		>>> text=u"الْعَرَبِيّةُ"
		>>> stripTashkeel(text)
		العربية

	@param text: arabic text.
	@type text: unicode.
	@return: return a striped text.
	@rtype: unicode.
	"""
	if text:
		return re.sub(TASHKEEL_pattern,'',text);
	return text;

def stripTatweel(text):
	"""
	Strip tatweel from a text and return a result text.

	Example:
		>>> text=u"العـــــربية"
		>>> stripTatweel(text)
		العربية

	@param text: arabic text.
	@type text: unicode.
	@return: return a striped text.
	@rtype: unicode.
	"""
	return text.replace(TATWEEL,'');

def stripShadda(text):
	"""
	Strip Shadda from a text and return a result text.

	Example:
		>>> text=u"الشّمسيّة"
		>>> stripTatweel(text)
		الشمسية

	@param text: arabic text.
	@type text: unicode.
	@return: return a striped text.
	@rtype: unicode.
	"""
	return text.replace(SHADDA,'');

def normalizeLigature(text):
	"""Normalize Lam Alef ligatures into two letters (LAM and ALEF), and Tand return a result text.
	Some systems present lamAlef ligature as a single letter, this function convert it into two letters,
	The converted letters into  LAM and ALEF are :
		- LAM_ALEF, LAM_ALEF_HAMZA_ABOVE, LAM_ALEF_HAMZA_BELOW, LAM_ALEF_MADDA_ABOVE

	Example:
		>>> text=u"لانها لالء الاسلام"
		>>> normalizeLigature(text)
		لانها لالئ الاسلام

	@param text: arabic text.
	@type text: unicode.
	@return: return a converted text.
	@rtype: unicode.
	"""
	if text:
		return LIGUATURES_pattern.sub(u'%s%s'%(LAM,ALEF), text)
	return text;
def normalizeHamza(word):
	"""Standardize the Hamzat into one form of hamza,
	replace Madda by hamza and alef.
	Replace the LamAlefs by simplified letters.
	Example:
		>>> text=u"سئل أحد الأئمة"
		>>> normalizeHamza(text)
		سءل ءحد الءءمة

	@param word: arabic text.
	@type word: unicode.
	@return: return a converted text.
	@rtype: unicode.
	"""
	HAMZAT= u"إأءئؤ";
	if word.startswith(ALEF_MADDA):
	   if len(word)>=3 and (word[1] not in HARAKAT) and (word[2]==SHADDA or len(word)==3):
			word=HAMZA+ALEF+word[1:];
	   else:
			word=HAMZA+HAMZA+word[1:];
	# convert all Hamza from into one form
	word=word.replace(ALEF_MADDA,HAMZA+HAMZA);
	word=HAMZAT_pattern.sub(HAMZA,word);

	return word;



def separate(word, ExtractShadda=False):
	"""
	separate the letters from the vowels, in arabic word,
	if a letter hasn't a haraka, the not definited haraka is attributed.
	return ( letters,vowels);
	"""
	#debug=True;
	stack1=Stack(word)
	# the word is inversed in the stack 
	stack1.items.reverse();
	letters=Stack()
	marks=Stack()	
	vowels=HARAKAT
	last1=stack1.pop();
	# if the last element must be a letter,
	# the arabic word can't starts with a haraka
	# in th stack the word is inversed
	while last1 in vowels: last1=stack1.pop();
	while  last1!=None:
		if last1 in vowels:
			# we can't have two harakats beside.
			# the shadda is considered as a letter
			marks.pop();
			marks.push(last1);
		elif last1==SHADDA:
			# is the element is a Shadda,
			# the previous letter must have a sukun as mark, 
			# and the shadda take the indefinate  mark
			marks.pop();
			marks.push(SUKUN);
			marks.push(NOT_DEF_HARAKA);
			letters.push(SHADDA);
		else:
			marks.push(NOT_DEF_HARAKA);
			letters.push(last1);
		last1=stack1.pop();
	if ExtractShadda:
		# the shadda is considered as letter
		wordletters =	u''.join(letters.items)
		# print wordletters.encode('utf8')
		shaddaPlaces = re.sub(ur'[^%s]'%SHADDA, TATWEEL,wordletters)
		shaddaPlaces = re.sub(u'%s%s'%(TATWEEL,SHADDA),SHADDA, shaddaPlaces); 
		# print wordletters.encode('utf8')		
		wordletters = stripShadda(wordletters);
		# print wordletters.encode('utf8')		
		return (wordletters,u''.join(marks.items), shaddaPlaces)
	else:
		return (u''.join(letters.items),u''.join(marks.items))



def joint(letters, marks):
	"""
	joint the letters with the marks
	the length ot letters and marks must be equal 
	return word;
	"""
	#debug=True;
	debug=False;

	# The length ot letters and marks must be equal 
	if len(letters)!=len(marks): return "";

	stackLetter=Stack(letters)
	stackLetter.items.reverse();
	stackMark=Stack(marks)
	stackMark.items.reverse();

	wordStack=Stack();
	lastLetter=stackLetter.pop();
	lastMark=stackMark.pop();


	vowels=HARAKAT
	while  lastLetter!=None and  lastMark!=None:
		if lastLetter == SHADDA:
			top=wordStack.pop();
			if top not in vowels:
				wordStack.push(top);
			wordStack.push(lastLetter);
			if lastMark!= NOT_DEF_HARAKA:
				wordStack.push(lastMark);
		else:
			wordStack.push(lastLetter);

			if lastMark!= NOT_DEF_HARAKA:
				wordStack.push(lastMark);
		
		lastLetter=stackLetter.pop();
		lastMark=stackMark.pop();

	if not (stackLetter.isEmpty() and stackMark.isEmpty()):
		return False;
	else:

		return ''.join(wordStack.items);
def vocalizedlike(word1,word2):
	"""
	if the two words has the same letters and the same harakats, this fuction return True.
	The two words can be full vocalized, or partial vocalized
	"""
	if vocalizedSimilarity(word1,word2)<0:
		return False;
	else: return True;


#-------------------------
# Function def vaznlike(word1,wazn):
#-------------------------
def waznlike(word1,wazn):
	"""
	if the  word1 is like a wazn (pattern),
	the letters must be equal,
	the wazn has FEH, AIN, LAM letters.
	this are as generic letters.
	The two words can be full vocalized, or partial vocalized
	"""
	debug=False;
	stack1=Stack(word1)
	stack2=Stack(wazn)
	root=Stack()	
	last1=stack1.pop();
	last2=stack2.pop();
	if debug: print "+0", stack1, stack2;
	vowels=HARAKAT
	while  last1!=None and  last2!=None:
		if last1==last2 and last2 not in (FEH, AIN,LAM):
			if debug: print "+2", stack1.items,last1, stack2.items,last2
			last1=stack1.pop();
			last2=stack2.pop();
		elif last1 not in vowels and last2 in (FEH, AIN,LAM):
			if debug: print "+2", stack1.items,last1, stack2.items,last2
			root.push(last1);
			print "t";
			last1=stack1.pop();
			last2=stack2.pop();
		elif last1 in vowels and last2 not in vowels:
			if debug: print "+2", stack1.items,last1, stack2.items,last2
			last1=stack1.pop();
		elif last1 not in vowels and last2 in vowels:
			if debug: print "+2", stack1.items,last1, stack2.items,last2
			last2=stack2.pop();
		else:
			if debug: print "+2", stack1.items,last1, stack2.items,last2
			break;
	# reverse the root letters
	root.items.reverse();
	print " the root is ", root.items#"".join(root.items);
	if not (stack1.isEmpty() and stack2.isEmpty()):
		return False;
	else: return True;
	
def shaddalike(partial,fully):
	"""
	if the two words has the same letters and the same harakats, this fuction return True.
	The first word is partially vocalized, the second is fully
	if the partially contians a shadda, it must be at the same place in the fully 
	"""
	debug=False;
	partial=stripHarakat(partial);
	fully=stripHarakat(fully)
	Pstack=Stack(partial)
	Vstack=Stack(fully)
	Plast=Pstack.pop();
	Vlast=Vstack.pop();
	if debug: print "+0", Pstack, Vstack;
	vowels=SHADDA
	while  Plast!=None and  Vlast!=None:
		if Plast==Vlast:
			if debug: print "+2", Pstack.items,Plast, Vstack.items,Vlast
			Plast=Pstack.pop();
			Vlast=Vstack.pop();
		elif Plast ==SHADDA and Vlast !=SHADDA:
			if debug: print "+2", Pstack.items,Plast, Vstack.items,Vlast
			break;
		elif Plast !=SHADDA and Vlast ==SHADDA:
			if debug: print "+2", Pstack.items,Plast, Vstack.items,Vlast
			Vlast=Vstack.pop();
		else:
			if debug: print "+2", Pstack.items,Plast, Vstack.items,Vlast
			break;
	if not (Pstack.isEmpty() and Vstack.isEmpty()):
		return False;
	else: return True;
def reduceTashkeel(text):
	"""
	Reduce the Tashkeel, by deleting evident cases.
	@param text: the input text fully vocalized.
	@type text: unicode.
	@return : partially vocalized text.
	@rtype: unicode.
	"""
	reduced=text;
	# delete all fathat,  except on waw and yeh
	#delete all sukun, except on waw and yeh.
	reduced=re.sub(u"(?<!(%s|%s))(%s|%s)"%( WAW, YEH, SUKUN, FATHA),'',reduced);

	#delete damma if followed by waw.
	reduced=re.sub(u"%s(?=%s)"%(DAMMA, WAW),'',reduced);

	#delete kasra if followed by yeh.
	reduced=re.sub(u"%s(?=%s)"%(KASRA, YEH),'',reduced);

	#delete fatha if followed by alef to reduce yeh maftouha and waw maftouha before alef.
	reduced=re.sub(u"%s(?=%s)"%(FATHA, ALEF),'',reduced);

	#delete fatha from yeh and waw if they are in the word begining.
	reduced=re.sub(u"(?<=\s(%s|%s))%s"%(WAW, YEH, FATHA),'',reduced);
	reduced=re.sub(u"(?<=\A(%s|%s))%s"%(WAW, YEH, FATHA),'',reduced);
	
	#delete kasra if preceded by Hamza below alef.
	reduced=re.sub(u"(?<=%s)%s"%(ALEF_HAMZA_BELOW,KASRA),'',reduced);

	return reduced;

def vocalizedSimilarity(word1,word2):
	"""
	if the two words has the same letters and the same harakats, this fuction return True.
	The two words can be full vocalized, or partial vocalized
	"""
	debug=False;
	stack1=Stack(word1)
	stack2=Stack(word2)
	last1=stack1.pop();
	last2=stack2.pop();
	errCount=0;
	if debug: print "+0", stack1, stack2;
	vowels=HARAKAT
	while  last1!=None and  last2!=None:
		if last1==last2:
			if debug: print u"\t".join(["0", u"".join(stack1.items),last1, u''.join(stack2.items),last2]).encode('utf8');
			last1=stack1.pop();
			last2=stack2.pop();
		elif last1 in vowels and last2 not in vowels:
			if debug: print u"\t".join(["1", u"".join(stack1.items),last1, u''.join(stack2.items),last2]).encode('utf8');
			last1=stack1.pop();
		elif last1 not in vowels and last2 in vowels:
			if debug: print u"\t".join(["2", u"".join(stack1.items),last1, u''.join(stack2.items),last2]).encode('utf8');
			last2=stack2.pop();
		else:
			if debug: print u"\t".join(["3", u"".join(stack1.items),last1, u''.join(stack2.items),last2]).encode('utf8');
			#break;
			if last1==SHADDA:
				last1=stack1.pop();
			elif last2==SHADDA: 
				last2=stack2.pop();
			else:
				last1=stack1.pop();
				last2=stack2.pop();
			errCount+=1;
	if errCount>0:#not (stack1.isEmpty() and stack2.isEmpty()):
		return -errCount;#False;
	else: return True;
def evidentTashkeel(word):
	"""
	Vocalize evident cases of word, some sequences of letters have evident vocalization; like any letter before Teh marbuta is maftouh
	
	@param word: word to be vocalized by evident cases. 
	@type word: 
	"""
	pass;

def tokenize(text=u""):
	"""
	Tokenize Arabic text into words
	@param text the input text.
	@type text: unicode.
	@return: list of words.
	@rtype: list.
	"""

	if text==u'':
		return [];
	else:
		mylist= TOKEN_pattern.split(text)
		if u'' in mylist: mylist.remove(u'');
		return mylist;



if __name__=="__main__":
	# word=u"عاليًا"
	# print stripLastHaraka(word).encode('utf8');
	# wordtuples=[
	# (u'العربية', u'اَلْعَرَبِيَّةُ'),
	# (u'العربية', u'اَلْعَرَبِيَةُ'),
	# (u'العربيةَ', u'اَلْعَرَبِيَةُ'),
	# (u'اَلْعَرْبِيَةِ', u'اَلْعَرَبِيَةُ'),
	# (u'الدَّجاجَةُ', u'الدَّجَاجَةُ'),
	# (u' فِي السَّمَاءِ نَجُومُ لاَمِعَةً .', u'فِي السَّمَاءِ نُجُومٌ لاَمِعَةٌ .'),
	# (u'', u''),
	# (u'', u''),
		
# ];
	# debug=True;
	# for bilist  in wordtuples:
		# print u"\t".join([bilist[0], bilist[1], str(vocalizedSimilarity(bilist[0], bilist[1])) ]).encode('utf8');
	words=[u'الْدَرَاجَةُ',
u'الدّرّاجة',
u'سّلّامْ',
	]
	for word in words:
		l,m,s=separate(word,True);
		print u'\t'.join([word, l,m,s]).encode('utf8');
		l=joint(l,s);
		print u'\t'.join([word, l,m,s]).encode('utf8');		
		newword= joint(l,m);
		print u'\t'.join([word, newword]).encode('utf8');
	
