#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Game.Objects.Character import Character
from Character import *

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 18:05:03$";

class Player(Character) :

	_x = 0;
	_y = 0;
	_superPower = False;

	def __init__(self, x, y):
		Character.__init__(self, x, y);
	pass

	def hasSuperPower(self):
		return self._superPower;
	pass

	def giveSuperPower(self):
		self._superPower = True;
	pass

	def noSuperPower(self):
		self._superPower = False;
	pass

pass
