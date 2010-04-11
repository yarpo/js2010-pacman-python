#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
from Game.Game import *

__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>"
__date__    = "$2010-04-11 13:05:20$"
__version__ = "0.1"

class PacmanGame:

	def __init__(self, title, size):
		game = Game(title, size);
		game.start();
	pass # /__init__

pass # / PacmanGame

if __name__ == "__main__" :
	PacmanGame("Pacman",
		{
			'w': 600,
			'h': 600
		});
	gtk.main();
pass # / if 
