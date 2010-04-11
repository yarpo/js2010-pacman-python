#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 18:05:03$";

class Object :

	ErrorMsg = 'To jedynie interfejs. Nie należy tworzyć obiketów klasy Game.Objects.Object';

	def __init(self):
		raise NotImplementedException(ErrorMsg);
	pass

	def draw(self, canvas):
		raise NotImplementedException(ErrorMsg);
	pass

pass