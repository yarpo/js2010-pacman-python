#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__="yarpo"
__date__ ="$2010-04-11 13:04:47$"

import pygtk
pygtk.require("2.0")

class Canvas(object):
	'''
	class responsible for drawing stuff on the screen
	'''
	oDrawingArea      = None
	__width           = None
	__height          = None
	__backBuffer      = None
	__backgroundColor = []


	def __init__(self, drawingArea, settings):
		'''
		Constructor
		drawingArea - where game stuff is drawn
		'''

		self.oDrawingArea = drawingArea
		self.__width = settings['w'];
		self.__height = settings['h'];
		self.oDrawingArea.set_size_request(self.width, self.height)
		self.__backgroundColor = [0.2, 0.3, 0.4]
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
