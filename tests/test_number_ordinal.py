#!/usr/bin/python
# -*- coding=utf-8 -*-
# at top of module
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
)
import unittest
import sys
sys.path.append("../")
from pyarabic import number as nb

x= nb.number2ordinal(525).encode('utf8')
print(x)


