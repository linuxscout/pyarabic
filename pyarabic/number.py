#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
Arabic numbers routins
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Arabtechies, Arabeyes, Taha Zerrouki
@license: GPL
@date:2017/02/14
@version: 0.3
# ArNumbers is imported from
license:   LGPL <http://www.gnu.org/licenses/lgpl.txt>
link      http://www.ar-php.org
category  Text
author    Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
copyright 2009 Khaled Al-Shamaa
"""
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
)

import math
import sys
from six import text_type as unicode
try:
    import araby
    import number_const as nbconst
    import named_const as nmconst
    import arabrepr

except ImportError:
    from . import araby
    from . import number_const as nbconst
    from . import named_const as nmconst
    from . import arabrepr


class ArNumbers(object):
    '''
    Arabic number class
    '''
    _individual = {}
    _feminine = 1
    _format = 1

    ##"""
    ##     * Loads initialize values
    ##"""
    def __init__(self):
        self._individual = nbconst.INDIVIDUALS
        self.complications = nbconst.COMPLICATIONS

    def set_feminine(self, value):
        """
         Set feminine flag of the counted object
         @param value: value Counted object feminine (1 for masculine & 2 for feminine)
         @type value: integer
         @return: True if success, or False if fail
         @rtype: boolean
         """

        flag = True
        if value in (1, 2):
            self._feminine = value
        else:
            flag = False
        return flag

    def set_format(self, value):
        """
        Set the grammar position flag of the counted object
        @param value: Grammar position of counted object (1 if Marfoua & 2 if Mansoub or Majrour)
        @type value: integer
        @return: True if success, or False if fail
        @rtype: boolean
        """

        flag = True

        if value in (1, 2):
            self._format = value
        else:
            flag = False
        return flag

    def get_feminine(self):
        """
        Get the feminine flag of counted object
        @return: return current setting of counted object feminine flag
        @rtype: integer
        """
        return self._feminine

    def get_format(self):
        """
        Get the grammer position flag of counted object
        @return: return current setting of counted object grammer position flag
        @rtype: integer
        """

        return self._format

    def int2str(self, number, output_charset=None, main=None):
        """
         Spell integer number in Arabic idiom
         @param number: The number you want to spell in Arabic idiom
         @type number: integer
         @param  output_charset: (optional) Output charset [utf-8|windows-1256|iso-8859-6]
         default value is None (use set output charset)
         @type  output_charset: string
         @param main:  Main Ar-PHP object to access charset converter options
         @type main: object
         @return: The Arabic idiom that spells inserted number
         @rtype: string
         """
        temp = number.split('.')
        string = self._int2str(temp[0])
        if len(temp) > 1:
            dec = self._int2str(temp[1])
            string += u' فاصلة ' + dec
        if main:
            if output_charset is None:
                output_charset = main.getOutputCharset()
            string = main.coreConvert(string, 'utf-8', output_charset)
        return string

    def _int2str(self, number_str):
        """
        Spell integer number in Arabic idiom
        @param number_str: The number you want to spell in Arabic idiom
        @type number_str: integer.
        @return: The Arabic idiom that spells inserted number
        @rtype:string
        """

        blocks = []
        items = []
        string = u''
        # ~ number = number#trunc(int(number)) #(int)number)
        try:
            number = int(number_str)
        except  ValueError:
            number = 0
        if int(number) > 0:
            number_part = ""
            while len(number_str) > 3:
                blocks.append(number_str[-3:])
                number_str = number_str[:len(number_str) - 3]
            blocks.append(number_str)
            blocks_num = len(blocks) - 1
            i = blocks_num
            while i >= 0:  # (i = blocks_num i > = 0 i--):
                number = math.floor(int(blocks[i]))
                text = self._written_block(number)
                if text:
                    if number == 1 and i != 0:
                        text = self.complications[i][4]
                    elif number == 2 and i != 0:
                        text = self.complications[i][self._format]
                    elif number > 2 and number < 11 and i != 0:
                        text += u' ' + self.complications[i][3]
                    elif i != 0:
                        text += u' ' + self.complications[i][4]
                    items.append(text)
                i -= 1
            string = u' و '.join(items)
        else:
            string = u'صفر'
        return string

    def _written_block(self, number):
        """
        Spell sub block number of three digits max in Arabic idiom
        @param number: number Sub block number of three digits max you want to spell in Arabic idiom
        @type number: integer
        @return: The Arabic idiom that spells inserted sub block
        @rtype: String
        """
        items = []
        string = u''
        number = int(number)
        if number > 99:
            hundred = math.floor(number / 100) * 100
            number = number % 100

            if hundred == 200:
                items.append(self._individual[hundred][self._format])
            else:
                items.append(self._individual[hundred])
        if number == 2 or number == 12:
            items.append(self._individual[number][self._feminine][self._format])
        elif number < 20:
            items.append(self._individual[int(number)][self._feminine])
        else:
            ones = number % 10
            tens = math.floor(number / 10) * 10
            tens = int(tens)

            if ones == 2:
                items.append( \
                    self._individual[ones][self._feminine][self._format])
            elif ones > 0:
                items.append(self._individual[ones][self._feminine])
            items.append(self._individual[tens][self._format])

        if u'' in items:
            items.remove(u'')
        string = u' و '.join(items)
        return string


def text2number(text):
    """
    Convert arabic text into number, for example convert تسعة وعشرون = >29.

    Example:
        >>> text2number(u"خمسمئة وثلاث وعشرون")
        523

    @param text: input text
    @type text: unicode
    @return: number extracted from text
    @rtype: integer
    """
    # the result total is 0
    total = 0
    # the partial total for the three number
    partial = 0
    text = araby.strip_tashkeel(text)
    words = text.split(u' ')
    # print words
    for word in words:
        if word and word != u'واحد' and word[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
            word = word[1:]
        if word != u'واحد' and word.startswith(u'و'):
            word = word[1:]

        if word in nbconst.NUMBER_WORDS:
            actualnumber = nbconst.NUMBER_WORDS[word]
            if actualnumber % 1000 == 0:
                # the case of 1000 or 1 million
                if partial == 0:
                    partial = 1
                total += partial * actualnumber
                # re-initiate the partial total
                partial = 0
            else:
                partial += nbconst.NUMBER_WORDS[word]
    # add the final partial to total
    total += partial
    return total


def number2text(anumber):
    """
    Convert number to arabic words, for example convert 25 --> خمسة و عشرون

    Example:
        >>> number2text(523)
        خمسمئة وثلاث وعشرون

    @param anumber: input number
    @type anumber: int
    @return: number words
    @rtype: unicode
    """
    # test if the given type is numeric(float or int
    # if ok, convert it to string
    if type(anumber) is int or type(anumber) is float:
        anumber = str(anumber)
    # if the given type is str/unicode, test if it's a valid number
    elif type(anumber) is str or type(anumber) is unicode:
        try:
            a = float(anumber);
        except ValueError:
            return u"صفر"
    # if the given number not a valid return 0
    else:
        return u"صفر"
    arbn = ArNumbers()
    return arbn.int2str(anumber)

    return total


def vocalize_number(wordlist, syn_tags=""):
    """ Vocalize a number words clause

    Example:
        >>> txt = u"خمسمئة وثلاثة وعشرين"
        >>> wordlist = araby.tokenize(txt)
        >>> vocalized = vocalize_number(wordlist)
        >>> print u" ".join(vocalized)
        خَمْسمِئَة وَثَلاثَة وَعِشْرِينَ

    @param wordlist: words to vocalize
    @type wordlist: unicode list
    @param syn_tags: tags about the clause
    @type syn_tags: unicode
    @return: the vocalized wordlist.
    @rtype: unicode
    """
    newlist = []
    prefix = u""
    nextword = u""
    # we can pass tags to this number word
    tags = syn_tags
    if len(wordlist) == 1:
        word = wordlist[0]
        word_nm = araby.strip_tashkeel(word)
        key = word_nm
        voc = word
        # the first word can have prefixes
        if word_nm and not wordlist and word_nm != u'واحد' \
                and word[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
            if word_nm[0] in (u'ل', u'ب', u'ك'):
                tags += u"مجرور"
            key = word[1:]
        elif word_nm != u'واحد' and word_nm.startswith(u'و'):
            key = word_nm[1:]
        # تحذب بعض الكلمات لأنها تلتبس مع أسماء الأجزاء مثل خُمس وخمس
        if key in nbconst.NUMBER_WORDS and \
                key not in (u'عشر', u'خمس', u'سبع', u'تسع', u'خمسا', \
                            u'سبعا', u'تسعا', u'عشرا', u'ألفين', u'عشرة', u'صفر', u'ألف'):
            voc = prefix + nbconst.VOCALIZED_NUMBER_WORDS[key]['i']
        return [voc, ]
    for i, word in enumerate(wordlist):
        # save the original word with possible harakat if exist
        # ~ word = wordlist[i]
        word_nm = araby.strip_tashkeel(word)
        key = word_nm
        # the first word can have prefixes
        if i == 0 and word_nm and word_nm != u'واحد' and \
                word[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
            if word_nm[0] in (u'ل', u'ب', u'ك'):
                tags += u"مجرور"
            key = word[1:]
        elif word_nm != u'واحد' and word_nm.startswith(u'و'):
            key = word_nm[1:]
        if key in nbconst.NUMBER_WORDS:
            if word_nm.endswith(u'ين'):
                tags += u"مجهول"  # إما مجرور أو منصوب
            elif word_nm.endswith(u'ان') or word_nm.endswith(u'ون'):
                tags += u"مرفوع"
    # add tashkeel
    # wordlist = araby.stripTashkeel(u" ".join(wordlist)).split(' ')
    pre_key = u''
    for i, word in enumerate(wordlist):
        # ~ word = wordlist[i]
        if i + 1 < len(wordlist):
            nextword = wordlist[i + 1]
        else:
            nextword = u""
        key = word
        # the first word can have prefixes
        if word and word != u'واحد' and \
                word[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
            key = word[1:]
            prefix = word[0]
            if prefix in (u'و', u'ف', u'ك'):
                prefix += u'َ'
            elif prefix in (u'ل', u'ب'):
                prefix += u'ِ'
        else:
            prefix = u''
        if key in nbconst.VOCALIZED_NUMBER_WORDS:
            voc = u''
            if nbconst.VOCALIZED_NUMBER_WORDS[key]['s'] == "*":
                voc = prefix + nbconst.VOCALIZED_NUMBER_WORDS[key]['i']

            # مبني على النصب في حالة المركب العددي
            elif nextword == u'عشر' or nextword == u'عشرة':
                voc = prefix + nbconst.VOCALIZED_NUMBER_WORDS[key]['n']
            # مبني على النصب في حالة المركب العددي
            elif key == u'عشر' and pre_key in nbconst.NUMBER_TEN_MASCULIN_UNITS:
                voc = u'عَشَرَ'
            elif key == u'عشرة' and pre_key in nbconst.NUMBER_TEN_FEMININ_UNITS:
                voc = u'عَشْرَةَ'
            elif u'مرفوع' in tags:
                if nextword.startswith(u'و'):
                    voc = prefix + nbconst.VOCALIZED_NUMBER_WORDS[key]['r2']
                else:
                    voc = prefix + nbconst.VOCALIZED_NUMBER_WORDS[key]['r']
            elif u'مجهول' in tags:
                voc = prefix + nbconst.VOCALIZED_NUMBER_WORDS[key]['i']

            elif u'مجرور' in tags:
                if nextword.startswith(u'و'):
                    voc = prefix + nbconst.VOCALIZED_NUMBER_WORDS[key]['j2']
                else:
                    voc = prefix + nbconst.VOCALIZED_NUMBER_WORDS[key]['j']
            # منصوب
            elif u'منصوب' in tags:
                if nextword.startswith(u'و'):
                    voc = prefix + nbconst.VOCALIZED_NUMBER_WORDS[key]['n2']
                else:
                    voc = prefix + \
                          nbconst.VOCALIZED_NUMBER_WORDS[key]['n']
            else:
                voc = prefix + nbconst.VOCALIZED_NUMBER_WORDS[key]['i']
            newlist.append(voc)
        else:
            newlist.append(prefix + key)
        pre_key = key
    return newlist


def is_unit(word):
    """
    return if the given word is a unit
    @param word: given word to be tested
    @type word: unicode
    @return: if word is a unit return True else False.
    @rtype: Boolean
    """
    return word in nbconst.UNIT_WORDS


def vocalize_unit(numeric, unit):
    """ Vocalize a number words
    @param numeric: given number
    @type numeric: integer
    @param unit: unit to vocalize
    @type unit: unicode
    @return: the vocalized unit, or unit word if itsnt a unit word.
    @rtype: unicode
    """
    # detect tags
    # The given word is not a unit
    unit_nm = araby.strip_tashkeel(unit)
    if not is_unit(unit_nm):
        return unit
    tags = u""
    vocalizedunit = unit

    # العدد بين واحد واثنان يتطلب صفة للوحدة ويكون بعدها
    # هذه الحالة لا تبرمج

    if numeric >= 0 and numeric <= 2:
        return unit
    # الإضافة إلى تمييز مضاف  إليه مجرور مفرد
    # تممييز الألف والمئة والمليون والمليار
    # يتطلب إضافة إلى مفرد
    # مثلا ألف رجل
    elif numeric % 100 == 0 or numeric % 1000 == 0:
        tags = u'SingleMajrour'
        vocalizedunit = nbconst.UNIT_WORDS[unit_nm]['a']
    # العدد المفرد يتطلب
    # إضافة إلى الجمع
    elif numeric % 100 <= 10:
        tags += "Plural"
        vocalizedunit = nbconst.UNIT_WORDS[unit_nm]['p']

    elif numeric % 100 < 100:
        tags += 'SingleMansoub'
        vocalizedunit = nbconst.UNIT_WORDS[unit_nm]['n']
    else:
        tags = ''
        vocalizedunit = nbconst.UNIT_WORDS[unit_nm]['i']
    if not vocalizedunit:
        return 'Error' + tags
    else:
        return vocalizedunit


def get_previous_tag(word):
    """Get the word tags
    @param word: given word
    @type word: unicode
    @return:word tag
    @rtype: unicode
    """
    word = araby.strip_tashkeel(word)
    # ~ tags = u''
    if word in nmconst.NOUN_NASEB_LIST:
        return u'منصوب'
    elif word in nmconst.JAR_LIST:
        return u'مجرور'
    elif word in nmconst.RAFE3_LIST:
        return u'مرفوع'
    else:
        return u''


def extract_number_phrases(text):
    """
    Extract number words in a text.

    Example:
        >>> extract_number_phrases(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا")
        خمسمئة وثلاثة وعشرين
        ثلاثة عشر

    @param text: input text
    @type text: unicode
    @return: number words extracted from text
    @rtype: integer
    """
    phrases = []

    wordlist = araby.tokenize(text)  # text.split(' ')
    positions = detect_number_phrases_position(wordlist)

    for pos in positions:
        if len(pos) >= 2:
            if pos[0] <= len(wordlist) and pos[1] <= len(wordlist):
                phrases.append(u' '.join(wordlist[pos[0]: pos[1] + 1]))
    return phrases


def extract_number_context(text, ):
    """
    Extract number words in a text within context.

    Example:
        >>> extract_number_context(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا")
        ‎وجدت، خمسمئة وثلاثة وعشرين، دينارا
        ‎فاشتريت، ثلاثة عشر ، دفتر

    @param text: input text
    @type text: unicode
    @return: number words extracted from text
    @rtype: integer
    """
    phrases = []
    wordlist = araby.tokenize(text)
    positions = detect_number_phrases_position(wordlist)

    for pos in positions:
        if len(pos) >= 2:
            if pos[0] <= len(wordlist) and pos[1] <= len(wordlist):
                if pos[0] - 1 >= 0:
                    prev = wordlist[pos[0] - 1]
                else:
                    prev = u''
                if pos[1] + 1 < len(wordlist):
                    nextword = wordlist[pos[1] + 1]
                else:
                    nextword = u''
                phrases.append( \
                    (prev, u' '.join(wordlist[pos[0]:pos[1] + 1]), nextword))
    return phrases


def detect_number_phrases_position(wordlist):
    """
    Detect number words in a text and return positions of each phrase.

    Example:
        >>> txt = u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا"
        >>> wordlist = araby.tokenize(txt)
        >>> positions_phrases = detect_number_phrases_position(wordlist)
        >>> print positions_phrase
        >>> print positions_phrases
        [(1, 3), (6, 7)]

    @param wordlist: wordlist
    @type wordlist: unicode list
    @return: list of numbers clause positions [(start,end),(start2,end2),]
    @rtype: list of tuple
    """
    # ~ wordlist# = text.split(u' ')
    # print words
    phrases = []
    startnumber = -1
    endnumber = False
    # ~ taglist = []
    for i, word in enumerate(wordlist):
        # ~ word = wordlist[i]
        if i + 1 < len(wordlist):
            nextword = araby.strip_tashkeel(wordlist[i + 1])
        else:
            nextword = None
        # save the original word with possible harakat if exist
        word_nm = araby.strip_tashkeel(word)
        key = word_nm
        # the first word can have prefixes
        if word_nm and not startnumber and word_nm != u'واحد' \
                and word_nm[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
            key = word_nm[1:]
        elif word_nm != u'واحد' and word_nm.startswith(u'و'):
            key = word_nm[1:]
        if key in nbconst.NUMBER_WORDS or key.isnumeric():
            if key not in (u'أحد', u'إحدى', u'اثنا', u'اثني', u'اثنتي', \
                           u'اثنتا') or nextword in (u'عشر', u'عشرة'):
                if startnumber < 0:
                    startnumber = i
                endnumber = i
            # phrase.append(word)
        else:
            if startnumber >= 0:  # There are a previous number phrase.
                phrases.append((startnumber, endnumber))
            startnumber = -1
    # add the final phrases
    if startnumber >= 0:  # There are a previous number phrase.
        phrases.append((startnumber, endnumber))

    return phrases


def detect_numbers(wordlist):
    """
    Detect number words in a text and return a taglist as BIO.

    Example:
        >>> wordlist = araby.tokenize(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا")
        >>> detect_numbers(wordlist)
        ['DO', 'DB', 'DI', 'DI', 'DO', 'DO', 'DB', 'DI', 'DO']

    @param wordlist: wordlist
    @type wordlist: unicode list
    @return: list of tags BIO
    @rtype: list of unicode
    """
    # ~ phrases = []
    starts = False
    taglist = []

    for i, word in enumerate(wordlist):
        # ~ word = wordlist[i]
        if i + 1 < len(wordlist):
            nextword = araby.strip_tashkeel(wordlist[i + 1])
        else:
            nextword = None
        # save the original word with possible harakat if exist
        word_nm = araby.strip_tashkeel(word)
        key = word_nm
        # the first word can have prefixes
        if word_nm and not starts and word_nm != u'واحد' \
                and word_nm[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
            key = word_nm[1:]
        elif word_nm != u'واحد' and word_nm.startswith(u'و'):
            key = word_nm[1:]
        if key in nbconst.NUMBER_WORDS or key.isnumeric():
            if key not in (u'أحد', u'إحدى', u'اثنا', u'اثني', u'اثنتي', \
                           u'اثنتا') or nextword in (u'عشر', u'عشرة'):
                if not starts:
                    taglist.append("DB")
                    starts = True
                else:
                    taglist.append("DI")
            else:
                starts = False
                taglist.append("O")
        else:
            starts = False
            taglist.append("O")
    return taglist


def detect_number_words(text):
    """
    Detect number words in a text.

    Example:
        >>> detect_number_words(u"وجدت خمسمئة وثلاثة وعشرين دينارا")
        خمسمئة وثلاثة وعشرين

    @param text: input text
    @type text: unicode
    @return: number words extracted from text
    @rtype: integer
    """

    phrases_context = extract_number_context(text)
    for ph_con in phrases_context:
        if len(ph_con) >= 3:
            previous = ph_con[0]
            phrase = ph_con[1]
            nextword = ph_con[2]
            numberedwords = phrase
            numeric = text2number(numberedwords)
            tags = get_previous_tag(previous)
            wordlist = araby.strip_tashkeel(numberedwords).split(' ')
            vocalized = vocalize_number(wordlist, tags)
            # calcul  vocalization similarity:
            sim = araby.vocalized_similarity(numberedwords, vocalized)
            voc_unit = vocalize_unit(numeric, nextword)
            sim_unit = araby.vocalized_similarity(voc_unit, nextword)

            if sim < 0:
                # ~ print u'\t'.join([str(sim), u' '.join(numberedwords), vocalized,
                # ~ str(numeric), u' '.join([previous, phrase, nextword]),
                # ~ nextword, voc_unit, str(sim_unit)]).encode('utf8')
                print(u'\t'.join([str(sim), u' '.join(numberedwords), u' '.join(vocalized)]))
                print(str(numeric), u' '.join([previous, phrase, nextword]))
                print(u'\t'.join([nextword, voc_unit, str(sim_unit)]))


def pre_tashkeel_number(wordlist):
    """
    Vocalized a number clauses in a text.

    Example:
        >>> txt = u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا"
        >>> wordlist = araby.tokenize(txt)
        >>> vocalized = pre_tashkeel_number(wordlist)
        >>> print u" ".join(vocalized)
        وجدت خَمْسمِئَة وَثَلاثَة وَعِشْرِينَ دينارا فاشتريت ثَلاثَةَ عَشَرَ دفترا

    @param wordlist: input text
    @type wordlist: unicode
    @return: wordlist with vocalized number clause
    @rtype: list
  """
    taglist = detect_numbers(wordlist)
    previous = ""
    vocalized_list = []
    chunk = []
    previous_tag = ""
    for word, tag in zip(wordlist, taglist):
        if tag in ("DB", "DI"):
            chunk.append(word)
        else:
            if chunk:
                # get the tag of previous word
                previous_tag = get_previous_tag(previous)
                vocalized = vocalize_number(chunk, previous_tag)
                vocalized_list.extend(vocalized)
                chunk = []
            vocalized_list.append(word)
            previous = word
    if chunk:
        vocalized = vocalize_number(chunk, previous_tag)
        vocalized_list.extend(vocalized)
        chunk = []
    return vocalized_list


def number2ordinal(anumber, feminin=False):
    """
    Convert number to arabic words in ordinal form, for example convert 25 --> الخامس والعشرون
    
      Example:
        >>> number2text(523)
        الخمسمئة والثالث والعشرون
    @param anumber: input number
    @type anumber: int
    @return: number words
    @rtype: unicode
    """
    # test if the given type is numeric(float or int
    # if ok, convert it to string
    a = 0
    if type(anumber) is int:
        anumber = str(anumber)
    # if the given type is str/unicode, test if it's a valid number
    elif type(anumber) is str or type(anumber) is unicode:
        try:
            a = int(anumber);
        except ValueError:
            return u"صفر"
    # if the given number not a valid return 0
    else:
        return u"الصفر"
    if a == 1:
        if feminin:
            return u"الأولى"
        else:
            return u"الأول"
    arbn = ArNumbers()
    arbn_str = arbn.int2str(anumber)
    # substitute numeral words to ordinal words
    # normalize waw
    arbn_str = arbn_str.replace(u"و ", u"و")
    tokens = arbn_str.split(" ")
    # the first token:
    # if it's  unit, change it to ordinal
    # and add definate article
    new_list = []
    if feminin:
        ordinal_words = nbconst.UNITS_ORDINAL_WORDS_FEMININ
    else:
        ordinal_words = nbconst.UNITS_ORDINAL_WORDS
    if tokens:
        tok = tokens[0]
        if tok in ordinal_words:
            # ثلاث = ثالث
            tok = ordinal_words.get(tok, tok)
        #add definite article
        tok = u"ال"+tok
        new_list.append(tok)

        for tok in tokens[1:]:
            # first strip first Waw
            if tok.startswith(araby.WAW):
                # strip waw
                tok = tok[1:]
                if tok in ordinal_words:
                    # ثلاث = ثالث
                    tok = ordinal_words.get(tok, tok)
                tok = u"وال"+tok
            new_list.append(tok)
    # ajust الواحد at the end
    if new_list[-1:] == u"الحادي":
        new_list.pop()
        new_list.append(u"الواحد")
    elif new_list[-1:] == u"الحادية":
        new_list.pop()
        new_list.append(u"الواحدة")
    ordinal_string = u" ".join(new_list)
    return ordinal_string

if __name__ == '__main__':
    # import number as ArabicNumberToLetters
    TEXTS = [u"مليونان وألفان وإثنا عشر",
             u"جاء مليونان وألفان وإثنا عشر",
             u"وجدت خمسمئة وثلاث وعشرون دينارا",
             u"خمسمئة وثلاث وعشرون دينارا",
             u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا",
             u"لم أجد شيئا",
             u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا",
             u'من ثلاثمئة وخمسين بلدا ',
             u'من ثلاثمئة وخمسين بلدا ',
             u'من أربعمئة وخمسين بلدا ',
             u'السلام عليكم 2014',
             ]
    # ~ arepr = arabrepr.ArabicRepr()
    for txt in TEXTS:
        word_list = araby.tokenize(txt)
        positions_phrases = detect_number_phrases_position(word_list)
        print(positions_phrases)
        nb_phrases = extract_number_phrases(txt)
        tag_list = detect_numbers(word_list)
        print(tag_list)
        print(u" ".join(word_list))
        print(zip(tag_list, word_list))
        print('tashkeel')
        tashkeel = u" ".join(pre_tashkeel_number(word_list))
        if sys.version_info < (3, 0):
            print(tashkeel.encode('utf8'))
        else:
            print(tashkeel)
        print(u'\t'.join(nb_phrases))
        print("detect number word")
        print(arabrepr.arepr(detect_number_words(txt)))
