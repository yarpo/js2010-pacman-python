#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Graphics.Canvas import *
from Objects.Character import *
from Objects.Player import *
from Objects.Enemy import *
from Window.Window import *
import gobject
import pygtk

pygtk.require('2.0');

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 13:05:03$";

class Game:

	DEFAULTS = {
		'iLifes' : 3,
		'iEnemies' : 3
	};
	PLAYGROUND_SIZE = {
		'width'  : 600,
		'height' : 550
	};
	oCanvas	= None;
	oPlayer = None;
	oWindow = None;
	oEnemies= [];
	oCookies= [];
	_isRunning = False;

	def __init__(self, title, size):
		self.oCanvas = Canvas(self.PLAYGROUND_SIZE);
		self.oWindow = Window(title, size, self);
 	pass # /__init__

	def _redraw(self):
		self.oCanvas.redraw(self);
		self._displayLifes();
		self._displayScore();
	pass # /_redraw

	def _gameLoop(self):
		if True == self.isRunning() :
			self._redraw();
			gobject.timeout_add(20, self._gameLoop);
		pass # /if
	pass #/_gameLoop

	def _createEnemies(self):
		self.oEnemies= [];
		n = 3;
		i = 0
		while i < n:
			self.oEnemies.append(Enemy(i*100, i*50));
			print 'Stworzylem enemy: ', self.oEnemies[i].getX(),self.oEnemies[i].getY(),
			i += 1;
		pass
	pass

	def _createCookies(self):
		self.oCookies= [];
	pass

	def _createWorld(self):
		Character.setPlaygroundBounds(self.PLAYGROUND_SIZE);
		self.oPlayer = Player(100, 100, self.DEFAULTS['iLifes']);
		self._createEnemies()
		self._createCookies();
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

	def _displayScore(self):
		self.oWindow.displayScore(self.oPlayer.getScore());
	pass

	def _displayLifes(self):
			self.oWindow.displayLifes(self.oPlayer.getLifes());
	pass

pass # /Game

