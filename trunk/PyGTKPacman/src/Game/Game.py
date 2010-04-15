#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Graphics.Canvas import *
from Objects.Character import *
from Objects.Player import *
from Objects.Enemy import *
from Window.Window import *
from Settings import *
import gobject
import pygtk

pygtk.require('2.0');

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 13:05:03$";

class Game:

	'''
	klasa odpowidzialna za stworzenie swiata gry
	'''

	SIZE_CONFIG = {
		'width'   : 600,
		'height'  : 560,
		'pgWidth' : 580,
		'pgHeight': 540,
		'plSize'  : 16,
		'eSize'   : 10,
		'cSize'   : 6,
		'xSize'   : 10,
		'cell'   : 40
	};
	oCanvas	  = None;
	oPlayer   = None;
	oWindow   = None;
	oSettings = None
	oEnemies  = [];
	oCookies  = [];
	_iCookies = 0;
	_bIsRunning = False;
	_aMatrix = [
		[0,0,0,1,0,0,0,2,0,0,0,0,0,0,0],
		[0,1,0,1,0,1,1,1,1,1,0,1,0,1,0],
		[0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
		[0,1,0,1,0,1,1,1,1,1,0,0,0,1,0],
		[0,1,0,0,0,0,0,0,0,0,1,1,0,1,0],
		[0,1,0,1,0,1,1,1,1,0,0,1,0,1,0],
		[0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
		[0,1,0,0,0,0,0,0,0,1,0,0,0,1,1],
		[0,1,1,1,0,1,1,1,1,1,0,1,0,0,2],
		[0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
		[0,1,0,1,0,1,1,1,1,1,0,1,0,1,1],
		[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,0,1,0,1,1,1,1,1,0,1,0,1,0],
		[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
	];

	def __init__(self, title, size, timeout = 20):
		'''
		konstruktor
		'''
		self.oCanvas = Canvas(self.SIZE_CONFIG);
		self.oSettings = Settings(3, 3);
		self.oWindow = Window(title, size, self);
 	pass # /__init__

	def _redraw(self):
		'''
		ponownie wyrysowuje swiat gry na ekranie
		'''
		self.oCanvas.redraw(self);
		self._displayLifes();
		self._displayScore();
	pass # /_redraw

	def _gameLoop(self):
		'''
		glowna petla gry
		'''
		if True == self.isRunning() :
			self._moveObjects();
			self._detectCollisions();
			self._redraw();
			if False == self._winner() :
				gobject.timeout_add(30, self._gameLoop);
			else :
				self._won();
		pass # /if
	pass #/_gameLoop

	def _won(self):
		'''
		wygrana
		'''
		self.oWindow.help("Wygrałeś!");
		self.restart();
	pass

	def _addCookie(self, x, y):
		'''
		Dodaje ciastko
		'''
		x_px = x*self.SIZE_CONFIG['cell'] + 0.5*self.SIZE_CONFIG['cell'];
		y_px = y*self.SIZE_CONFIG['cell'] + 0.5*self.SIZE_CONFIG['cell'];
		self.oCookies.append(Object(x_px, y_px));
		self._iCookies += 1;
	pass

	def _delCookie(self, index):
		self.oPlayer.addScore();
		self.oCookies.pop(index);
		self._iCookies -= 1;
	pass

	def _winner(self):
		'''
		Czy juz nie ma ciasteczek
		'''
		return (self._iCookies == 0 );
	pass

	def _playerKilled(self, enemy) :
		'''
		obsluga zderzenia gracza z przeciwnikiem
		'''
		if self.oPlayer.hasSuperPower() :
			self.oEnemies.remove(enemy);
			self.oPlayer.addScore();
		else:
			self.stop();
			self.oPlayer.die();
			if self.oPlayer.isDead() :
				self.oWindow.help('To już koniec. \nNastąpi zamknięcie okna');
				self.oWindow.quit();
			else:
				gobject.timeout_add(2000, self.__rerun);
			pass
	pass

	def __rerun(self):
		'''
		Wznowienie gry z reczna zmiana pozycji gracza - po smierci
		'''
		self.oPlayer.setPos(100, 100);
		self._run();
		self._gameLoop();
	pass

	def _enemiesCollisions(self):
		'''
		Wykrywa kolizje gracza z przeciwnikami
		'''
		for enemy in self.oEnemies :
			if self.oPlayer.distance(enemy) :
				self._playerKilled(enemy);
			pass
		pass
	pass

	def _cookiesCollisions(self):
		'''
		Kolizje z ciastkami
		'''
		index = 0;
		for cookie in self.oCookies :
			if self.oPlayer.distance(cookie) :
				self._delCookie(index);
			pass
			index += 1;
		pass
	pass

	def _extrasCollisions(self):
		'''
		Kolizje z superciastkami
		'''
		index = 0;
		for extra in self.oExtras :
			if self.oPlayer.distance(extra) :
				self.oPlayer.giveSuperPower();
				self.oExtras.pop(index);
			pass
			index += 1;
		pass
	pass

	def _detectCollisions(self):
		'''
		sprawdza czy nie bylo kolizji miedzy obiektami
		'''
		self._enemiesCollisions();
		self._cookiesCollisions();
		self._extrasCollisions();

	pass

	def _moveObjects(self):
		'''
		porusza obiektami
		'''
		self.oPlayer.move();
		for enemy in self.oEnemies :
			enemy.move();
		pass
	pass

	def _createEnemies(self, n):
		'''
		tworzy przeciwnikow wg zadanych parametrow
		'''
		self.oEnemies= [];
		i = 0
		while i < n:
			self.oEnemies.append(Enemy(20, 20));
			i += 1;
		pass
	pass

	def _createCookies(self):
		'''
		Tworzy ciasteczka wszedzie gdzie jest na to miejsce
		'''
		self.oCookies = [];
		self.oExtras  = [];
		y = 0;
		for row in self._aMatrix :
			x = 0
			for cell in row :
				if 0 == cell :
					self._addCookie(x, y);
				elif 2 == cell :
					x_px = x*self.SIZE_CONFIG['cell'] + 0.5*self.SIZE_CONFIG['cell'];
					y_px = y*self.SIZE_CONFIG['cell'] + 0.5*self.SIZE_CONFIG['cell'];
					self.oExtras.append(Object(x_px, y_px));
				pass
				x += 1;
			pass
			y += 1;
		pass
	pass

	def _createWorld(self):
		'''
		Tworzy swiat gry
		'''
		Character.setPlaygroundBounds(self.SIZE_CONFIG, self._aMatrix);
		self.oPlayer = Player(100, 100, self.oSettings.iLifes);
		self._createEnemies(self.oSettings.iEnemies);
		self._createCookies();
	pass #/_createWorld

	def isRunning(self):
		'''
		czy gra sie toczy
		'''
		return self._bIsRunning;
	pass

	def _run(self) :
		'''
		ustawia flage odpowiedzialna za kontynuowanie rozgrywki
		'''
		self._bIsRunning = True;
	pass # /run

	def start(self):
		'''
		start gry - ustawienia poczatkowe
		'''
		self._run();
		self.oWindow.addEventListeners();
		self._createWorld();
		self._gameLoop();
	pass # /start

	def restart(self) :
		'''
		ponowny start gry po pauzie
		'''
		self.stop();
		if self.oWindow.question('Nowa Gra?') == True :
			self.start();
		pass
		self._run();
	pass # /restart

	def stop(self) :
		'''
		Zatrzymuje gre - pauza
		'''
		self._bIsRunning = False;
	pass #/stop

	def _displayScore(self):
		'''
		wyswietla wynik w oknie gry
		'''
		self.oWindow.displayScore(self.oPlayer.getScore());
	pass

	def _displayLifes(self):
		'''
		wyswietla liczbe zyc
		'''
		self.oWindow.displayLifes(self.oPlayer.getLifes());
	pass

	def setLifes(self, lifes):
		'''
		zapisuje liczbe zyc
		'''
		self.oPlayer.setLifes(lifes);
	pass

pass # /Game

