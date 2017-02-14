#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Unicode represention texts
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Taha Zerrouki
@license: GPL
@date:2014/03/01
@version: 0.1
"""
import repr as reprlib
class ArabicRepr(reprlib.Repr):
    """ Unicode representation"""
    def repr_unicode(self, obj, level):
        "Modify unicode display "
        return u"u'%s'" % obj
