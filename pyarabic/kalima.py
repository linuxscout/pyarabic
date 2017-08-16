﻿#!/usr/bin/python
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
Kalima : Arabic word module
"""
import araby
class kalima:
	word=u'';
	letters=u"";
	marks= u""
	def __init__(self, word, marks=u""):
		"""
		Create Kalima object,
		if the marks is given, the word is considered as letters
		else the word is considered as vocalized
		"""
		if marks==u"":
			self.letters, self.marks = araby.separate(word);
			self.word=word;
		else:
			self.letters = word;
			self.marks   = marks;
			self.word=araby.joint(word, marks);
	#####################################
	#{ special methods
	#####################################
	
	def __hash__(self):
		return hash(self.letters+self.marks);
	def __repr__(self):
		return (u"(%s, %s)"%(self.letters,self.marks)).encode('utf8');
	def __str__(self):
		return self.word.encode('utf8');
	def __del__(self):
		pass;
	def __eq__(self, other):
		"""
		Compare two vocalized words,
		the two words are equal if they have the same letters and marks
		The two words are greater or equals if have the same letters and similar full or partial vocalization
		"""
	
		if self.letters==other.letters and self.marks==other.marks:
			return True;
		return False;
	def __ne__(self, other):
		"""
		Compare two vocalized words,
		the two words are equal if they have the same letters and marks
		The two words are greater or equals if have the same letters and similar full or partial vocalization
		"""
		if self.letters!=other.letters and self.marks!=other.marks:
			return True;
		return False;
	def __ge__(self, other):
		"""
		Compare two vocalized words,
		the two words are equal if they have the same letters and marks
		The two words are greater or equals if have the same letters and similar full or partial vocalization
		"""
		if self.letters==other.letters and len(self.marks)==len(other.marks):
			for i in range(len(self.marks)):
				if self.marks[i]==other.marks[i]:
					continue;
				elif self.marks[i]==araby.NOT_DEF_HARAKA or other.marks[i]==araby.NOT_DEF_HARAKA:
					continue;
				else:
					return False;
			return True;
		return False;
	def __le__(self, other):
		"""
		Compare two vocalized words,
		the two words are equal if they have the same letters and marks
		The two words are greater or equals if have the same letters and similar full or partial vocalization
		"""
	def __len__(self,):
		"""
		Get the word length without harakat.
		"""
		return len(self.letters);


		
	def __nonzero__(self,):
		"""
		Get the word length without harakat.
		"""
		return len(self.letters)!=0;
	
	def __setitem__(self, key, value):
		if key <=len(self.letters):
			self.letters[key]=value;

	def __getitem__(self, key):
		if key <=len(self.letters):
			return self.letters[key];
	def __getslice__(self, i, j):
		return self.letters[i:j];
	def __setslice__(self, i, j, seq):
		self.letters[i:j] = seq
	def __delslice__(self, i, j):
		del self.letters[i:j:]
		del self.marks[i:j:]		

	def __iadd__(self, other):
		self.letters+= other.letters;
		self.marks  += other.marks;
	def __add__(self, other):
		return kalima(self.letters + other.letters, self.marks  + other.marks);

	#####################################
	#{ Default attributes fucntions
	#####################################

	def setLetters(self, letters):	
		if letters:
			self.letters=letters;
	def getMarks(self):
		return self.marks;
	def setMarks(self,marks):
		if marks:
			self.marks= marks;
	def getVocalized(self,):
		return self.word;
	def getUnocalized(self,):
		return self.letters;
	def letter(self, key):
		""" get the specific letter by index number"""
		if key <=len(self.letters):
			return self.letters[key];
	def mark(self, key):
		""" get the specific mark by index number"""
		if key <=len(self.marks):
			return self.marks[key];
	#####################################
	#{ Has letter functions
	#####################################
	def hasShadda(self,):
		"""Checks if the arabic word  contains shadda.
		@param word: arabic unicode char
		@type word: unicode
		"""
		return araby.hasShadda(self.word);

	#####################################
	#{ word and text functions
	#####################################
	def isVocalized(self,):
		"""Checks if the arabic word is vocalized.
		the word musn't  have any spaces and pounctuations.
		@param word: arabic unicode char
		@type word: unicode
		"""
		return araby.isVocalized(self.word);
	def isArabic(self,):
		""" Checks for an valid Arabic  word.
		An Arabic word not contains spaces, digits and pounctuation
		avoid some spelling error,  TEH_MARBUTA must be at the end.
		@param word: input word
		@type word: unicode
		@return: True if all charaters are in Arabic block
		@rtype: Boolean
		"""
		return araby.isArabicword(self.word);
#To DO
""" How to represent Shadda
is shadda a letter or a mark
can we represent shadda as a third attributes
	- letters
	- marks
	- shadda
Can we represent the hamzat as same code
	- letters
	- marks
	- shadda
	- hamza
"""

if __name__ == "__main__":
	words=u"""مسلُم
	مسْلمٌ
	مسلّم
	شلامُ
	سِلام
	سَلام
	سكام
	سُكام
	سنام
	سُلَام
	سلامِ
	سلامٌ
	مسلّم
	مسلّم
	سيلم
	سليم"""
	words=words.split('\n');
	#words.sort();
	pkword=kalima(""); # previous word
	for word in words:
		word=word.strip(); #strip
		kword=kalima(word);
		print u"\t".join([word, str(hash(word)),  str(hash(kword)) ]).encode('utf8');
		print kword, pkword, len(kword),kword>=pkword, repr(kword);
		
		pkword=kword;
