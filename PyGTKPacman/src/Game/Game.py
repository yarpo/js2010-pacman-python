#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk;
import gobject;
pygtk.require('2.0');

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    ="$2010-04-11 13:05:03$";

class Game:

	oCanvas	= None;
	oPlayer = None;
	oEnemies= [];
	oCookies= [];
	__isRunning = False;

	def __init__(self, canvas):
		self.oCanvas = canvas;
  		print "dziala Game"
	pass # /__init__

	def __redraw(self):
		print "odrysowuje co mam odrysowac"
		#self.oCanvas.draw()
	pass # /__redraw

	def __gameLoop(self):
		if True == self.__isRunning :
			self.__redraw()
			gobject.timeout_add(100, self.__gameLoop)
		pass # /if
	pass #/__gameLoop

	def __createWorld(self):
		print "Stworzono swiat gry"
	pass #/__createWorld

	def start(self):
		self.__isRunning = True;
		self.__createWorld()
		self.__gameLoop()
	pass # /start

	def stop(self) :
		self.__isRunning = False;
	pass #/stop

pass # /Game
