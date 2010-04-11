#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
from Menu import *

__date__    = "$2010-04-11 13:04:19$"
__version__ = "0.1"
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>"

class Window(gtk.Window):

	#oWindow	= None;
	oGame	= None;
	oMenu	= None;
	oVBox	= None;
	oCanvas	= None;

	def __init__(self, title, size, game):
		self.oGame = game;
		gtk.Window.__init__(self)
		self.__windowSetUp(title, size);
		self.__addMainVBox();
		self.__addMenu();
		self.__addCanvas();
		self.show_all();
		self.__addEventListeners();
	pass

	def question(self, message):
		md = gtk.Dialog(message,
						self.oWindow,
						gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
						(gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT,
						 gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
		result = md.run();
		result = (gtk.RESPONSE_OK == result or gtk.RESPONSE_ACCEPT == result);

		md.destroy()
		return result;
	pass

	def __addCanvas(self) :
		self.oCanvas = self.oGame.oCanvas;
		self.oVBox.pack_start(self.oCanvas);
		self.oCanvas.show();
	pass


	def __addMenu(self) :
		self.oMenu = Menu(self);
		self.oVBox.pack_start(self.oMenu.oMenuBar, False, True, 0);
		self.oMenu.oMenuBar.show();
	pass

	def __windowSetUp(self, title, size) :
		self.set_title(title);
		self.set_size_request(size['w'], size['h']);
	pass

	def __addMainVBox(self) :
		self.oVBox = gtk.VBox(False, 1);
		self.oVBox.show();
		self.add(self.oVBox);
	pass

	def __addEventListeners(self) :
		self.attachEvent("destroy", self.__closeWindow);
		self.attachEvent('key-press-event', self.__keybordEvents);
		self.attachEvent('key-release-event', self.__keybordEvents);
	pass

	def attachEvent(self, event, handler, data = None) :
		self.connect(event, handler, data);
	pass

	def __closeWindow(self, window, event, data = None) :
		gtk.main_quit();
	pass

	def __keybordEvents(self, window, event, data = None) :
		keyval = event.keyval;
		mod = gtk.accelerator_get_label(keyval, event.state);
		if ('Lewo' == mod) :
			self.oCanvas.x -= 0.5;
		elif ('Prawo' == mod) :
			self.oCanvas.x += 0.5;
		elif ('Góra' == mod) :
			self.oCanvas.y -= 0.5;
		elif ('Dół' == mod) :
			self.oCanvas.y += 0.5;
		pass
	pass
pass # klasa
