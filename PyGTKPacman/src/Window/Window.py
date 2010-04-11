#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
from Menu import *
from Graphics.Canvas import *

import gtk.gdk as gdk
import math
import random
import gobject

__date__    = "$2010-04-11 13:04:19$"
__version__ = "0.1"
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>"

class Window:

	oWindow	= None;
	oMenu	= None;
	oVBox	= None;
	oCanvas	= None;

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

	def __init__(self, title, size):
		self.__windowSetUp(title, size);
		self.__addMenu();
		#self.__setUpMet();
		self.__addCanvas();
		self.oWindow.show_all()
		self.__addEventListeners()
	pass


	# Draw the circles and update their positions.
	def expose(self, *args):
		cr = self.darea.window.cairo_create()
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

	'''
	def __addCanvas(self) :
		#da = gtk.DrawingArea();
		self.darea = gtk.DrawingArea();
		self.darea.connect("expose-event", self.expose)
		#self.oCanvas = Canvas(da, {'w' : 300, 'h' : 300});
		self.oVBox.pack_start(self.darea);
		self.darea.show();
		#self.oWindow.add(self.darea);
		#self.oCanvas.show();
		gobject.idle_add(self.timeout)
	pass
	'''

	def __addCanvas(self) :
		self.oCanvas = Canvas();
		self.oVBox.pack_start(self.oCanvas);
		self.oCanvas.show();
		#gobject.idle_add(self.timeout)
	pass

	# Self-evident?
	def timeout(self):
		self.darea.queue_draw()
		return True
	pass

	def __addMenu(self) :
		self.oMenu = Menu(self.oWindow);
		self.oVBox.pack_start(self.oMenu.oMenuBar, False, True, 0);
		self.oMenu.oMenuBar.show();
	pass

	def __windowSetUp(self, title, size) :
		self.oWindow = gtk.Window(gtk.WINDOW_TOPLEVEL);
		self.oWindow.set_title(title);
		self.oWindow.set_size_request(size['w'], size['h']);
		self.oVBox = gtk.VBox(False, 1);
		self.oVBox.show();
		self.oWindow.add(self.oVBox);
	pass

	def __addEventListeners(self) :
		self.attachEvent("destroy", self.__closeWindow);
		self.attachEvent('key-press-event', self.__keybordEvents);
		self.attachEvent('key-release-event', self.__keybordEvents);
	pass

	def attachEvent(self, event, handler, data = None) :
		self.oWindow.connect(event, handler, data);
	pass

	def __closeWindow(self, window, event, data = None) :
		gtk.main_quit();
	pass

	def __keybordEvents(self, window, event, data = None) :
		keyval = event.keyval;
		mod = gtk.accelerator_get_label(keyval, event.state);
		print "naciśnięto / puszczono ", mod;
	pass
pass # klasa
