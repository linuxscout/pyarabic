#!/usr/bin/python
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
Stack module
"""
class Stack :
	def __init__(self,text="") :
		self.items = list(text);

	def push(self, item) :
		self.items.append(item)

	def pop(self) :
		if not self.isEmpty():
			return self.items.pop()
		else: 
			return None;

	def isEmpty(self) :
		return (self.items == [])