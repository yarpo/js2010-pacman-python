#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__="yarpo"
__date__ ="$2010-04-11 13:04:47$"

import pygtk
import gtk
pygtk.require("2.0")
import math

class Canvas(gtk.DrawingArea):

	_oPlayer  = None;
	_oEnemies = None;
	_oCookies = None;
	_width    = 0;
	_height   = 0;

	def __init__(self, size):
		gtk.DrawingArea.__init__(self);
		self.resize(size['width'], size['height']);
		self.connect("expose-event", self.expose);
	pass

	def resize(self, x, y):
		self._width = x;
		self._height = y;
		self.set_size_request(x, y);
	pass

	def getWidth(self):
		return self._width;
	pass


	def getHeight(self):
		return self._height;
	pass

	def redraw(self, game):
		self.drawCookies(game.oCookies);
		self.drawEnemies(game.oEnemies);
		self.drawPlayer(game.oPlayer);
		self.draw();
	pass

	def getContext(self):
		return self.window.cairo_create()
	pass

	def _drawPlayer(self):
		x = self._oPlayer.getX();
		y = self._oPlayer.getY();
		cr = self.getContext();
		cr.set_line_width(4)
		cr.arc(x, y, 16, 0, 2 * math.pi)
		cr.stroke_preserve()
		cr.set_source_rgb(1, 1, 1)
		cr.fill()
	pass

	def drawPlayer(self, player):
		self._oPlayer = player;
	pass

	def drawEnemies(self, enemies):
		self._oEnemies = enemies;
	pass

	def _drawEnemy(self, enemy):
		x = enemy.getX();
		y = enemy.getY();
		cr = self.getContext();
		cr.set_line_width(4);
		cr.arc(x, y, 10, 0, 2 * math.pi);
		cr.stroke_preserve();
		cr.set_source_rgb(1, 0, 0);
		cr.fill();
	pass

	def _drawEnemies(self):
		for enemy in self._oEnemies :
			self._drawEnemy(enemy);
		pass
	pass

	def drawCookies(self, cookies):
		self._oCookies = cookies;
	pass

	def _drawCookie(self, cookie):
		x = cookie.getX();
		y = cookie.getY();
		cr = self.getContext();
		cr.set_line_width(4);
		cr.arc(x, y, 6, 0, 2 * math.pi);
		cr.stroke_preserve();
		cr.set_source_rgb(0.9, 0.8, 0.1);
		cr.fill();
	pass

	def _drawCookies(self):
		for cookie in self._oCookies :
			self._drawCookie(cookie);
		pass
	pass

	def _drawRectangle(self, x, y, w, h, r, g, b):
		cr = self.getContext();
		cr.set_source_rgb(r, g, b);
		cr.rectangle(x, y, w, h);
		cr.fill()
		pass
	pass

	def _drawBackground(self, r, g, b) :
		self._drawRectangle(0, 0, self.getWidth(), self.getHeight(), r, g, b);
	pass

	def _drawWall(self, x, y, w, h):
		self._drawRectangle(x, y, w, h, 0, 0, 0);
	pass

	def _drawVerticalWall(self, x, y, h):
		start_x = x * 40;
		start_y = y * 40;
		height  = h * 40;
		self._drawWall(start_x, start_y, 40, height);
	pass

	def _drawHorizontalWall(self, x, y, h):
		start_x = x * 40;
		start_y = y * 40;
		width = h * 40;
		self._drawWall(start_x, start_y, width, 40);
	pass

	def _drawWalls(self):
		self._drawVerticalWall(1, 1, 12);
		self._drawVerticalWall(3, 0, 3);
		self._drawVerticalWall(3, 4, 3);
		self._drawVerticalWall(3, 8, 3);
		self._drawVerticalWall(3, 12, 2);
		self._drawVerticalWall(11, 0, 3);
		self._drawVerticalWall(11, 4, 3);
		self._drawVerticalWall(11, 8, 3);
		self._drawVerticalWall(11, 12, 2);
		self._drawVerticalWall(13, 1, 12);

		self._drawHorizontalWall(5, 1, 5);
		self._drawHorizontalWall(5, 3, 5);
		self._drawHorizontalWall(5, 5, 5);

		self._drawHorizontalWall(5, 8, 5);
		self._drawHorizontalWall(5, 10, 5);
		self._drawHorizontalWall(5, 12, 5);

	pass

	def expose(self, *args):
		self._drawBackground(0.5, 0.5, 0.5);
		self._drawWalls();
		self._drawCookies();
		self._drawEnemies();
		self._drawPlayer();
		self._reset();
	pass
	
	def _reset(self):
		self._oPlayer  = None;
		self._oEnemies = None;
		self._oCookies = None;
	pass

	def draw(self):
		self.queue_draw();
	pass
pass
