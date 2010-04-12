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
	_bSuperPower = False;
	_iScore  = 0;
	_iLifes = 0
	POINTS = 10;

	def __init__(self, x, y, lifes):
		Character.__init__(self, x, y);
		self._iLifes = lifes;
		self._iScore = 0;
	pass

	def hasSuperPower(self):
		return self._bSuperPower;
	pass

	def giveSuperPower(self):
		self._bSuperPower = True;
	pass

	def noSuperPower(self):
		self._bSuperPower = False;
	pass

	def getScore(self) :
		return self._iScore;
	pass

	def addScore(self) :
		self._iScore += self.POINTS;
	pass

	def die(self):
		self._iLifes -= 1;
	pass

pass
