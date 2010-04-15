#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Object import *

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 18:05:03$";

class Character(Object) :

	'''
	Klasa dla po ktorej dziedzicza wszystkie obiety ruchome
	'''

	STEP_X = 3; # liczba pixli o ktore w kazdym obiegu petli przesywa sie obiekt
	STEP_Y = 3;
	MIN_X = 0 # ograniczenia x, y w jakich moze poruszac sie obiekt
	MIN_Y = 0 # ustawiane w setPlaygroundBounds
	MAX_X = 0;
	MAX_Y = 0;
	
	# Kierunki w jakich moze sie poruszac obiekt
	
	DIRECTIONS = {
		'up'     : 0,
		'right'  : 1,
		'down'   : 2,
		'left'   : 3
	};

	def __init__(self, x, y):
		'''
		Konstruktor klasy Character
		'''
		Object.__init__(self, x,y);
		self._direction = -1; # -1 = nigdzie
	pass

	def move(self):
		'''
		Metoda odpowialna za poruszanie sie obiektu - interfejs
		'''
		self._move();
	pass

	def _move(self):
		'''
		wlasciwe poruszanie obiektem
		'''
		if self.DIRECTIONS['up'] == self._direction :
			self._up();
		elif self.DIRECTIONS['right'] == self._direction :
			self._right();
		elif self.DIRECTIONS['down'] == self._direction :
			self._down();
		elif self.DIRECTIONS['left'] == self._direction :
			self._left();
		pass
	pass

	def up(self):
		'''
		Ustawienie kierunku poruszania na "do gory"
		'''
		self._direction = self.DIRECTIONS['up'];
	pass

	def right(self):
		'''
		Ustawienie kierunku poruszania na "w prawo"
		'''
		self._direction = self.DIRECTIONS['right'];
	pass

	def down(self):
		self._direction = self.DIRECTIONS['down'];
	pass

	def left(self):
		'''
		Ustawienie kierunku poruszania na "w lewo"
		'''
		self._direction = self.DIRECTIONS['left'];
	pass

	def _up(self):
		'''
		przesuniecie o ustalona jednostke obiektu w gore
		'''
		if self.possibleUp():
			self._y -= self.STEP_Y;
		pass
	pass

	def _down(self):
		'''
		przesuniecie o ustalona jednostke obiektu w dol
		'''
		if self.possibleDown():
			self._y += self.STEP_Y;
		pass
	pass

	def _left(self):
		'''
		przesuniecie o ustalona jednostke obiektu w lewo
		'''
		if self.possibleLeft() :
			self._x -= self.STEP_X;
		pass
	pass

	def _right(self):
		'''
		przesuniecie o ustalona jednostke obiektu w prawo
		'''
		if self.possibleRight() :
			self._x += self.STEP_X;
		pass
	pass

	def possibleUp(self):
		'''
		Czy mozna sie przesunac w gore
		'''
		if self._possibleMoveY(-self.STEP_Y) :
			if self._noWallUp() :
				return True;
			pass
		pass
		return False;
	pass

	def possibleDown(self):
		'''
		Czy mozna sie przesunac w dol
		'''
		if self._possibleMoveY(self.STEP_Y) :
			if self._noWallDown() :
				return True;
			pass
		pass
		return False;
	pass

	def possibleLeft(self):
		'''
		Czy mozna sie przesunac w lewo
		'''
		if self._possibleMoveX(-self.STEP_X):
			if self._noWallLeft() :
				return True;
			pass
		pass
		return False;
	pass

	def possibleRight(self):
		'''
		Czy mozna sie przesunac w prawo
		'''
		if self._possibleMoveX(self.STEP_X) :
			if self._noWallRight() :
				return True;
			pass
		pass
		return False;
	pass

	def _noWallRight(self):
		'''
		Czy po prawej istnieje przeszkoda w poruszaniu sie
		'''
		x = int((self.getX()-21) / 40);
		y = int(self.getY() / 40);

		if 1 == self.aMatrix[y][x+1] :
			return False;

		return True;
	pass

	def _noWallLeft(self):
		'''
		Czy po lewej istnieje przeszkoda w poruszaniu sie
		'''
		x = int((self.getX()+19) / 40);
		y = int(self.getY() / 40);

		if 1 == self.aMatrix[y][x-1] :
			return False;

		return True;
	pass


	def _noWallUp(self):
		'''
		Czy u gory istnieje przeszkoda w poruszaniu sie
		'''
		x = int(self.getX() / 40);
		y = int((self.getY()+19) / 40);

		if 1 == self.aMatrix[y-1][x] :
			return False;

		return True;
	pass

	def _noWallDown(self):
		'''
		Czy na dole istnieje przeszkoda w poruszaniu sie
		'''
		x = int(self.getX() / 40);
		y = int((self.getY()-21) / 40);

		if 1 == self.aMatrix[y+1][x] :
			return False;

		return True;
	pass

	def _possibleMoveX(self, step):
		'''
		Poruszania sie w obrebie wyznaczonego prostokatu - horyzontalne
		'''
		result = self._x + step;

		if result < self.MIN_X or result > self.MAX_X :
			return False;
		pass
		return True;
	pass

	def _possibleMoveY(self, step):
		'''
		Poruszania sie w obrebie wyznaczonego prostokatu - wertykalne
		'''
		result = self._y + step;

		if result < self.MIN_Y or result > self.MAX_Y :
			return False;
		pass
	
		return True;
	pass

	def dir(self):
		'''
		getter pozycji
		'''
		return self._direction;
	pass

	def distance(self, obj, dist = 15):
		'''
		sprawdza czy nastapil kontakt z innym obiektem 
		'''
		if  ((abs(self.getX() - obj.getX()) <= dist) and
			(abs(self.getY() - obj.getY()) <= dist)) :
			return True;
		pass
		return False;
	pass

	@staticmethod
	def setPlaygroundBounds(ps, matrix):
		'''
		statyczna metoda pozwalajace przejac wazne dla obiektow infomacje
		'''
		Character.MAX_X = ps['pgWidth'];
		Character.MAX_Y = ps['pgHeight'];
		Character.MIN_X = ps['cell'] / 2;
		Character.MIN_Y = ps['cell'] / 2;
		Character.aMatrix = matrix;
	pass

pass