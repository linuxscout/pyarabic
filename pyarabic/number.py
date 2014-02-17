"""kk
 * ----------------------------------------------------------------------
 *
 * Copyright (C) 2009 by Khaled Al-Shamaa.
 *
 * http://www.ar-php.org
 *
 * ----------------------------------------------------------------------
 *
 * LICENSE
 *
 * This program is open source product; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public License (LGPL)
 * as published by the Free Software Foundation; either version 3
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/lgpl.txt>.
 *
 * ----------------------------------------------------------------------
 *
 * Class Name: Spell numbers in the Arabic idiom
 *
 * Filename:   ArNumbers.class.php
 *
 * Original    Author(s): Khaled Al-Sham'aa <khaled.alshamaa@gmail.com>
 *
 * Purpose:    Spell numbers in the Arabic idiom
 *
 * ----------------------------------------------------------------------
 *
 * Spell numbers in the Arabic idiom
 *
 * PHP class to spell numbers in the Arabic idiom. This function is very
 * useful for financial applications in Arabic for example.
 *
 * If you ever have to create an Arabic PHP application built around invoicing or
 * accounting, you might find this class useful. Its sole reason for existence is
 * to help you translate integers into their spoken-word equivalents in Arabic
 * language.
 *
 * How is this useful? Well, consider the typical invoice: In addition to a
 * description of the work done, the date, and the hourly or project cost, it always
 * includes a total cost at the end, the amount that the customer is expected to pay.
 * To avoid any misinterpretation of the total amount, many organizations (mine
 * included) put the amount in both words and figures; for example, 1,200 becomes
 * "one thousand and two hundred dollars." You probably do the same thing every time
 * you write a check.
 *
 * Now take this scenario to a Web-based invoicing system. The actual data used to
 * generate the invoice will be stored in a database as integers, both to save space
 * and to simplify calculations. So when a printable invoice is generated, your Web
 * application will need to convert those integers into words, this is more clarity
 * and more personality.
 *
 * This class will accept almost any numeric value and convert it into an equivalent
 * string of words in written Arabic language (using Windows-1256 character set).
 * The value can be any positive number up to 999,999,999 (users should not use
 * commas). It will take care of feminine and Arabic grammar rules.
 *
 * Example:
 * <code>
 *     include('./Arabic.php');
 *     Arabic = new Arabic('ArNumbers');
 *
 *     Arabic->ArNumbers->setFeminine(1);
 *     Arabic->ArNumbers->setFormat(1);
 *
 *     integer = 2147483647;
 *
 *     text = Arabic->int2str(integer);
 *
 *     echo "<p align=\"right\"><b class=hilight>integer</b><br />text</p>";
 *
 *     Arabic->ArNumbers->setFeminine(2);
 *     Arabic->ArNumbers->setFormat(2);
 *
 *     integer = 2147483647;
 *
 *     text = Arabic->int2str(integer);
 *
 *     echo "<p align=\"right\"><b class=hilight>integer</b><br />text</p>";
 * </code>
 *
 * @category  Text
 * @package   Arabic
 * @author    Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
 * @copyright 2009 Khaled Al-Shamaa
 *
 * @license   LGPL <http://www.gnu.org/licenses/lgpl.txt>
 * @link      http://www.ar-php.org
 """

# New in PHP V5.3: Namespaces
# namespace Arabic/ArNumbers;

"""
 * This PHP class spell numbers in the Arabic idiom
 *
 * @category  Text
 * @package   Arabic
 * @author    Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
 * @copyright 2009 Khaled Al-Shamaa
 *
 * @license   LGPL <http://www.gnu.org/licenses/lgpl.txt>
 * @link      http://www.ar-php.org
 """
import math
import araby
from number import *
from number_const import *

class ArNumbers:
	_individual = {};
	_feminine = 1;
	_format = 1;
##"""
##     * Loads initialize values
##"""
	def __init__(self):
		self._individual[0]={};
		self._individual[1]={};		
		self._individual[2]={};
		self._individual[2][1]={};
		self._individual[2][2]={};
		self._individual[3]={};
		self._individual[4]={};
		self._individual[5]={};
		self._individual[6]={};
		self._individual[7]={};
		self._individual[8]={};
		self._individual[9]={};
		self._individual[10]={};
		self._individual[11]={};
		self._individual[12]={};
		self._individual[12][1]={};
		self._individual[12][2]={};
		self._individual[13]={};
		self._individual[14]={};
		self._individual[15]={};
		self._individual[16]={};
		self._individual[17]={};
		self._individual[18]={};
		self._individual[19]={};
		self._individual[20]={};
		self._individual[30]={};
		self._individual[40]={};
		self._individual[50]={};
		self._individual[60]={};
		self._individual[70]={};
		self._individual[80]={};
		self._individual[90]={};
		self._individual[100]={};
		self._individual[200]={};
		self._individual[300]={};
		self._individual[400]={};
		self._individual[500]={};
		self._individual[600]={};
		self._individual[700]={};
		self._individual[800]={};
		self._individual[900]={};
		self._individual[1000]={};
		self._individual[2000]={};
		self._individual[14]={};
		self._individual[0][1] = u'';
		self._individual[0][2] = u'';		
		self._individual[1][1] = u'واحد';
		self._individual[1][2] = u'واحدة';
		self._individual[2][1][1] = u'إثنان';
		self._individual[2][1][2] = u'إثنين';
		self._individual[2][2][1] = u'إثنتان';
		self._individual[2][2][2] = u'إثنتين';

		self._individual[3][1] = u'ثلاث';
		self._individual[4][1] = u'أربع';
		self._individual[5][1] = u'خمس';
		self._individual[6][1] = u'ست';
		self._individual[7][1] = u'سبع';
		self._individual[8][1] = u'ثماني';
		self._individual[9][1] = u'تسع';
		self._individual[10][1] = u'عشر';
		self._individual[3][2] = u'ثلاثة';
		self._individual[4][2] = u'أربعة';
		self._individual[5][2] = u'خمسة';
		self._individual[6][2] = u'ستة';
		self._individual[7][2] = u'سبعة';
		self._individual[8][2] = u'ثمانية';
		self._individual[9][2] = u'تسعة';
		self._individual[10][2] = u'عشرة';

		self._individual[11][1] = u'أحد عشر';
		self._individual[11][2] = u'إحدى عشرة';

		self._individual[12][1][1] = u'إثنا عشر';
		self._individual[12][1][2] = u'إثني عشر';
		self._individual[12][2][1] = u'إثنتا عشرة';
		self._individual[12][2][2] = u'إثنتي عشرة';

		self._individual[13][1] = u'ثلاث عشرة';
		self._individual[14][1] = u'أربع عشرة';
		self._individual[15][1] = u'خمس عشرة';
		self._individual[16][1] = u'ست عشرة';
		self._individual[17][1] = u'سبع عشرة';
		self._individual[18][1] = u'ثماني عشرة';
		self._individual[19][1] = u'تسع عشرة';
		self._individual[13][2] = u'ثلاثة عشر';
		self._individual[14][2] = u'أربعة عشر';
		self._individual[15][2] = u'خمسة عشر';
		self._individual[16][2] = u'ستة عشر';
		self._individual[17][2] = u'سبعة عشر';
		self._individual[18][2] = u'ثمانية عشر';
		self._individual[19][2] = u'تسعة عشر';

		self._individual[20][1] = u'عشرون';
		self._individual[30][1] = u'ثلاثون';
		self._individual[40][1] = u'أربعون';
		self._individual[50][1] = u'خمسون';
		self._individual[60][1] = u'ستون';
		self._individual[70][1] = u'سبعون';
		self._individual[80][1] = u'ثمانون';
		self._individual[90][1] = u'تسعون';
		self._individual[20][2] = u'عشرين';
		self._individual[30][2] = u'ثلاثين';
		self._individual[40][2] = u'أربعين';
		self._individual[50][2] = u'خمسين';
		self._individual[60][2] = u'ستين';
		self._individual[70][2] = u'سبعين';
		self._individual[80][2] = u'ثمانين';
		self._individual[90][2] = u'تسعين';

		self._individual[200][1] = u'مئتان';
		self._individual[200][2] = u'مئتين';

		self._individual[100] = u'مئة';
		self._individual[300] = u'ثلاثمئة';
		self._individual[400] = u'أربعمئة';
		self._individual[500] = u'خمسمئة';
		self._individual[600] = u'ستمئة';
		self._individual[700] = u'سبعمئة';
		self._individual[800] = u'ثمانمئة';
		self._individual[900] = u'تسعمئة';
		self.complications={1:{},2:{},3:{}};
		self.complications[1][1] = u'ألفان';
		self.complications[1][2] = u'ألفين';
		self.complications[1][3] = u'آلاف';
		self.complications[1][4] = u'ألف';

		self.complications[2][1] = u'مليونان';
		self.complications[2][2] = u'مليونين';
		self.complications[2][3] = u'ملايين';
		self.complications[2][4] = u'مليون';

		self.complications[3][1] = u'ملياران';
		self.complications[3][2] = u'مليارين';
		self.complications[3][3] = u'مليارات';
		self.complications[3][4] = u'مليار';

##    """
##     * Set feminine flag of the counted object
##     *
##     * @param integer value Counted object feminine (1 for masculine & 2 for feminine)
##     *
##     * @return boolean True if success, or False if fail
##     * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
##     """
	def setFeminine(self,value):
		flag = True;
		if (value == 1 or value == 2):
			self._feminine = value;
		else:
			flag = False;
		return flag;

##    """
##     * Set the grammar position flag of the counted object
##     *
##     * @param integer value Grammar position of counted object
##     *                       (1 if Marfoua & 2 if Mansoub or Majrour)
##     *
##     * @return boolean True if success, or False if fail
##     * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
##     """
	def setFormat(self,value):
		flag = True;

		if (value == 1 or value == 2):
			self._format = value;
		else:
			flag = False;
		return flag;


##"""
##     * Get the feminine flag of counted object
##     *
##     * @return integer return current setting of counted object feminine flag
##     * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
##"""
	def getFeminine(self):
		return self._feminine;
	"""
     * Get the grammer position flag of counted object
     *
     * @return integer return current setting of counted object grammer
     *                 position flag
     * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
     """
	def getFormat(self):
		return self._format;

##    """
##     * Spell integer number in Arabic idiom
##     *
##     * @param integer number        The number you want to spell in Arabic idiom
##     * @param string  outputCharset (optional) Output charset [utf-8|windows-1256|iso-8859-6]
##     *                               default value is None (use set output charset)
##     * @param object  main          Main Ar-PHP object to access charset converter options
##     *
##     * @return string The Arabic idiom that spells inserted number
##     * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
##     """
	def int2str(self,number, outputCharset = None, main = None):
##		temp = (trunc(number), number-trunc(number));
		temp = number.split('.');
		string = self._int2str(temp[0]);
		if (len(temp)>1):
			dec = self._int2str(temp[1]);
			string += u' فاصلة ' + dec;
		if (main):
			if (outputCharset == None):
				outputCharset = main.getOutputCharset();
			string = main.coreConvert(string, 'utf-8', outputCharset);
		return string;

	"""
	 * Spell integer number in Arabic idiom
	 *
	 * @param integer number The number you want to spell in Arabic idiom
	 *
	 * @return string The Arabic idiom that spells inserted number
	 * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
	 """
	def _int2str(self,number):
		blocks = [];
		items = [];
		string = u'';
		number = number;#trunc(int(number)) #(int)number);
		try:
			newnumber=int(number);
		except:
			number="0";
		if (int(number) > 0):
			while (len(number) > 3):
				blocks.append( number[-3:]);
				number = number[:len(number) - 3];
			blocks.append(number);
			blocks_num = len(blocks) - 1;
			i=blocks_num;
			while i>=0:#(i = blocks_num; i >= 0; i--) :
				number = math.floor(int(blocks[i]));
				text = self._writtenBlock(number);
				if (text) :
					if (number == 1 and i != 0) :
						text = self.complications[i][4];
					elif (number == 2 and i != 0) :
						text = self.complications[i][self._format];
					elif (number > 2 and number < 11 and i != 0) :
						text += u' ' + self.complications[i][3];
					elif (i != 0) :
						text += u' ' + self.complications[i][4];
					items.append(text);
				i-=1;
			string = u' و '.join(items);
		else :
			string = u'صفر';
		return string;

	"""
	 * Spell sub block number of three digits max in Arabic idiom
	 *
	 * @param integer number Sub block number of three digits max you want to
	 *                        spell in Arabic idiom
	 *
	 * @return string The Arabic idiom that spells inserted sub block
	 * @author Khaled Al-Shamaa <khaled.alshamaa@gmail.com>
	 """
	def _writtenBlock(self,number):
		items = [];
		string = u'';
		number=int(number)
		if (number > 99):
			hundred = math.floor(number / 100) * 100;
			number = number % 100;

			if (hundred == 200):
				items.append( self._individual[hundred][self._format]);
			else:
				items.append( self._individual[hundred]);
		if (number == 2 or number == 12):
			items.append( self._individual[number][self._feminine][self._format]);
		elif (number < 20):
			items.append(self._individual[int(number)][self._feminine]);
		else :
			ones = number % 10;
			tens = math.floor(number / 10) * 10;
			tens=int(tens);

			if (ones == 2) :
				items.append(self._individual[ones][self._feminine][self._format]);
			elif (ones > 0) :
				items.append( self._individual[ones][self._feminine]);
			items.append( self._individual[tens][self._format]);

		if u'' in items: items.remove(u'');
		string = u' و '.join(items);
		return string;
	def text2number(text):
		"""
		Convert arabic text into number, for example convert تسعة وعشرون  =>29.
		@param text: input text
		@type text: unicode
		@return : number extracted from text
		@rtype: integer
		>>> text2number(u"خمسمئة وثلاث وعشرون");
		523
		"""
		#the result total is 0
		total=0;
		# the partial total for the three number
		partial=0;
		words=text.split(' ');
		for word in words:
			if ThaousandMultiple.has_key(word):
				total+=partial* ThaousandMultiple[word];
				#re-initiate the partial total
				partial=0;
			if NumberWords.has_key(word):
				partial+=NumberWords[word];
		# add the final partial to total
		total+=partial;		
		return total

def text2number(text):
	"""
	Convert arabic text into number, for example convert تسعة وعشرون  =>29.
	@param text: input text
	@type text: unicode
	@return : number extracted from text
	@rtype: integer
	>>> text2number(u"خمسمئة وثلاث وعشرون");
	523
	"""
	#the result total is 0
	total=0;
	# the partial total for the three number
	partial=0;
	text=araby.stripTashkeel(text);
	words=text.split(u' ');
	#print words;
	for word in words:
		if word and word!=u'واحد' and word[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
			word=word[1:];
		if word!=u'واحد' and word.startswith(u'و'):
			word=word[1:];
			
		if NumberWords.has_key(word):
			actualnumber=NumberWords[word];
			if actualnumber%1000==0:
				# the case of 1000 or 1 million
				if partial==0: partial=1;
				total+=partial* actualnumber;
				#re-initiate the partial total
				partial=0;				
			else: partial+=NumberWords[word];
	# add the final partial to total
	total+=partial;		
	return total
def vocalizeNumber(wordlist, synTags=""):
	""" Vocalize a number words
	@param wordlist: words to vocalize
	@type wordlist: unicode list
	@param synTags: tags about the clause
	@type synTags: unicode
	@return: the vocalized wordlist.
	@rtype: unicode
	"""
	newlist=[];
	prefix=u"";
	next=u"";
	#detect tags 
	# we can pass tags to this number word
	tags= synTags;
	majrour = False;
	if len(wordlist)==1:
		#return araby.stripTashkeel(wordlist[0]);
		word=wordlist[0];
		word_nm=araby.stripTashkeel(word);
		key=word_nm;
		voc=word;
		# the first word can have prefixes 
		if word_nm and not wordlist and word_nm!=u'واحد' and word[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
			if word_nm[0] in (u'ل', u'ب', u'ك'):
				tags +=u"مجرور";
			key=word[1:];
		elif word_nm!=u'واحد' and word_nm.startswith(u'و'):
			key=word_nm[1:];
		# تحذب بعض الكلمات لأنها تلتبس مع أسماء الأجزاء مثل خُمس وخمس
		if NumberWords.has_key(key) and not key in (u'عشر',u'خمس',u'سبع', u'تسع',u'خمسا', u'سبعا',u'تسعا',u'عشرا', u'ألفين',u'عشرة', u'صفر', u'ألف'):
			voc =prefix+VocalizedNumberWords[key]['i']
		return [voc,];
	for i in range(len(wordlist)):
		#save the original word with possible harakat if exist
		word=wordlist[i];
		word_nm=araby.stripTashkeel(word);
		key=word_nm;
		# the first word can have prefixes 
		if i==0 and word_nm and word_nm!=u'واحد' and word[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
			if word_nm[0] in (u'ل', u'ب', u'ك'):
				tags +=u"مجرور";
			key=word[1:];
		elif word_nm!=u'واحد' and word_nm.startswith(u'و'):
			key=word_nm[1:];
		if NumberWords.has_key(key):
			if word_nm.endswith(u'ين') : 
				tags +=u"مجهول"; # إما مجرور أو منصوب
			elif word_nm.endswith(u'ان')  or word_nm.endswith(u'ون') :
				tags +=u"مرفوع";
	#add tashkeel 
	#wordlist=araby.stripTashkeel(u" ".join(wordlist)).split(' ');
	previousKey=u'';
	for i in range(len(wordlist)):
		word =wordlist[i];
		if i+1<len(wordlist):
			next=wordlist[i+1];
		else: next =u"";
		key=word;
		# the first word can have prefixes 
		if word and word!=u'واحد' and word[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
			key=word[1:];
			prefix=word[0];
			if prefix in  (u'و', u'ف',  u'ك'):
				prefix +=u'َ'
			elif prefix in  ( u'ل', u'ب'):
				prefix +=u'ِ'
		else: prefix='';
		if VocalizedNumberWords.has_key(key):
			voc=u'';
			if VocalizedNumberWords[key]['s']=="*":
				voc =prefix+VocalizedNumberWords[key]['i']

			# مبني على النصب في حالة المركب العددي
			elif next==u'عشر' or next==u'عشرة':
					voc =prefix+VocalizedNumberWords[key]['n']
			# مبني على النصب في حالة المركب العددي
			elif key==u'عشر' and previousKey in NumberTenMasculinUnits:
					voc =u'عَشَرَ'
			elif key==u'عشرة' and previousKey in NumberTenFemininUnits:
					voc =u'عَشْرَةَ'

			elif u'مرفوع' in tags:
				if next.startswith(u'و'):
					voc =prefix+VocalizedNumberWords[key]['r2']
				else:		
					voc =prefix+VocalizedNumberWords[key]['r']
			elif u'مجهول' in tags:
				voc =prefix+VocalizedNumberWords[key]['i']
			
			elif u'مجرور' in tags:
				if next.startswith(u'و'):
					voc =prefix+VocalizedNumberWords[key]['j2']
				else:		
					voc =prefix+VocalizedNumberWords[key]['j']
			# منصوب
			elif u'منصوب' in tags:
				if next.startswith(u'و'):
					voc =prefix+VocalizedNumberWords[key]['n2']
				else:		
					voc =prefix+VocalizedNumberWords[key]['n']			
			else:
				voc =prefix+VocalizedNumberWords[key]['i'] 
			newlist.append(voc)		
		else:
			newlist.append(prefix+key);
		previousKey=key;
	return newlist;

def isUnit(word):
	"""
	return if the given word is a unit
	@param word: given word to be tested
	@type word: unicode
	@return: if word is a unit return True else False.
	@rtype: Boolean
	"""
	return UnitWords.has_key(word);
	
def vocalizeUnit(numeric, unit):
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
	unit_nm = araby.stripTashkeel(unit);
	if not isUnit(unit_nm):
		return unit;
	tags= u"";
	vocalizedUnit=unit;

	# العدد بين واحد واثنان يتطلب صفة للوحدة ويكون بعدها
	# هذه الحالة لا تبرمج

	if numeric>=0 and numeric <=2:
		return unit;
	# الإضافة إلى تمييز مضاف  إليه مجرور مفرد
	# تممييز الألف والمئة والمليون والمليار 
	# يتطلب إضافة إلى مفرد
	# مثلا ألف رجل
	elif  numeric % 100 == 0 or  numeric % 1000 == 0:
		
		tag='SingleMajrour';
		vocalizedUnit = UnitWords[unit_nm]['a'];
	# العدد المفرد يتطلب 
	# إضافة إلى الجمع
	elif numeric % 100 <=10:
		tags+="Plural";
		vocalizedUnit = UnitWords[unit_nm]['p'];

	elif numeric % 100 <100:
		tags+='SingleMansoub';
		vocalizedUnit = UnitWords[unit_nm]['n'];
	else:
		tags='';
		vocalizedUnit = UnitWords[unit_nm]['i'];
	if not vocalizedUnit:
		return 'Error'+tags;
	else:
		return vocalizedUnit;


def getPreviousTag(word):
	"""Get the word tags
	@param word: given word
	@type word: unicode
	@return :word tag
	@rtype: unicode
	"""
	word=araby.stripTashkeel(word);
	tags=u'';
	if word in NOUN_NASEB_LIST:
		return u'منصوب';
	elif word in JAR_LIST:
		return u'مجرور';
	elif word in RAFE3_LIST:
		return u'مرفوع';
	else:
		return u'';
def extractNumberPhrases(text):
	"""
	Extract number words in a text.
	@param text: input text
	@type text: unicode
	@return : number words extracted from text
	@rtype: integer
	>>> extractNumberPhrases(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا");
	خمسمئة وثلاثة وعشرين
	ثلاثة عشر 
	"""
	phrases=[];

	wordlist = araby.tokenize(text)#text.split(' ');
	positions= detectNumberPhrasesPosition(wordlist);

	for pos in positions:
		if len(pos)>=2:
			if pos[0]<=len(wordlist) and pos[1]<=len(wordlist):
				phrases.append(u' '.join(wordlist[pos[0]: pos[1]+1]))
	return phrases;
def extractNumberPhrasesWithinContext(text):
	"""
	Extract number words in a text.
	@param text: input text
	@type text: unicode
	@return : number words extracted from text
	@rtype: integer
	>>> extractNumberPhrasesWithinContext(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا");
	وجدت، خمسمئة وثلاثة وعشرين، دينارا
	 فاشتريت، ثلاثة عشر ، دفترا
	"""
	phrases=[];
	wordlist = araby.tokenize(text);
	positions= detectNumberPhrasesPosition(wordlist);

	for pos in positions:
		if len(pos)>=2:
			if pos[0]<=len(wordlist) and pos[1]<=len(wordlist):
				if pos[0]-1>=0: 
					previous= wordlist[pos[0]-1];
				else: previous=u'';
				if pos[1]+1<len(wordlist): 
					next= wordlist[pos[1]+1];
				else: next=u'';
				phrases.append((previous, u' '.join(wordlist[pos[0]: pos[1]+1]), next))
	return phrases;

def detectNumberPhrasesPosition(wordlist):
	"""
	Detect number words in a text and return positions of each phrase.
	@param wordlist: wordlist
	@type wordlist: unicode list
	@return : list of numbers clause positions [(start,end),(start2,end2),]
	@rtype: list of tuple
	>>> detectNumberPhrasesPosition(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا");
	(1،3)، (6،7)
	"""
	wordlist#=text.split(u' ');
	#print words;
	phrases = [];
	startNumber =-1;
	endNumber   =False;
	for i in range(len(wordlist)):
		word=wordlist[i];
		if i+1<len(wordlist):
			next=araby.stripTashkeel(wordlist[i+1]);
		else: next=None;
		#save the original word with possible harakat if exist
		word_nm=araby.stripTashkeel(word);
		key=word_nm;
		# the first word can have prefixes 
		if word_nm and not startNumber and word_nm!=u'واحد' and word_nm[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
			key=word_nm[1:];
		elif word_nm!=u'واحد' and word_nm.startswith(u'و'):
			key=word_nm[1:];
		if NumberWords.has_key(key):
			if not key in (u'أحد',u'إحدى',u'اثنا',u'اثني', u'اثنتي', u'اثنتا') or next in (u'عشر', u'عشرة'):
				if startNumber<0:
					startNumber = i;
				endNumber = i;
			# phrase.append(word);
		else:
			if startNumber>=0: #There are a previous number phrase.
				phrases.append((startNumber, endNumber));
			startNumber=-1;
	# add the final phrases 
	if startNumber>=0: #There are a previous number phrase.
		phrases.append((startNumber, endNumber));
	return phrases

def detectNumberWords(text):
	"""
	Detect number words in a text.
	@param text: input text
	@type text: unicode
	@return : number words extracted from text
	@rtype: integer
	>>> text2number(u"وجدت خمسمئة وثلاثة وعشرين دينارا");
	خمسمئة وثلاثة وعشرين
	"""

	words=araby.tokenize(text)
	#print words;
	phrasesContext=extractNumberPhrasesWithinContext(text);
	for phCon in phrasesContext:
		if len(phCon)>=3:
			previous=phCon[0];
			phrase=phCon[1];
			next=phCon[2];
			numberedwords=phrase;
			numeric = text2number(numberedwords);
			tags = getPreviousTag(previous);
			vocalized = vocalizeNumber(araby.stripTashkeel(numberedwords).split(' '), tags);				
			#calcul  vocalization similarity : 
			sim = araby.vocalizedSimilarity(numberedwords, vocalized);
			vocUnit=vocalizeUnit(numeric, next);
			simUnit = araby.vocalizedSimilarity(vocUnit, next);					
			if sim<0:
				print u'\t'.join([str(sim), numberedwords, vocalized, str(numeric), u' '.join([previous,phrase, next]), next, vocUnit, str(simUnit)]).encode('utf8');

def preTashkeelNumber(wordlist):
	"""
	Detect number words in a text.
	@param wordlist: input text
	@type wordlist: unicode
	@return : wordlist with vocalized number clause
	@rtype: list
	>>> preTashkeelNumber(u"وجدت خمسمئة وثلاثة وعشرين دينارا");
	وجدت خمسمئة وثلاثة وعشرين دينارا
	"""

	positions= detectNumberPhrasesPosition(wordlist);
	for pos in positions:
		if len(pos)>=2:
			startPos=pos[0];
			endPos= pos[1];
			if startPos<=len(wordlist) and endPos<=len(wordlist):
				# get the context of current number phrase
				if startPos-1>=0:  previous= wordlist[startPos-1];
				else: previous=u'';
				if endPos+1<len(wordlist): 	next= wordlist[endPos+1];
				else: next=u'';
				#get the tag of previous word
				tags = getPreviousTag(previous);
				vocalized = vocalizeNumber(wordlist[startPos: endPos+1], tags);				
				wordlist = wordlist[:startPos] + vocalized  +wordlist[endPos+1:]
	return wordlist;
if __name__ == '__main__':
	#import number as ArabicNumberToLetters
	texts=[u"مليونان وألفان وإثنا عشر", 
	u"جاء مليونان وألفان وإثنا عشر", 
	u"وجدت خمسمئة وثلاث وعشرون دينارا",
		u"خمسمئة وثلاث وعشرون دينارا",
	u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا",
	u"لم أجد شيئا",
	u'من ثلائمئة وخمسين بلدا ',
		u'من ثلاثمئة وخمسين بلدا ',
	u'من أربعمئة وخمسين بلدا ',
	];
	for text in texts:
		# result = detectNumberWords(text);
		# print u";".join(result).encode('utf8');
		positions= detectNumberPhrasesPosition(araby.tokenize(text));
		print positions;
		phrases = extractNumberPhrases(text);
		print text.encode('utf8');
		print u'\t'.join(phrases).encode('utf8');
