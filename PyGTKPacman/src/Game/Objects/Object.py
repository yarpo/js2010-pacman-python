#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 18:05:03$";

class Object :

	_x = 0;
	_y = 0;

	def __init__(self, x, y):
		self._x = x;
		self._y = y;
	pass

	def getX(self):
		return self._x;
	pass

	def getY(self):
		return self._y;
	pass

pass