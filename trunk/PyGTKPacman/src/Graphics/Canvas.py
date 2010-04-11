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
		self.__setUpMet()
		gobject.idle_add(self.timeout)
		#darea = gtk.DrawingArea()
		self.connect("expose-event", self.expose)
		#self.oDrawingArea = drawingArea
		#self.__width = settings['w'];
		#self.__height = settings['h'];
		#self.set_size_request(self.width, self.height)
		#self.__backgroundColor = [0.2, 0.3, 0.4]
	pass

	def __setUpMet(self) :
		# The number of circles and the window size.
		self.num = 128
		self.size = 512

		# Initialize circle coordinates and velocities.
		self.x = []
		self.y = []
		self.xv = []
		self.yv = []
		for i in range(self.num):
			self.x.append(random.randint(0, self.size))
			self.y.append(random.randint(0, self.size))
			self.xv.append(random.randint(-4, 4))
			self.yv.append(random.randint(-4, 4))
		pass
	pass

	# Draw the circles and update their positions.
	def expose(self, *args):
		cr = self.window.cairo_create()
		cr.set_line_width(4)
		for i in range(self.num):
			cr.set_source_rgb(1, 0, 0)
			cr.arc(self.x[i], self.y[i], 8, 0, 2 * math.pi)
			cr.stroke_preserve()
			cr.set_source_rgb(1, 1, 1)
			cr.fill()
			self.x[i] += self.xv[i]
			self.y[i] += self.yv[i]
			if self.x[i] > self.size or self.x[i] < 0:
				self.xv[i] = -self.xv[i]
			if self.y[i] > self.size or self.y[i] < 0:
				self.yv[i] = -self.yv[i]

	def timeout(self):
		self.queue_draw()
		return True
	pass

	def draw(self):
		'''
		draws all objects on the screen
		'''
		cr = self._drawingArea.window.cairo_create()
		cr.set_source_rgb(*self.__backgroundColor)
		cr.rectangle(0, 0, self.width, self.height)
		cr.fill()
	pass

	def _getHeight(self):
		'''
		get height of the canvas
		'''
		return self.__height
	pass

	def _getWidth(self):
		'''
		get width of the canvas
		'''
		return self.__width
	pass

	width = property(_getWidth, doc = "get width of the canvas")
	height = property(_getHeight, doc = "get height of the canvas")
pass
