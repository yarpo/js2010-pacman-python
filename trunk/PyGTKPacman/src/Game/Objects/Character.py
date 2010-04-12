#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Object import *

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 18:05:03$";

class Character(Object) :

	STEP_X = 2.5;
	STEP_Y = 2.5;
	MAX_X = 0;
	MAX_Y = 0;

	def __init__(self, x, y):
		Object.__init__(self, x,y);
	pass

	def up(self):
		if self.posibleMoveY(-self.STEP_Y) :
			self._y -= self.STEP_Y;
		pass
	pass

	def down(self):
		if self.posibleMoveY(self.STEP_Y) :
			self._y += self.STEP_Y;
		pass
	pass

	def left(self):
		if self.posibleMoveX(-self.STEP_X) :
			self._x -= self.STEP_X;
		pass
	pass

	def right(self):
		if self.posibleMoveX(self.STEP_X) :
			self._x += self.STEP_X;
		pass
	pass

	def posibleMoveX(self, step):
		result = self._x + step;

		if result < 0 or result > self.MAX_X :
			return False;
		pass
		return True;
	pass

	def posibleMoveY(self, step):
		result = self._y + step;

		if result < 0 or result > self.MAX_Y :
			return False;
		pass
		return True;
	pass

	@staticmethod
	def setPlaygroundBounds(ps):
		Character.MAX_X = ps['width'];
		Character.MAX_Y = ps['height'];
	pass

pass