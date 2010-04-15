#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__="yarpo"
__date__ ="$2010-04-11 13:04:47$"

import pygtk
import gtk
pygtk.require("2.0")
import math

class Canvas(gtk.DrawingArea):

	'''
	Klasa pozwalajaca wyrysowywac swiat gry na ekranie
	Dziedziczy po gtk.DrawingArea
	'''

	_oPlayer  = None;
	_oEnemies = None;
	_oCookies = None;
	_width    = 0;
	_height   = 0;
	_size     = None;

	def __init__(self, size):
		'''
		konstruktor
		'''
		gtk.DrawingArea.__init__(self);
		self._size = size;
		self.resize(size['width'], size['height']);
		self.connect("expose-event", self.expose);
	pass

	def resize(self, x, y):
		'''
		reczna zmiana rozmiarow
		'''
		self._width = x;
		self._height = y;
		self.set_size_request(x, y);
	pass

	def getWidth(self):
		'''
		getter szerokosci
		'''
		return self._width;
	pass

	def getHeight(self):
		'''
		getter wysokosci
		'''
		return self._height;
	pass

	def redraw(self, game):
		'''
		namaluj swiat na nowo
		'''
		self.drawCookies(game.oCookies);
		self.drawExtras(game.oExtras);
		self.drawEnemies(game.oEnemies);
		self.drawPlayer(game.oPlayer);
		self.draw();
	pass

	def getContext(self):
		'''
		pobranie kontekstu, na ktory wszystko jest wyrysowywane
		'''
		return self.window.cairo_create()
	pass

	def _drawPlayer(self):
		'''
		rysowanie gracza
		'''
		x = self._oPlayer.getX();
		y = self._oPlayer.getY();
		cr = self.getContext();
		cr.set_line_width(4)
		cr.arc(x, y, self._size['plSize'], 0, 2 * math.pi)
		cr.stroke_preserve()
		cr.set_source_rgb(1, 1, 1)
		if self._oPlayer.hasSuperPower() :
			cr.set_source_rgb(0, 0, 1)
		pass
		cr.fill()
	pass

	def drawPlayer(self, player):
		'''
		setter gracza
		'''
		self._oPlayer = player;
	pass

	def drawEnemies(self, enemies):
		'''
		setter przeciwnikow
		'''
		self._oEnemies = enemies;
	pass

	def _drawEnemy(self, enemy):
		'''
		wyrysowanie przeciwnika
		'''
		cr = self.getContext();
		x = enemy.getX();
		y = enemy.getY();
		cr.set_line_width(4);
		cr.arc(x, y, self._size['eSize'], 0, 2 * math.pi);
		cr.stroke_preserve();
		cr.set_source_rgb(1, 0, 0);
		cr.fill();
	pass

	def _drawEnemies(self):
		'''
		wyrysowanie przeciwnikow
		'''
		for enemy in self._oEnemies :
			self._drawEnemy(enemy);
		pass
		
	pass

	def drawCookies(self, cookies):
		'''
		setter ciasteczek
		'''
		self._oCookies = cookies;
	pass

	def _drawCookie(self, cookie):
		'''
		wyrysowanie ciasteczka
		'''
		x = cookie.getX();
		y = cookie.getY();
		cr = self.getContext();
		cr.set_line_width(4);
		cr.arc(x, y, self._size['cSize'], 0, 2 * math.pi);
		cr.stroke_preserve();
		cr.set_source_rgb(0.9, 0.8, 0.1);
		cr.fill();
	pass

	def _drawCookies(self):
		'''
		rysowanie wszystkich ciastek
		'''
		for cookie in self._oCookies :
			self._drawCookie(cookie);
		pass
		
	pass

	def drawExtras(self, extras):
		'''
		setter super ciasteczek
		'''
		self._oExtras = extras;
	pass

	def _drawExtra(self, extra):
		'''
		wyrysowanie ciasteczka
		'''
		x = extra.getX();
		y = extra.getY();
		cr = self.getContext();
		cr.set_line_width(4);
		cr.arc(x, y, self._size['xSize'], 0, 2 * math.pi);
		cr.stroke_preserve();
		cr.set_source_rgb(0.9, 0.1, 0.6);
		cr.fill();
	pass

	def _drawExtras(self):
		'''
		rysowanie wszystkich ciastek
		'''
		for extra in self._oExtras :
			self._drawExtra(extra);
		pass

	pass

	def _drawRectangle(self, x, y, w, h, r, g, b):
		'''
		rysowanie prostokata
		'''
		self._cr.set_source_rgb(r, g, b);
		self._cr.rectangle(x, y, w, h);
		self._cr.fill();
		pass
	pass

	def _drawBackground(self, r, g, b) :
		'''
		rysowanie tla
		'''
		self._drawRectangle(0, 0, self.getWidth(), self.getHeight(), r, g, b);
		
	pass

	def _drawWall(self, x, y, w, h):
		'''
		rysowanie sciany
		'''
		self._drawRectangle(x, y, w, h, 0, 0, 0);
	pass

	def _drawVerticalWall(self, x, y, h):
		'''
		pozioma sciana
		'''
		start_x = x * 40;
		start_y = y * 40;
		height  = h * 40;
		self._drawWall(start_x, start_y, 40, height);
	pass

	def _drawHorizontalWall(self, x, y, h):
		'''
		Pionowa sciana
		'''
		start_x = x * 40;
		start_y = y * 40;
		width = h * 40;
		self._drawWall(start_x, start_y, width, 40);
	pass

	def _drawWalls(self):
		'''
		wyrysowanie wszystkich scian
		'''
		self._drawVerticalWall(1, 1, 12);
		self._drawVerticalWall(2, 8, 1);
		self._drawVerticalWall(3, 0, 4);
		self._drawVerticalWall(3, 5, 2);
		self._drawVerticalWall(3, 8, 3);
		self._drawVerticalWall(3, 12, 1);
		self._drawVerticalWall(10, 4, 1);
		self._drawVerticalWall(11, 1, 2);
		self._drawVerticalWall(11, 4, 3);
		self._drawVerticalWall(11, 8, 3);
		self._drawVerticalWall(11, 12, 2);
		self._drawVerticalWall(13, 1, 7);
		self._drawVerticalWall(13, 9, 2);
		self._drawVerticalWall(13, 12, 1);
		self._drawVerticalWall(14, 7, 1);
		self._drawVerticalWall(14, 10, 1);
		self._drawHorizontalWall(5, 1, 5);
		self._drawHorizontalWall(5, 3, 5);
		self._drawHorizontalWall(5, 5, 4);
		self._drawHorizontalWall(5, 8, 5);
		self._drawHorizontalWall(9, 7, 1);
		self._drawHorizontalWall(5, 10, 5);
		self._drawHorizontalWall(5, 12, 5);
	pass

	def expose(self, *args):
		'''
		odswiezenie wszystkiego co jest rysowane na ekranie
		'''
		try:
			self._cr = self.getContext();
			self._drawBackground(0.5, 0.5, 0.5);
			self._drawWalls();
			self._drawCookies();
			self._drawExtras();
			self._drawEnemies();
			self._drawPlayer();
			self._reset();
		except:
			pass
	pass
	
	def _reset(self):
		'''
		czysc pamiec
		'''
		self._oPlayer  = None;
		self._oEnemies = None;
		self._oCookies = None;
	pass

	def draw(self):
		'''
		zlec rysowanie wszystkiego z bufora
		'''
		self.queue_draw();
	pass
pass
