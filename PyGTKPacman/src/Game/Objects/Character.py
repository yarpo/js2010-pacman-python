#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 18:05:03$";

class Character(Object) :

	_iX;
	_iY;

	def __init(self, x, y):
		self._iX = x;
		self._iY = y;
	pass

	def draw(self, canvas):
		raise NotImplementedException(ErrorMsg);
	pass

pass