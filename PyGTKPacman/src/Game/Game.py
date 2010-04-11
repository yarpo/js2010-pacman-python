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
	_isRunning = False;

	def __init__(self, title, size):
		self.oCanvas = Canvas();
		self.oWindow = Window(title, size, self);
 	pass # /__init__

	def _redraw(self):
		self.oCanvas.drawPlayer(self.oPlayer);
		self.oCanvas.drawEnemies(self.oEnemies);
		self.oCanvas.drawCookies(self.oCookies);
		self.oCanvas.draw();
	pass # /_redraw

	def _gameLoop(self):
		if True == self.isRunning() :
			self._redraw();
			gobject.timeout_add(20, self._gameLoop);
		pass # /if
	pass #/_gameLoop

	def _createEnemies(self):
		self.oEnemies= [];
	pass

	def _createCookies(self):
		self.oCookies= [];
	pass

	def _createWorld(self):
		self.oPlayer = Player(100, 100);
		self.oEnemies = self._createEnemies()
		self.oCookies = self._createCookies();
	pass #/_createWorld

	def isRunning(self):
		return self._isRunning;
	pass

	def _run(self) :
		self._isRunning = True;
	pass # /run

	def start(self):
		self._run();
		self._createWorld();
		self._gameLoop();
	pass # /start

	def restart(self) :
		self.stop();
		if self.oWindow.question('Nowa Gra?') == True :
			self.start();
		pass
		self._run();
	pass # /restart

	def stop(self) :
		self._isRunning = False;
	pass #/stop

pass # /Game

