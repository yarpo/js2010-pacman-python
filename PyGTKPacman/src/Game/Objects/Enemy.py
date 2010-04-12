#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 18:05:03$";

from Character import *

class Enemy(Character) :

	def __init__(self, x, y):
		Character.__init__(self, x, y);
	pass

pass