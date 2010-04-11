#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Game.Objects.Character import Character
from Character import *
import math

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 18:05:03$";

class Player(Character) :

	#iX = 0;
	#iY = 0;

	def __init__(self, x, y):
		self.iX = x;
		self.iY = y;

		#Character.__init__(self, x, y);
	pass

	def draw(self, cr):
		print "Jedziemy", self.iX, self.iY
		cr.set_line_width(4)
		cr.arc(self.iX, self.iY, 8, 0, 2 * math.pi)
		cr.stroke_preserve()
		cr.set_source_rgb(1, 1, 1)
		cr.fill()
	pass
