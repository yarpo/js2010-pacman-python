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
		cr.arc(x, y, 20, 0, 2 * math.pi)
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

	def _drawBackground(self) :
		cr = self.getContext();
		cr.set_source_rgb(0.5, 0.5, 0.5);
		cr.rectangle(0, 0, self.getWidth(), self.getHeight());
		cr.fill()
	pass

	def _drawWals(self):
		cr = self.getContext();
		cr.move_to(10, 10);
		cr.line_to(30, 30);
		cr.stroke();
	pass

	def expose(self, *args):
		self._drawBackground();
		self._drawWals();
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
