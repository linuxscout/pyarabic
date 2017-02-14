 #~* ----------------------------------------------------------------------
 #~*
 #~* Copyright (C) 2009 by Khaled Al-Shamaa.
 #~*
 #~* http://www.ar-php.org
 #~*
 #~* ----------------------------------------------------------------------
 #~*
 #~* LICENSE
 #~*
 #~* This program is open source product you can redistribute it and/or
 #~* modify it under the terms of the GNU Lesser General Public License (LGPL)
 #~* as published by the Free Software Foundation either version 3
 #~* of the License, or (at your option) any later version.
 #~*
 #~* This program is distributed in the hope that it will be useful,
 #~* but WITHOUT ANY WARRANTY without even the implied warranty of
 #~* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #~* GNU Lesser General Public License for more details.
 #~*
 #~* You should have received a copy of the GNU Lesser General Public License
 #~* along with this program.  If not, see <http://www.gnu.org/licenses/lgpl.txt>.
 #~*
 #~* ----------------------------------------------------------------------
 #~*
 #~* Class Name: Spell numbers in the Arabic idiom
 #~*
 #~* Filename:   ArNumbers.class.php
 #~*
 #~* Original    Author(s): Khaled Al-Sham'aa <khaled.alshamaa@gmail.com>
 #~*
 #~* Purpose:    Spell numbers in the Arabic idiom
 #~*
 #~* ----------------------------------------------------------------------
 #~*
 #~* Spell numbers in the Arabic idiom
 #~*
 #~* PHP class to spell numbers in the Arabic idiom. This function is very
 #~* useful for financial applications in Arabic for example.
 #~*
 #~* If you ever have to create an Arabic PHP application built around invoicing or
 #~* accounting, you might find this class useful. Its sole reason for existence is
 #~* to help you translate integers into their spoken-word equivalents in Arabic
 #~* language.
 #~*
 #~* How is this useful? Well, consider the typical invoice: In addition to a
 #~* description of the work done, the date, and the hourly or project cost, it always
 #~* includes a total cost at the end, the amount that the customer is expected to pay.
 #~* To avoid any misinterpretation of the total amount, many organizations (mine
 #~* included) put the amount in both words and figures for example, 1,200 becomes
 #~* "one thousand and two hundred dollars." You probably do the same thing every time
 #~* you write a check.
 #~*
 #~* Now take this scenario to a Web-based invoicing system. The actual data used to
 #~* generate the invoice will be stored in a database as integers, both to save space
 #~* and to simplify calculations. So when a printable invoice is generated, your Web
 #~* application will need to convert those integers into words, this is more clarity
 #~* and more personality.
 #~*
 #~* This class will accept almost any numeric value and convert it into an equivalent
 #~* string of words in written Arabic language (using Windows-1256 character set).
 #~* The value can be any positive number up to 999,999,999 (users should not use
 #~* commas). It will take care of feminine and Arabic grammar rules.
 #~*
 #~* Example:
 #~* <code>
 #~*     include('./Arabic.php')
 #~*     Arabic = new Arabic('ArNumbers')
 #~*
 #~*     Arabic->ArNumbers->setFeminine(1)
 #~*     Arabic->ArNumbers->setFormat(1)
 #~*
 #~*     integer = 2147483647
 #~*
 #~*     text = Arabic->int2str(integer)
 #~*
 #~*     echo "<p align = \"right\"><b class = hilight>integer</b><br />text</p>"
 #~*
 #~*     Arabic->ArNumbers->setFeminine(2)
 #~*     Arabic->ArNumbers->setFormat(2)
 #~*
 #~*     integer = 2147483647
 #~*
 #~*     text = Arabic->int2str(integer)
 #~*
 #~*     echo "<p align = \"right\"><b class = hilight>integer</b><br />text</p>"
 #~* </code>
 #~*
 #~* @category  Text
 #~* @package   Arabic
 #~* @author    Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
 #~* @copyright 2009 Khaled Al-Shamaa
 #~*
 #~* @license   LGPL <http://www.gnu.org/licenses/lgpl.txt>
 #~* @link      http://www.ar-php.org
#~
 #~* This PHP class spell numbers in the Arabic idiom
 #~*
 #~* @category  Text
 #~* @package   Arabic
 #~* @author    Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
 #~* @copyright 2009 Khaled Al-Shamaa
 #~*
 #~* @license   LGPL <http://www.gnu.org/licenses/lgpl.txt>
 #~* @link      http://www.ar-php.org
'''     Arabic number class    '''
import math
import pyarabic.araby as araby
import pyarabic.number_const as nbconst

class ArNumbers:
    '''
    Arabic number class    '''
    _individual = {}
    _feminine = 1
    _format = 1
    def __init__(self):
        self._individual = nbconst.INDIVIDUALS
        self.complications = nbconst.COMPLICATIONS
    def set_feminine(self, value):
        """
         * Set feminine flag of the counted object
         *
         * @param integer value Counted object feminine (1 for masculine & 2 for feminine)
         *
         * @return boolean True if success, or False if fail
         * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
         """

        flag = True
        if (value  ==  1 or value  ==  2):
            self._feminine = value
        else:
            flag = False
        return flag

    def set_format(self, value):
        """
         * Set the grammar position flag of the counted object
         *
         * @param integer value Grammar position of counted object
         *                       (1 if Marfoua & 2 if Mansoub or Majrour)
         *
         * @return boolean True if success, or False if fail
         * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
         """

        flag = True

        if (value  ==  1 or value  ==  2):
            self._format = value
        else:
            flag = False
        return flag



    def get_feminine(self):
        """
             * Get the feminine flag of counted object
             *
             * @return integer return current setting of counted object feminine flag
             * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
        """        
        return self._feminine
    def get_format(self):
        """
         * Get the grammer position flag of counted object
         *
         * @return integer return current setting of counted object grammer
         *                 position flag
         * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
         """

        return self._format

    def int2str(self,  number, output_charset = None, main = None):
        """
         * Spell integer number in Arabic idiom
         *
         * @param integer number        The number you want to spell in Arabic idiom
         * @param string  outputCharset (optional) Output charset [utf-8|windows-1256|iso-8859-6]
         *                               default value is None (use set output charset)
         * @param object  main          Main Ar-PHP object to access charset converter options
         *
         * @return string The Arabic idiom that spells inserted number
         * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
         """
        temp = number.split('.')
        string = self._int2str(temp[0])
        if (len(temp)>1):
            dec = self._int2str(temp[1])
            string +=  u' فاصلة ' + dec
        if (main):
            if (output_charset  ==  None):
                output_charset = main.getOutputCharset()
            string = main.coreConvert(string, 'utf-8', output_charset)
        return string

    def _int2str(self, number):
        """
		 * Spell integer number in Arabic idiom
		 *
		 * @param integer number The number you want to spell in Arabic idiom
		 *
		 * @return string The Arabic idiom that spells inserted number
		 * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
        """

        blocks = []
        items = []
        string = u''
        number = number#trunc(int(number)) #(int)number)
        try:
            number = int(number)
        except  ValueError:
            number = "0"
        if (int(number) > 0):
            while (len(number) > 3):
                blocks.append( number[-3:])
                number = number[:len(number) - 3]
            blocks.append(number)
            blocks_num = len(blocks) - 1
            i = blocks_num
            while i >= 0:#(i = blocks_num i > =  0 i--) :
                number = math.floor(int(blocks[i]))
                text = self._written_block(number)
                if (text) :
                    if (number  ==  1 and i !=  0) :
                        text = self.complications[i][4]
                    elif (number  ==  2 and i !=  0) :
                        text = self.complications[i][self._format]
                    elif (number > 2 and number < 11 and i !=  0) :
                        text +=  u' ' + self.complications[i][3]
                    elif (i !=  0) :
                        text +=  u' ' + self.complications[i][4]
                    items.append(text)
                i -= 1
            string = u' و '.join(items)
        else :
            string = u'صفر'
        return string


    def _written_block(self, number):
        """
         Spell sub block number of three digits max in Arabic idiom
         *
         * @param integer number Sub block number of three digits max you want to
         *                        spell in Arabic idiom
         *
         * @return string The Arabic idiom that spells inserted sub block
         * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
         """
        items = []
        string = u''
        number = int(number)
        if (number > 99):
            hundred = math.floor(number / 100) * 100
            number = number % 100

            if (hundred  ==  200):
                items.append( self._individual[hundred][self._format])
            else:
                items.append( self._individual[hundred])
        if (number  ==  2 or number  ==  12):
            items.append(self._individual[number][self._feminine][self._format])
        elif (number < 20):
            items.append(self._individual[int(number)][self._feminine])
        else :
            ones = number % 10
            tens = math.floor(number / 10) * 10
            tens = int(tens)

            if (ones  ==  2) :
                items.append(\
                  self._individual[ones][self._feminine][self._format])
            elif (ones > 0) :
                items.append( self._individual[ones][self._feminine])
            items.append( self._individual[tens][self._format])

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
    @return : number extracted from text
    @rtype: integer
    """
    #the result total is 0
    total = 0
    # the partial total for the three number
    partial = 0
    text = araby.strip_tashkeel(text)
    words = text.split(u' ')
    #print words
    for word in words:
        if word and word != u'واحد' and \
           word[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
            word = word[1:]
        if word != u'واحد' and word.startswith(u'و'):
            word = word[1:]
            
        if nbconst.NumberWords.has_key(word):
            actualnumber = nbconst.NumberWords[word]
            if actualnumber % 1000 == 0:
                # the case of 1000 or 1 million
                if partial == 0:
                    partial = 1
                total += partial* actualnumber
                #re-initiate the partial total
                partial = 0                
            else:
                partial += nbconst.NumberWords[word]
    # add the final partial to total
    total += partial        
    return total
def vocalize_number(wordlist, syn_tags = ""):
    """ Vocalize a number words
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
    tags =  syn_tags
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
        if nbconst.NumberWords.has_key(key) and \
          not key in (u'عشر', u'خمس', u'سبع',  u'تسع', u'خمسا',
            u'سبعا', u'تسعا', u'عشرا',  u'ألفين', u'عشرة',  u'صفر',  u'ألف'):
            voc = prefix + nbconst.VocalizedNumberWords[key]['i']
        return [voc, ]
    for i in range(len(wordlist)):
        #save the original word with possible harakat if exist
        word = wordlist[i]
        word_nm = araby.strip_tashkeel(word)
        key = word_nm
        # the first word can have prefixes 
        if i == 0 and word_nm and word_nm != u'واحد' and\
            word[0] in (u'و',  u'ف',  u'ل',  u'ب',  u'ك'):
            if word_nm[0] in (u'ل',  u'ب',  u'ك'):
                tags += u"مجرور"
            key = word[1:]
        elif word_nm != u'واحد' and word_nm.startswith(u'و'):
            key = word_nm[1:]
        if nbconst.NumberWords.has_key(key):
            if word_nm.endswith(u'ين') : 
                tags += u"مجهول" # إما مجرور أو منصوب
            elif word_nm.endswith(u'ان')  or word_nm.endswith(u'ون') :
                tags += u"مرفوع"
    #add tashkeel 
    #wordlist = araby.stripTashkeel(u" ".join(wordlist)).split(' ')
    pre_key = u''
    for i in range(len(wordlist)):
        word = wordlist[i]
        if i+1 < len(wordlist):
            nextword = wordlist[i+1]
        else: nextword = u""
        key = word
        # the first word can have prefixes 
        if word and word != u'واحد' and\
            word[0] in (u'و',  u'ف', u'ل', u'ب', u'ك'):
            key = word[1:]
            prefix = word[0]
            if prefix in  (u'و', u'ف',  u'ك'):
                prefix += u'َ'
            elif prefix in  ( u'ل', u'ب'):
                prefix  += u'ِ'
        else: prefix = ''
        if nbconst.VocalizedNumberWords.has_key(key):
            voc = u''
            if nbconst.VocalizedNumberWords[key]['s'] == "*":
                voc = prefix + nbconst.VocalizedNumberWords[key]['i']

            # مبني على النصب في حالة المركب العددي
            elif nextword == u'عشر' or nextword == u'عشرة':
                voc = prefix + nbconst.VocalizedNumberWords[key]['n']
            # مبني على النصب في حالة المركب العددي
            elif key == u'عشر' and pre_key in nbconst.NumberTenMasculinUnits:
                voc = u'عَشَرَ'
            elif key == u'عشرة' and pre_key in nbconst.NumberTenFemininUnits:
                voc = u'عَشْرَةَ'
            elif u'مرفوع' in tags:
                if nextword.startswith(u'و'):
                    voc = prefix + nbconst.VocalizedNumberWords[key]['r2']
                else:        
                    voc = prefix + nbconst.VocalizedNumberWords[key]['r']
            elif u'مجهول' in tags:
                voc = prefix + nbconst.VocalizedNumberWords[key]['i']
            
            elif u'مجرور' in tags:
                if nextword.startswith(u'و'):
                    voc = prefix + nbconst.VocalizedNumberWords[key]['j2']
                else:        
                    voc = prefix + nbconst.VocalizedNumberWords[key]['j']
            # منصوب
            elif u'منصوب' in tags:
                if nextword.startswith(u'و'):
                    voc = prefix + nbconst.VocalizedNumberWords[key]['n2']
                else:        
                    voc = prefix + \
                      nbconst.VocalizedNumberWords[key]['n']            
            else:
                voc = prefix + nbconst.VocalizedNumberWords[key]['i'] 
            newlist.append(voc)        
        else:
            newlist.append(prefix+key)
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
    return nbconst.UnitWords.has_key(word)
    
def vocalize_unit(numeric, unit):
    """ Vocalize a number words
    @param numeric: given number
    @type numeric: integer
    @param unit: unit to vocalize
    @type unit: unicode
    @return: the vocalized unit, or unit word if itsnt a unit word.
    @rtype: unicode
    """
    #detect tags 
    # The given word is not a unit
    unit_nm = araby.strip_tashkeel(unit)
    if not is_unit(unit_nm):
        return unit
    tags =  u""
    vocalizedunit = unit

    # العدد بين واحد واثنان يتطلب صفة للوحدة ويكون بعدها
    # هذه الحالة لا تبرمج

    if numeric >= 0 and numeric <= 2:
        return unit
    # الإضافة إلى تمييز مضاف  إليه مجرور مفرد
    # تممييز الألف والمئة والمليون والمليار 
    # يتطلب إضافة إلى مفرد
    # مثلا ألف رجل
    elif  numeric % 100  ==  0 or  numeric % 1000  ==  0:
        tags = 'SingleMajrour'
        vocalizedunit = nbconst.UnitWords[unit_nm]['a']
    # العدد المفرد يتطلب 
    # إضافة إلى الجمع
    elif numeric % 100 <= 10:
        tags += "Plural"
        vocalizedunit = nbconst.UnitWords[unit_nm]['p']

    elif numeric % 100 < 100:
        tags += 'SingleMansoub'
        vocalizedunit = nbconst.UnitWords[unit_nm]['n']
    else:
        tags = ''
        vocalizedunit = nbconst.UnitWords[unit_nm]['i']
    if not vocalizedunit:
        return 'Error' + tags
    else:
        return vocalizedunit


def get_previous_tag(word):
    """Get the word tags
    @param word: given word
    @type word: unicode
    @return :word tag
    @rtype: unicode
    """
    word = araby.strip_tashkeel(word)
    #~ tags = u''
    if word in nbconst.NOUN_NASEB_LIST:
        return u'منصوب'
    elif word in nbconst.JAR_LIST:
        return u'مجرور'
    elif word in nbconst.RAFE3_LIST:
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
    @return : number words extracted from text
    @rtype: integer
    """
    phrases = []

    wordlist = araby.tokenize(text)
    positions =  detect_number_phrases_position(wordlist)

    for pos in positions:
        if len(pos) >= 2:
            if pos[0] <= len(wordlist) and pos[1] <= len(wordlist):
                phrases.append(u' '.join(wordlist[pos[0]: pos[1]+1]))
    return phrases
def extract_number_context(text, ):
    """
    Extract number words in a text.
    
    Example:
    >>> extract_number_context(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا")
    وجدت، خمسمئة وثلاثة وعشرين، دينارا
    فاشتريت، ثلاثة عشر ، دفترا
    
    @param text: input text
    @type text: unicode
    @return: number words extracted from text
    @rtype: integer
    """
    phrases = []
    wordlist = araby.tokenize(text)
    positions =  detect_number_phrases_position(wordlist)

    for pos in positions:
        if len(pos) >= 2:
            if pos[0] <= len(wordlist) and pos[1] <= len(wordlist):
                if pos[0]-1 >= 0: 
                    prev =  wordlist[pos[0]-1]
                else: prev = u''
                if pos[1]+1 < len(wordlist): 
                    nextword =  wordlist[pos[1]+1]
                else: nextword = u''
                phrases.append( \
                      (prev, u' '.join(wordlist[pos[0]:pos[1]+1]), nextword))
    return phrases

def detect_number_phrases_position(wordlist):
    """
    Detect number words in a text and return positions of each phrase.
    
    Example:
    >>> detect_number_phrases_position(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا")
    (1،3)، (6،7)
    @param wordlist: wordlist
    @type wordlist: unicode list
    @return : list of numbers clause positions [(start,end),(start2,end2),]
    @rtype: list of tuple

    """
    #~ wordlist# = text.split(u' ')
    #print words
    phrases = []
    startnumber = -1
    endnumber = False
    for i in range(len(wordlist)):
        word = wordlist[i]
        if i+1 < len(wordlist):
            nextword = araby.strip_tashkeel(wordlist[i+1])
        else: nextword = None
        #save the original word with possible harakat if exist
        word_nm = araby.strip_tashkeel(word)
        key = word_nm
        # the first word can have prefixes 
        if word_nm and not startnumber and word_nm != u'واحد' \
            and word_nm[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
            key = word_nm[1:]
        elif word_nm != u'واحد' and word_nm.startswith(u'و'):
            key = word_nm[1:]
        if nbconst.NumberWords.has_key(key):
            if not key in (u'أحد', u'إحدى', u'اثنا', u'اثني',  u'اثنتي', \
             u'اثنتا')  or nextword in (u'عشر',  u'عشرة'):
                if startnumber < 0:
                    startnumber = i
                endnumber = i
            # phrase.append(word)
        else:
            if startnumber >= 0: #There are a previous number phrase.
                phrases.append((startnumber, endnumber))
            startnumber = -1
    # add the final phrases 
    if startnumber >= 0: #There are a previous number phrase.
        phrases.append((startnumber, endnumber))
    return phrases

def detect_number_words(text):
    """
    Detect number words in a text.
    
    Example:
    >>> text2number(u"وجدت خمسمئة وثلاثة وعشرين دينارا")
                    خمسمئة وثلاثة وعشرين
    
    @param text: input text
    @type text: unicode
    @return : number words extracted from text
    @rtype: integer
    """

    #~ words = araby.tokenize(text)
    #print words
    phrases_context = extract_number_context(text)
    for ph_con in phrases_context:
        if len(ph_con) >= 3:
            previous = ph_con[0]
            phrase = ph_con[1]
            nextword = ph_con[2]
            numberedwords = phrase
            numeric = text2number(numberedwords)
            tags = get_previous_tag(previous)
            vocalized = vocalize_number(araby.strip_tashkeel(\
            numberedwords).split(' '), tags)                
            #calcul  vocalization similarity : 
            sim = araby.vocalized_similarity(numberedwords, vocalized)
            voc_unit = vocalize_unit(numeric, nextword)
            sim_unit = araby.vocalized_similarity(voc_unit, \
                nextword)                    
            if sim < 0:
                print u'\t'.join([str(sim), numberedwords, vocalized, \
                 str(numeric), u' '.join([previous, phrase, nextword]), \
                  nextword, voc_unit, str(sim_unit)]).encode('utf8')

def pre_tashkeel_number(wordlist):
    """
    Detect number words in a text.
    
    Example:
    >>> preTashkeelNumber(u"وجدت خمسمئة وثلاثة وعشرين دينارا")
    وجدت خمسمئة وثلاثة وعشرين دينار
    @param wordlist: input text
    @type wordlist: unicode
    @return : wordlist with vocalized number clause
    @rtype: list
ا
    """

    positions =  detect_number_phrases_position(wordlist)
    for pos in positions:
        if len(pos) >= 2:
            startpos = pos[0]
            endpos =  pos[1]
            if startpos <= len(wordlist) and endpos <= len(wordlist):
                # get the context of current number phrase
                if startpos-1 >= 0:
                    previous =  wordlist[startpos-1]
                else: previous = u''
                #~ if endos+1 < len(wordlist):
                    #~ next =  wordlist[endpos+1]
                #~ else: next = u''
                #get the tag of previous word
                tags = get_previous_tag(previous)
                vocalized = vocalize_number(wordlist[startpos: endpos+1], \
                                          tags)                
                wordlist = wordlist[:startpos] + vocalized +wordlist[endpos+1:]
    return wordlist
if __name__  ==  '__main__':
    #import number as ArabicNumberToLetters
    TEXTS = [u"مليونان وألفان وإثنا عشر", 
    u"جاء مليونان وألفان وإثنا عشر", 
    u"وجدت خمسمئة وثلاث وعشرون دينارا",
        u"خمسمئة وثلاث وعشرون دينارا",
    u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا",
    u"لم أجد شيئا",
    u'من ثلائمئة وخمسين بلدا ',
        u'من ثلاثمئة وخمسين بلدا ',
    u'من أربعمئة وخمسين بلدا ',
    ]
    for txt in TEXTS:
        positions_phrases =  detect_number_phrases_position(araby.tokenize(txt))
        print positions_phrases
        nb_phrases = extract_number_phrases(txt)
        print txt.encode('utf8')
        print u'\t'.join(nb_phrases).encode('utf8')
