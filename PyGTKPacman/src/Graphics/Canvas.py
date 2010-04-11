#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__="yarpo"
__date__ ="$2010-04-11 13:04:47$"

import pygtk
import gtk
pygtk.require("2.0")


import math
import random
import gobject


class Canvas(gtk.DrawingArea):
	'''
	class responsible for drawing stuff on the screen
	'''
	oDrawingArea      = None
	__width           = None
	__height          = None
	__backBuffer      = None
	__backgroundColor = []


	def __init__(self):
		gtk.DrawingArea.__init__(self);
		self.x = 10
		self.y = 10
		self.connect("expose-event", self.expose)
	pass

	# Draw the circles and update their positions.
	def expose(self, *args):
		cr = self.window.cairo_create()
		cr.set_line_width(4)
		cr.arc(self.x, self.y, 8, 0, 2 * math.pi)
		cr.stroke_preserve()
		cr.set_source_rgb(1, 1, 1)
		cr.fill()
		#for i in range(self.num):
		#	cr.set_source_rgb(1, 0, 0)
		#	cr.arc(self.x[i], self.y[i], 8, 0, 2 * math.pi)
		#	cr.stroke_preserve()
		#	cr.set_source_rgb(1, 1, 1)
		#	cr.fill()
			#self.x[i] += self.xv[i]
			#self.y[i] += self.yv[i]
			#if self.x[i] > self.size or self.x[i] < 0:
			#	self.xv[i] = -self.xv[i]
			#pass
			#if self.y[i] > self.size or self.y[i] < 0:
			#	self.yv[i] = -self.yv[i]
			#pass
		#pass
	pass

	def timeout(self):
		self.queue_draw();
		return True;
	pass

	def draw(self):
		self.queue_draw();
	pass

	def _getHeight(self):
		return self.__height;
	pass

	def _getWidth(self):
		return self.__width;
	pass

	width = property(_getWidth, doc = "get width of the canvas")
	height = property(_getHeight, doc = "get height of the canvas")
pass
