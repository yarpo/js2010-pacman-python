#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__="yarpo"
__date__ ="$2010-04-11 13:04:47$"

import pygtk
import gtk
pygtk.require("2.0")
import math

class Canvas(gtk.DrawingArea):

	def __init__(self):
		gtk.DrawingArea.__init__(self);
		self.x = 10
		self.y = 10
		self.connect("expose-event", self.expose)
	pass

	def getContext(self):
		return self.window.cairo_create()
	pass

	def expose(self, *args):
		cr = self.getContext();
		cr.set_line_width(4)
		cr.arc(self.x, self.y, 8, 0, 2 * math.pi)
		cr.stroke_preserve()
		cr.set_source_rgb(1, 1, 1)
		cr.fill()
	pass

	
	def draw(self):
		self.queue_draw();
	pass
pass
