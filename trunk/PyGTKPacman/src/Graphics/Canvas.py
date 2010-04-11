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

	def __init__(self):
		gtk.DrawingArea.__init__(self);
		self.connect("expose-event", self.expose)
	pass

	def getContext(self):
		return self.window.cairo_create()
	pass

	def passPlayer(self, player):
		self.pl = player;
		#self.drawPlayer(self.pl)
	pass

	def _drawPlayer(self):
		x = self._oPlayer.getX();
		y = self._oPlayer.getY();
		cr = self.getContext();
		cr.set_line_width(4)
		cr.arc(x, y, 8, 0, 2 * math.pi)
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

	def _drawEnemies(self):
		pass
	pass

	def drawCookies(self, cookies):
		self._oCookies = cookies;
	pass

	def _drawCookies(self):
		pass
	pass


	def expose(self, *args):
		self._drawPlayer();
		self._drawEnemies();
		self._drawCookies();
		self._reset();
		return False;
		#pass
		#self.drawPlayer();
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
