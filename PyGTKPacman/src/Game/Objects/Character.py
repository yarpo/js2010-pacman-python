#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Object import *

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 18:05:03$";

class Character(Object) :

	iX = 0;
	iY = 0;

	def __init__(self, x, y):
		
		self.iX = x;
		self.iY = y;
	pass

	def draw(self, canvas):
		raise NotImplementedException(ErrorMsg);
	pass

pass