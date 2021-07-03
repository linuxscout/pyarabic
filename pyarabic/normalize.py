#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
Normalize
Utility functions used by to prepare an arabic text to search and index.
@author: Taha Zerrouki <taha_zerrouki at gmail dot com>
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Arabtechies, Arabeyes, Taha Zerrouki
@license: GPL
@date:2017/02/15
@version:0.3
"""
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
)
import re
try:
    import araby as arabconst

except:
    from . import araby as arabconst

######################################################################
#{ Indivudual Functions
######################################################################

#--------------------------------------
def strip_tashkeel(text):
    """Strip vowel from a text and return a result text.
    The striped marks are :
        - FATHA, DAMMA, KASRA
        - SUKUN
        - SHADDA
        - FATHATAN, DAMMATAN, KASRATAN, , , .
    Example:
        >>> text=u"الْعَرَبِيّةُ"
        >>> strip_tashkeel(text)
        العربية

    @param text: arabic text.
    @type text: unicode.
    @return: return a striped text.
    @rtype: unicode.
    """
    return arabconst.strip_tashkeel(text)


#strip tatweel from a text and return a result text
#--------------------------------------
def strip_tatweel(text):
    """
    Strip tatweel from a text and return a result text.

    Example:
        >>> text=u"العـــــربية"
        >>> strip_tatweel(text)
        العربية

    @param text: arabic text.
    @type text: unicode.
    @return: return a striped text.
    @rtype: unicode.
    """
    return arabconst.strip_tatweel(text)


#--------------------------------------
def normalize_hamza(text):
    """Normalize Hamza forms into one form, and return a result text.
    The converted letters are :
        - The converted lettersinto HAMZA are: WAW_HAMZA,YEH_HAMZA
        - The converted lettersinto ALEF are: ALEF_MADDA,
        ALEF_HAMZA_ABOVE, ALEF_HAMZA_BELOW ,HAMZA_ABOVE, HAMZA_BELOW

    Example:
        >>> text=u"أهؤلاء من أولئكُ"
        >>> normalize_hamza(text)
        اهءلاء من اولءكُ

    @param text: arabic text.
    @type text: unicode.
    @return: return a converted text.
    @rtype: unicode.
    """
    text = arabconst.ALEFAT_PATTERN.sub(arabconst.ALEF, text)
    return arabconst.HAMZAT_PATTERN.sub(arabconst.HAMZA, text)

#--------------------------------------
def normalize_lamalef(text):
    """Normalize Lam Alef ligatures into two letters (LAM and ALEF),
    and return a result text.
    Some systems present lamAlef ligature as a single letter,
    this function convert it into two letters,
    The converted letters into  LAM and ALEF are :
        - LAM_ALEF, LAM_ALEF_HAMZA_ABOVE, LAM_ALEF_HAMZA_BELOW,
         LAM_ALEF_MADDA_ABOVE

    Example:
        >>> text=u"لانها لالئ الاسلام"
        >>> normalize_lamalef(text)
        لانها لالئ الاسلام

    @param text: arabic text.
    @type text: unicode.
    @return: return a converted text.
    @rtype: unicode.
    """
    return arabconst.normalize_ligature(text)
#--------------------------------------
def normalize_spellerrors(text):
    """Normalize some spellerrors like,
    TEH_MARBUTA into HEH,ALEF_MAKSURA into YEH, and return
    a result text.
    In some context users omit the difference between TEH_MARBUTA
    and HEH, and ALEF_MAKSURA and YEh.
    The conversions are:
        - TEH_MARBUTA into HEH
        - ALEF_MAKSURA into YEH

    Example:
        >>> text=u"اشترت سلمى دمية وحلوى"
        >>> normalize_spellerrors(text)
        اشترت سلمي دميه وحلوي

    @param text: arabic text.
    @type text: unicode.
    @return: return a converted text.
    @rtype: unicode.
    """
    text = re.sub(u'[%s]' % arabconst.TEH_MARBUTA, arabconst.HEH, text)
    return re.sub(u'[%s]' % arabconst.ALEF_MAKSURA, arabconst.YEH, text)

######################################################################
#{ Normalize One Function
######################################################################

def normalize_searchtext(text):
    """Normalize input text and return a result text.
    Normalize a text by :
        - strip tashkeel
        - strip tatweel
        - normalize  Hamza
        - normalize Lam Alef.
        - normalize Teh Marbuta and Alef Maksura
    Example:
        >>> text=u'أستشتري دمـــى آلية لأبنائك قبل الإغلاق'
        >>> normalize_searchtext(text)
        استشتري دمي اليه لابناءك قبل الاغلاق

    @param text: arabic text.
    @type text: unicode.
    @return: return a normalized text.
    @rtype: unicode.
    """
    text = strip_tashkeel(text)
    text = strip_tatweel(text)
    text = normalize_lamalef(text)
    text = normalize_hamza(text)
    text = normalize_spellerrors(text)
    return text
