#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Graphics.Canvas import *
from Objects.Player import *
from Window.Window import *
import gobject
import pygtk


pygtk.require('2.0');

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 13:05:03$";

class Game:

	DEFAULTS = {
				'iLives' : 3,
				'iEnemies' :3
	};
	oCanvas	= None;
	oPlayer = None;
	oWindow = None;
	oEnemies= [];
	oCookies= [];
	__isRunning = False;

	def __init__(self, title, size):
		self.oCanvas = Canvas();
		self.oWindow = Window(title, size, self);
 	pass # /__init__

	def __redraw(self):
		self.oCanvas.drawPlayer(self.oPlayer);
		self.oCanvas.drawEnemies(self.oEnemies);
		self.oCanvas.drawCookies(self.oCookies);
		self.oCanvas.draw();
	pass # /__redraw

	def __gameLoop(self):
		if True == self.isRunning() :
			self.__redraw();
			gobject.timeout_add(20, self.__gameLoop);
		pass # /if
	pass #/__gameLoop

	def __createEnemies(self):
		pass
	pass

	def __createCookies(self):
		pass
	pass

	def __createWorld(self):
		self.oPlayer = Player(100, 100);
		self.oEnemies = self.__createEnemies()
		self.oCookies = self.__createCookies();
	pass #/__createWorld

	def isRunning(self):
		return self.__isRunning;
	pass

	def __run(self) :
		self.__isRunning = True;
	pass # /run

	def start(self):
		self.__run();
		self.__createWorld();
		self.__gameLoop();
	pass # /start

	def restart(self) :
		self.stop();
		if self.oWindow.question('Nowa Gra?') == True :
			self.start();
		pass
		self.__run();
	pass # /restart

	def stop(self) :
		self.__isRunning = False;
	pass #/stop

pass # /Game

