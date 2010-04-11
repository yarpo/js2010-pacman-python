#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
from Window.Window import *
from Game.Game import *

__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>"
__date__    ="$2010-04-11 13:05:20$"
__version__ = "0.1"

class PacmanGame:

	oWindow = None;
	oGame	= None;

	def __init__(self):
		self.oWindow = Window("Pacman", {'w' : 600, 'h': 600});
		self.oGame = Game(Window.oCanvas);
		self.oGame.start();
	pass # /__init__

pass # klasa

if __name__ == "__main__" :
	PacmanGame();
	gtk.main();
pass
