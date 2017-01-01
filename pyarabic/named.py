#!/usr/bin/python2
# -*- coding=utf-8 -*-
#
import re, string,sys
sys.path.append('../lib')
import pyarabic.araby as araby
import named_const
import propernouns
# from number import *
DineNamed=(
u'شمس',
u'تقي',
u'علاء',
u'نجم',
u'نور',
u'سيف',
#u'',
#u'',

)
def isProperNoun(word):
	"""
	Test if the word is a proper noun
	@param word: given word
	@type word: unicode
	@return: True if is properword
	@rtype: Boolean
	"""
	# return word in named_const.ProperNouns;
	return propernouns.ProperNouns.has_key(word);	

def detectNamedPosition(wordlist):
	"""
	Detect named enteties words in a text and return positions of each phrase.
	@param wordlist: wordlist
	@type wordlist: unicode list
	@return : list of numbers clause positions [(start,end),(start2,end2),]
	@rtype: list of tuple
	>>> detectNamedPosition(u"قال خالد بن رافع  حدثني أحمد بن عنبر عن خاله");
	((1,3), (6,8))
	"""
	wordlist#=text.split(u' ');
	#print words;
	positions = [];
	startNamed =-1;
	endNamed   =False;
	# print u":".join(wordlist).encode('utf8');
	for i in range(len(wordlist)):
		word=wordlist[i];
		if i+1<len(wordlist):
			next=araby.stripTashkeel(wordlist[i+1]);
		else: next=u''
		if i-1>=0: 
			previous=araby.stripTashkeel(wordlist[i-1]);
			if previous and startNamed<0  and previous[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
				previous=previous[1:];
		else: previous = u''
		#save the original word with possible harakat if exist
		word_nm=araby.stripTashkeel(word);
		key=word_nm;
		# the first word can have prefixes 
		if word_nm and startNamed<0  and word_nm[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
			key=word_nm[1:];
		if startNamed<0 and key in (u'ابن', ):
			startNamed=i;
			endNamed=i

		elif key in (u'ابن', u'بن',u'أبو',u'أبا', u'أبي', u'عبد' , u'عبيد' , u'بنو', u'بني', u'بنت'):
			if startNamed<0:
				startNamed=i;
			endNamed=i
	
		elif previous in (u'بن', u'ابن', u'أبو',u'أبا', u'أبي', u'عبد', u'عبيد', u'بنو', u'بني', u'بنت'):
			if startNamed<0:
				startNamed=i-1;
			endNamed=i
		elif next in (u'بن', u'بنت',): #  u'أبو', u'أبي', u'ابا',) :#or word in (u'الدين',):
			if startNamed<0:
				startNamed=i;
			endNamed=i
		# if the word is a proper noun
		elif startNamed<0 and isProperNoun(key):
			startNamed=i;
			endNamed=i
		else:
			if startNamed>=0: #There are a previous number phrase.
				if word_nm.startswith(u'ال') and word_nm.endswith(u'ي'):
					# add family name إضافة الكنية
					endNamed=i

				positions.append((startNamed, endNamed));
			startNamed=-1;
	# add the final phrases 
	if startNamed>=0: #There are a previous number phrase.
		positions.append((startNamed, endNamed));
	return positions

def extractNamed(text):
	"""
	Extract named enteties words in a text.
	@param text: input text
	@type text: unicode
	@return : named enteties words extracted from text
	@rtype: integer
	>>> extractNamed(u"قال خالد بن رافع  حدثني أحمد بن عنبر عن خاله");
	("خالد بن رافع"، "أحمد بن عنبر ")
	"""
	phrases=[];
	wordlist = araby.tokenize(text);
	positions= detectNamedPosition(wordlist);

	for pos in positions:
		if len(pos)>=2:
			if pos[0]<=len(wordlist) and pos[1]<=len(wordlist):
				phrases.append(u' '.join(wordlist[pos[0]: pos[1]+1]))
	return phrases;
	

def extractNamedWithinContext(text):
	"""
	Extract number words in a text.
	@param text: input text
	@type text: unicode
	@return : number words extracted from text
	@rtype: integer
	>>> extractNumberPhrasesWithinContext(u"تصدق عبد الله بن عمر بدينار");
	("تصدق"، "عبد الله بن عمر"، "بدينار")
	"""
	phrases=[];
	wordlist = araby.tokenize(text);
	positions= detectNamedPosition(wordlist);	
	for pos in positions:
		# print pos;
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

def detectNamed(text):
	"""
	Detect named enteties in a text
	@param text: input text
	@type text: unicode
	@return : extract named enteties
	@rtype: integer
	>>> text2number(u"وجد  عبد الله بن عمر دينارا");
	عبد الله بن عمر
	"""
	words=araby.tokenize(text);
	#print words;
	phrase  = [];
	phrases = [];
	tags= u"";	
	majrour = False;
	previous=u"";
	for i in range(len(words)):
		word = words[i];
		if i+1<len(words): next = words[i+1];
		else: next= u"";
		key=word;
		# the first word can have prefixes 
		if not phrase and word and word[0] in (u'و', u'ف', u'ل', u'ب', u'ك'):
			key=word[1:];


			
		if not phrase and key in (u'ابن', ):
			phrase.append(word);

		elif key in (u'بن',u'أبو',u'أبا', u'أبي', u'عبد' , ):
			phrase.append(word);
	
		elif previous in (u'بن', u'ابن', u'أبو',u'أبا', u'أبي', u'عبد',):
			phrase.append(word);
		elif next in (u'بن',  u'عبد' , u'أبو', u'أبي') and word in (u'الدين',):
			phrase.append(previous);
			phrase.append(word);
		elif next in (u'بن', ) :
			phrase.append(word);
		else:
			if len(phrase)>=1:
				if word.startswith(u'ال') and word.endswith(u'ي'):
					phrase.append(word);
				phrases.append(u" ".join(phrase));
			phrase=[];
		previous = key;
	# add the final phrases 
	if phrase: phrases.append(u" ".join(phrase));
	return phrases
	
def getPreviousTag(word):
	"""Get the word tags
	@param word: given word
	@type word: unicode
	@return :word tag
	@rtype: unicode
	"""
	word=araby.stripTashkeel(word);
	tags=u'';
	if word in named_const.NOUN_NASEB_LIST:
		return u'منصوب';
	elif word in named_const.JAR_LIST:
		return u'مجرور';
	elif word in named_const.RAFE3_LIST:
		return u'مرفوع';
	else:
		return u'';

def vocalizeNamed(wordlist, synTags=""):
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
	bin_count=0;
	for i in range(len(wordlist)):
		#save the original word with possible harakat if exist
		word=wordlist[i];
		word_nm=araby.stripTashkeel(word);
		# the first word can have prefixes 
		if i==0 and word_nm:  
			# word to get majrour tag
			if word_nm in (u'أبي', u'بنو', u'آل', u'ابن',):
				tags +=u"مجرور";
			elif word_nm in (u'أبو', ):
				tags +=u"مرفوع";
			elif word_nm in (u'أبا', ):
				tags +=u"منصوب";
		# select vocalization

		if word_nm==u'بن':
			bin_count+=1;
			#treat first bin according to tags
			if bin_count==1:
				if u'مجرور' in tags:
					voc=u'بْنِ'
				elif u'مرفوع' in tags:
					voc=u'بْنُ'
				elif u'منصوب' in tags:
					voc=u'بْنَ'
				else:
					voc=u'بْن'
			else:
				#  u'مجرور' 
				voc=u'بْنِ'
		#Todo Vocalize names
		else:
			voc=word;
		newlist.append(voc);
	return newlist;

def preTashkeelNamed(wordlist):
	"""
	Detect named words in a text.
	@param wordlist: input text
	@type wordlist: unicode
	@return : wordlist with vocalized named clause
	@rtype: list
	>>> preTashkeelNumber(u"وجدت خمسمئة وثلاثة وعشرين دينارا");
	وجدت خمسمئة وثلاثة وعشرين دينارا
	"""

	positions= detectNamedPosition(wordlist);
	#print positions
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
				vocalized = vocalizeNamed(wordlist[startPos: endPos+1], tags);				
				#print u' '.join(vocalized).encode('utf8');
				wordlist = wordlist[:startPos] + vocalized  +wordlist[endPos+1:]
	return wordlist;

if __name__ == '__main__':
	#import number as ArabicNumberToLetters
	texts=[
	u"وجد عبد الله بن عمر دينارا",
	
	u"جاء  خالد بن الوليد وقاتل مسيلمة بن حذام الكذاب في موقعة الحديقة", 
	u'روى أحمد بن عقيل الشامي عن أبي طلحة المغربي أنّ عقابا بن مسعود بن أبي سعاد قال',
	u"""
6 :* حَديثُ عَمٍّ: فَرَجُ سَقْفِ بَيْتِي وَأَنَا بِمَكَّةٍ ، فَنَزَلَ جِبْرِيلُ ، فَفَرَجُ صَدْرِي ، ثُمَّ غَسَلَهُ مِنْ مَاءِ زَمْزَمَ ، ثُمَّ جَاءَ بِطَسْتِ مَمْلُوءِ حِكْمَةِ وَإيمَانَا فَأُفْرِغُهَا فِي صَدْرِي ، ثُمَّ أَطُبِّقَهُ قَالَ عَبْدُ اللهِ بْن أَحَمْدٌ: حَدِّثِنَّي مُحَمَّدَ بْن عَبَّادٍ الْمَكِّيُّ ، ثِنَا أَبُو ضَمْرَةٌ ، عَنْ يُونِسٍ ، عَنِ الزَّهْرِيِ ، عَنْ أُنْسٍ: كَانَ أَبِي يُحَدِّثُ بِمَا هُنَا وَحَدِّثِنَّي مُحَمَّدَ بْن إسحاق بْن مُحَمَّدِ المسيبي ، ثِنَا أَنَسُ بْن عياض ، عَنْ يُونُسُ بْن يَزِيدُ ، قَالٌ: قَالَ اِبْنُ شِهَابٍ: قَالَ أَنَسُ بْن مَالِكٍ: كَانَ أَبِي بْن كَعْبِ يَحْدُثُ ، فَذُكِرَ حَديثُ الْإِسْراءِ بِطُولِهِ ، وَفِيه: قَالَ الزُّهْرِيُّ: وَأَخْبَرَنِي اِبْنُ حَزْمٍ ، أَنَّ اِبْنَ عَبَّاسٍ ، وَأَبَا حَبَّةُ الْأَنْصارِيِ يَقُولَانِّ: قَالَ رَسُولُ اللهِ ، صَلَّى اللهُ عَلَيه وَسَلَّمُ: ثَمَّ عَرَجِ بِي حَتَّى ظَهَرْتِ لِمُسْتَوى أَسْمَعُ صَرِيفَ الْأَقْلاَمِ وَفِيه قَالَ الزُّهْرِيُّ: قَالَ اِبْنُ حَزْمٍ ، وَأَنَسُ بْن مَالِكٍ: قَالَ رَسُولُ اللهِ صَلَّى اللهُ عَلَيه وَسَلَّمُ: فَرَضَ اللَّهُ عَلَى أمتي خَمْسِينَ صَلاَةٌ ، فَرَجَعْتِ بِذَلِكَ حَتَّى أَمْرِ عَلَى مُوسى الْحَديثِ ، تَفْرُدُ بِهِ .( 1 / 6)
2	71.16%	83.07%	92	54	154	319	69.85%	81.62%	 28: حَديثُ كَمْ حَمُ: فِي هَذِهِ الْآيَةَ :{ وَإِذْ أَخَذَ رَبُّكَ مِنْ بُنِّيِّ آدَمِ مِنْ ظُهورِهُمْ ذَرِّيَّتِهُمْ } الْآيَةُ ، قَالٌ: جَمْعُهُمْ لَهُ يَوْمَئِذٍ جَمِيعًا فَجَعَلَهُمْ أَرَواحًا ثَمَّ صُورِهُمْ وَاِسْتَنْطَقُهُمْ الْحَديثِ ، وَفِيه قَوْلُ آدَمِ: رُبَّ لَوْ سُوِّيتِ بَيْنَ عِبَادِكَ ، قَالٌ: إِنَِّي أَحُبَّ أَنْ أَشْكَرَ ، وَفِيه ذِكْرُ عِيسَى اِبْنُ مَرْيَمٍ ، وَقَوْلُ أَبِي بْن كَعْبٍ: إِنَّ الرَّوْحَ دُخِلَ مِنْ فِي مَرْيَمِ كَمْ فِي تَفْسِيرِ الْأَعْرَافِ: أَنَا أَبُو جَعْفَرٍ مُحَمَّدُ بْن عَلِيٍّ الشَّيْبانِيُّ ، أَنَا أَحُمِدَ بْن حازِمٍ ، ثِنَا عَبِيدَ اللهِ بْن مُوسى ، ثِنَا أَبُو جَعْفَرٌ ، عَنِ الرَّبِيعُ بْن أُنْسٍ ، عَنْ أَبِي الْعَالِيَةَ ، عَنْ أَبِي بِطُولِهِ وَرَوَاهُ عَبْدُ اللهِ بْن أَحَمْدَ فِي زِيادَاتِهِ: حَدِّثِنَّي مُحَمَّدَ بْن يَعْقُوبِ الرَّبالِيِ ، ثِنَا الْمُعْتَمِرُ بْن سَلِيمَانِ ، سَمِعْتِ أَبِي يُحَدِّثُ عَنِ الرَّبِيعِ ، بِهِ.
3	72.39%	85.31%	156	83	242	565	73.98%	88.21%	 44 :* حَديثُ حُبِّ حَمُ عَمٌّ: قَالَ لِي جِبْرِيلُ :{ قُلْ أَعُوذُ بِرَبِّ الْفَلْقِ } فَقِلْتِهَا الْحَديثَ حُبٌّ: فِي الْعَشْرَيْنِ مِنَ الثَّالِثِ: أَنَا عِمْرَانُ بْن مُوسى ، ثِنَا هُدْبَةُ بْن خَالِدٍ ، ثِنَا حَمَّادُ بْن سلمةٍ ، عَنْ عَاصِمٍ ، عَنْ زِرٍّ: قُلْتِ لِأَبِي بْن كَعْبٍ: إِنَّ اِبْنَ مَسْعُودِ لَا يَكْتُبْ فِي مُصْحَفِهِ المعوذتين فَقَالَ أَبِي: قَالَ لِي رَسُولُ اللهِ: قَالَ لِي جِبْرِيلُ فَذَكَرَهُ رَوَاهُ أَحْمَدُ: عَنْ أَبِي بِكَرِّ بْن عَيّاشٍ ، عَنْ عَاصِمِ بِلَفْظٍ: قُلْتِ لِأَبِي: إِنَّ عَبْدَ اللهِ يَقُولُ فِي المعوذتين فَقَالَ أَبِي: سَأَلَنَا عَنْهُمَا رَسُولُ اللهِ ، فَقَالٌ: قَيَّلَ لِي: قَلَّ وَأَنَا أَقُولُ كَمَا قَالَ وَعَنْ وكيع ، وَعَبْدُ الرَّحْمَنِ بْن مَهْدِي كِلَاهُمَا ، عَنْ سُفْيانٍ ، وَعَنْ مُحَمَّدِ بْن جَعْفَرٍ ، عَنْ شُعْبَةِ وَعَنْ عَفّانٍ ، عَنْ حَمَّادُ بْن سلمةٍ ، وَأَبِي عَوانَةٌ ، فَرَقَهُمَا ، كلَهُمْ عَنْ عَاصِمِ وَعَنْ سُفْيانِ بْن عيينة ، عَنْ عَبْدَةُ بْن أَبِي لُبَابَةٌ ، وَعَاصِمُ وَعَنْ عَبْدِ الرَّحْمَنِ بْن مَهْدِيٍّ ، عَنْ سُفْيانٍ ، عَنِ الزُّبَيْرِ بْن عِدِّيِ ، عَنْ أَبِي رَزينٌ ، ثلاثتهم عَنْ زِرِّ وَقَالَ عَبْدُ اللهِ: حَدِّثِنَّي مُحَمَّدَ بْن الحسين بْن إشكاب ، ثِنَا مُحَمَّدَ بْن أَبِي عُبَيْدَةُ بْن مِعْنَ ، ثِنَا أَبِي ، عَنِ الْأعْمَشِ ، عَنْ أَبِي إسْحَاقُ ، عَنْ عَبْدِ الرَّحْمَنِ بْن يَزِيدُ ، قَالٌ: كَانَ عَبْدُ اللهِ يَحُكُّ المعوذتين مِنْ مَصَاحِفِهِ وَيَقُولُ: إِنَّهُمَا لَيْسَتَا مِنْ كِتَابِ اللهِ قَالِ الْأعْمَشِ: وَثَنَا عَاصِمُ ، عَنْ زِرِّ فَذكرِ نَحْوَ الْأَوَّلِ .( 1 / 16)
4	74.60%	85.77%	207	116	321	815	79.60%	86.80%	 54 :* حَديثُ كَمْ حَمُ عَمٌّ: إِذَا كَانَ يَوْمُ الْقِيَامَةِ كِنْتِ إمَامَ النَّبِيِّينَ وَخَطِيبُهُمْ وَصَاحِبُ شَفَاعَتِهُمْ ، غَيْرَ فَخْرُ كَمْ فِي الْإيمَانِ: ثِنَا الْحُسَيْنُ بْن الْحُسْنِ الطَّوْسِيِ ، ثِنَا أَبُو حاتِمٍ الرّازِيُّ ، ثِنَا عَبْدَ اللهِ بْن جَعْفَرٍ الرَّقِّيُّ ، ثِنَا عَبِيدَ اللهِ بْن عَمْروِ وَعَنْ مُحَمَّدِ بْن صَالِحِ بْن هَانِئٍ ، ثِنَا السَّرِيُّ بْن خَزِيمَةٍ ، ثِنَا أَبُو حُذَيْفَةُ النَّهْدِيِ ، ثِنَا زُهَيْرُ بْن مُحَمَّدٍ ، كِلَاهُمَا عَنْ عَبْدِ اللهِ بْن مُحَمَّدِ بْن عَقِيلٍ ، عَنِ الطفيل بْن أَبِي بْن كَعْبٍ ، عَنْ أَبِيه ، بِهِ وَقَالٌ: صَحِيحُ الْإِسْنادِ وَلَمْ يُخْرِجَاهُ لِتَفَرُّدِ اِبْنِ عَقِيلِ بِهِ لَمَّا نَسْبِ إِلَيه مِنْ سُوءِ الْحِفْظِ ، وَهُوَ عِنْدَ أئِمَّتُنَا مِنَ الْمُتَقَدِّمِينَ ثِقَةُ مَأْمُونِ وَفِي الْفَضَائِلِ: أَنَا الْقَطِيعِيُّ ، ثِنَا عَبْدَ اللهِ بْن أَحَمْدٌ ، حَدَّثَنِي أُبَيُّ ، ثِنَا عَبْدَ الرَّحْمَنِ ، وَهُوَ اِبْنُ مَهْدِيٍّ ، ثِنَا زُهَيْرُ بْن مُحَمَّدٍ ، عَنْ عَبْدِ اللهِ بْن مُحَمَّدٍ ، بِهِ وَرَوَاهُ الْإمَامُ أَحْمَدُ: عَنْ أَبِي عَامِرٌ ، عَنْ زُهَيْرٍ ، يَعْنِي: اِبْنُ مُحَمَّدٍ ، عَنْ عَبْدِ اللهِ بْن مُحَمَّدٍ ، بِهِ وَعَنْ زَكَرِيّا بْن عِدِّيِ ، وَأَحْمَدُ بْن عَبْدِ الْمَلِكِ الْحَرَّانِيِ ، كِلَاهُمَا عَنْ عَبِيدِ اللهِ بْن عَمْروٍ ، بِهِ وَعَنْ أَبِي أَحْمَدَ الزُّبَيْرِيُّ ، عَنْ شَرِيكِ ، عَنْ عَبْدِ اللهِ بْن مُحَمَّدٍ ، بِهِ وَرَوَاهُ اِبْنُهُ عَبْدُ اللهِ فِي زِيادَاتِهِ: حَدَّثَنِي عُبَيْدُ اللَّهِ الْقَوَارِيرِيُّ ، ثِنَا مُحَمَّدَ بْن عَبْدِ اللهِ بْن الزُّبَيْرِ ، ثِنَا شَرِيكُ ، بِهِ وَقَالَ أيضا: ثِنَا هَاشِمُ بْن الْحارِثِ ، ثِنَا عَبِيدَ اللهِ بْن عَمْروٍ ، بِهِ وَحَدِّثِنَّي ( 1 / 24)
5	75.54%	85.94%	228	131	354	932	82.05%	87.18%	 56 :* حَديثُ كَمْ حَمُ: بَيَّنَا نَحْنُ فِي صَلاَةِ الظَّهيرَةِ وَالنَّاسَ فِي الصُّفُوفِ فَرَأَيْنَاهُ يَتَنَاوَلُ شِيئَا الْحَديثَ كَمْ فِي الْأَهْوَالِ: أَنَا عَبْدُ الرَّحْمَنِ بْن حَمْدانٍ ، ثِنَا هِلاَلُ بْن الْعَلاءِ ، ثِنَا أَبِي ، ثِنَا عَبِيدَ اللهِ بْن عَمْروٍ ، عَنْ عَبْدِ اللهِ بْن مُحَمَّدِ بْن عَقِيلٍ ، عَنِ الطفيل بْن أَبِي بْن كَعْبٍ ، عَنْ أَبِيه ، وَقَالٌ: صَحِيحُ الْإِسْنادِ رَوَاهُ أَحْمَدُ بِطُولِهِ: عَنْ أَحُمِدَ بْن عَبْدِ الْمَلِكِ بْن واقد الْحَرَّانِيِ ، عَنْ عَبِيدِ اللهِ بْن عَمْروٍ ، بِهِ قُلْتُ: رواه زَكَرِيّا بْن عِدِّيِ ، عَنْ عَبِيدِ اللهِ بْن عَمْروٍ ، فَقَالٌ: عَنْ عَبْدِ اللهِ بْن مُحَمَّدِ بْن عَقِيلٍ ، عَنْ جَابِرِ وَأَخْرَجَهُ أَحْمَدُ ، أيضا: عَنْ زَكَرِيّا.
6	75.46%	86.02%	265	151	403	1080	75.00%	86.49%	 68 :* عَبْدُ اللهِ بْن رباحٍ ، عَنْ أَبِي حَديثُ كَمْ م حَمُ عَمٌّ: قَالَ لِي رَسُولُ اللهِ ، صَلَّى اللهُ عَلَيه وَسَلَّمُ: أَيُّ آيَةِ فِي كِتَابِ اللهِ أُعْظِمُ ؟ قَالٌ: قُلْتِ :{ اللهُ لَا إلَهُ إلّا هُوَ الْحَيُّ الْقَيُّومَ } قَالٌ: فَضَرْبُ صَدْرِي وَقَالٌ: لِيَهِنُكَ الْعِلْمَ أَبَا الْمُنْذِرَ كَمْ فِي الْمَعْرِفَةِ: ثِنَا أَبُو عَبْدُ اللَّهِ الْحافِظُ ، ثِنَا إبراهيم بْن عَبْدِ اللهِ ، ثِنَا يَزِيدُ بْن هارُونٍ ، أَنَا الْجَرِيرِيِ ، عَنْ أَبِي السَّلِيلَ ، عَنْ عَبْدِ اللهِ بْن رباحٍ ، عَنْه ، بِهَذَا قُلْتُ: هُوَ فِي مُسْلِمٍ ، فَلَا يُسْتَدْرَكُ وَرَوْاهُ الْإمَامَ أَحْمَدُ: ثِنَا عَبْدَ الرَّزَّاقِ ، أَنَا سُفْيانٌ ، عَنْ سَعِيدُ الْجَرِيرِيِ ، بِهِ وَرَوَاهُ اِبْنُهُ عَبْدُ اللهِ ، فِي زِيادَاتِهِ: حَدَّثَنِي عُبَيْدُ اللَّهِ الْقَوَارِيرِيُّ ، ثِنَا جَعْفَرُ بْن سَلِيمَانِ ، ثِنَا الْجُرَيْرِيُّ ، عَنْ بَعْضُ أَصْحَابِهِ ، عَنْ عَبْدِ اللهِ بْن رباحٍ ، بِهِ.	
	""",
	u"قال مُحَمَّدُ بْنُ خَالِدُ بْنُ إسماعيلفي حديثه",
	u"ِنْصَرَفْنَا إِلَى أَنَسُ بْنُ مَالِكَ الْحَديثِ"
	];
	for text in texts:
		positions = detectNamedPosition(text.split(' '));
		print positions;
		# result=extractNamed(text);
		# print u"\t".join(result).encode('utf8');
		# result= extractNamedWithinContext(text);
		text=araby.stripTashkeel(text);
		result= preTashkeelNamed(araby.tokenize(text));
		print u' '.join(result).encode('utf8');
		# result=detectNamed(text);
		# print u"\t".join(result).encode('utf8');

