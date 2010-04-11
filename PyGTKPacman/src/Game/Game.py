#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
from Menu import *

__version__ = "0.1"
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>"
__date__ ="$2010-04-11 13:05:03$"

class Game:

	oCanvas	= None;

	def __init__(self, canvas):
		self.oCanvas = canvas
		print "dziala Game"
	pass
pass # klasa
