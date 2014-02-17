#!/usr/bin/python
# -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        kalima
# Purpose:
#
# Author:      Taha Zerrouki
#
# Created:     11-12-2012
# Copyright:   (c) عبدة 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import araby
"""
Arabic module for arabic word kalima
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Taha Zerrouki
@license: GPL
@date:2012/12/12
@version: 0.1
"""
class kalima():
    def __init__(word):
        self.vocalized = word;
        self.letters, self.marks= araby.separate(word);
    pass;
    #####################################
    #{Letter functions
    #####################################
    def firstLetter():
    	"""
    	Return the first Letter
    	@return: the first Letter
    	@rtype: unicode Letter;
    	"""
    	return self.letters[0];
    def secondLetter():
    	"""
    	Return the second Letter
    	@return: the first Letter
    	@rtype: unicode Letter;
    	"""
    	return self.letters[1:2];
    def lastLetter():
    	"""
    	Return the last letter
    	example: zerrouki; 'i' is the last.
    	@return: the last letter
    	@rtype: unicode Letter;
    	"""
    	return self.letters[-1:];
    def secondlastLetter():
    	"""
    	Return the second last letter
    	example: zerrouki; 'k' is the second last.
    	@return: the second last letter
    	@rtype: unicode Letter;
    	"""
    	return self.letters[-2:-1]
    #####################################
    #{Marks functions
    #####################################
    def firstMark():
    	"""
    	Return the first Marks
    	@return: the first Marks
    	@rtype: unicode Marks;
    	"""
    	return self.marks[0];
    def secondMark():
    	"""
    	Return the second Marks
    	@return: the first Marks
    	@rtype: unicode Marks;
    	"""
    	return self.marks[1:2];
    def lastMark():
    	"""
    	Return the last mark
    	example: zerrouki; 'i' is the last.
    	@return: the last letter
    	@rtype: unicode Marks;
    	"""
    	return self.marks[-1:];
    def secondlastMark():
    	"""
    	Return the second last mark
    	example: zerrouki; 'k' is the second last.
    	@return: the second last letter
    	@rtype: unicode Marks;
    	"""
    	return self.marks[-2:-1]
	#####################################
	#{Char functions
	#####################################
	def firstChar():
		"""
		Return the first Char
		@return: the first Char
		@rtype: unicode Char;
		"""
		return self.vocalized[0];
	def secondChar():
		"""
		Return the second Char
		@return: the first Char
		@rtype: unicode Char;
		"""
		return self.vocalized[1:2];
	def lastChar():
		"""
		Return the last char
		example: zerrouki; 'i' is the last.
		@return: the last char
		@rtype: unicode Char;
		"""
		return self.vocalized[-1:];
	def secondlastChar():
		"""
		Return the second last char
		example: zerrouki; 'k' is the second last.
		@return: the second last char
		@rtype: unicode Char;
		"""
		return self.vocalized[-2:-1]
def main():
    pass

if __name__ == '__main__':
    main()
