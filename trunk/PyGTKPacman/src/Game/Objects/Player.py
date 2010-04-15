#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Character import *
from time import *

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 18:05:03$";

class Player(Character) :

	'''
	Klasa odpowiedzialna za funkcjonalnosc gracza
	'''

	_x      = 0;
	_y      = 0;
	_iScore = 0;
	_iLifes = 0
	POINTS  = 10;
	SP_TIME = 8;
	_bSuperPower = False;

	def __init__(self, x, y, lifes):
		Character.__init__(self, x, y);
		self._iLifes = lifes;
		self._iScore = 0;
		self.noSuperPower();
		self._direction = -1;
	pass

	def setPos(self, x, y):
		'''
		reczne nadanie nowej pozycji
		'''
		self._x = x;
		self._y = y;
	pass

	def hasSuperPower(self):
		'''
		czy gracz posiada super moce
		'''
		if time() - self._iTimeSuperPower > self.SP_TIME :
			self._bSuperPower = False;
		pass

		return self._bSuperPower;
	pass

	def giveSuperPower(self):
		'''
		nadaj supermoce
		'''
		self._iTimeSuperPower = time();
		self._bSuperPower = True;
	pass

	def noSuperPower(self):
		self._iTimeSuperPower = time() - 2*self.SP_TIME;
		self._bSuperPower = False;
	pass

	def getScore(self) :
		'''
		getter liczby punktow
		'''
		return self._iScore;
	pass

	def addScore(self) :
		'''
		dodaje punkty
		'''
		self._iScore += self.POINTS;
	pass

	def getLifes(self) :
		'''
		getter liczby zyc
		'''
		return self._iLifes;
	pass

	def die(self):
		'''
		zabiera jedno zycie
		'''
		self._iLifes -= 1;
	pass

	def isDead(self):
		'''
		czy gracz jeszcze zyje?
		'''
		return (self.getLifes() == 0);
	pass
pass
