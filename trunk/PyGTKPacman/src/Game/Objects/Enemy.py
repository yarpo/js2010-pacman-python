#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 18:05:03$";

from Character import *
import random
from time import *

class Enemy(Character) :

	'''
	klasa przeciwnikow w grze
	'''

	def __init__(self, x, y):
		Character.__init__(self, x, y);
		random.seed(time())
		self.newDirection();
	pass

	def move(self):
		'''
		poruszanie obiektem
		'''
		if self._canNotMove() :
			self.newDirection();
		pass

		self._move();
	pass

	def _canNotMove(self):
		'''
		czy obiekt nie moze sie poruszyc -> do zmiany kierunku ruchu
		'''
		if (self.DIRECTIONS['up'] == self._direction and False == self.possibleUp()) :
			return True;
		elif self.DIRECTIONS['right'] == self._direction and False == self.possibleRight() :
			return True;
		elif self.DIRECTIONS['down'] == self._direction and False == self.possibleDown() :
			return True;
		elif self.DIRECTIONS['left'] == self._direction and False == self.possibleLeft() :
			return True;
		pass
	
		return False;
	pass

	def newDirection(self):
		'''
		ustawianie nowego kierunku ruchu - pseudo-losowo
		'''
		self._direction = self._rand();
	pass

	def _rand(self):
		'''
		metoda losujaca nowy kierunek
		'''
		return random.randint(0, len(self.DIRECTIONS)-1);
	pass
pass