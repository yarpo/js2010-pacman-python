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

	KEY = {
		'up'	: 65362,
		'right' : 65363,
		'down'	: 65364,
		'left'	: 65361
	};

	oGame	  = None;
	oMenu	  = None;
	oVBox	  = None;
	oCanvas	  = None;
	oLifeBar  = None;
	oScoreBar = None;

	def __init__(self, title, size, game):
		self.oGame = game;
		gtk.Window.__init__(self)
		self._windowSetUp(title, size);
		self._addMainVBox();
		self._addMenu();
		self._addCanvas();
		self._addBottomBar();
		self.show_all();
		self._addEventListeners();
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

	def _addBottomBar(self):
		hbox = gtk.HBox(False, 5);
		self.oLifeBar  = gtk.Label("Życia: %d" % 3);
		self.oScoreBar = gtk.Label("Wynik: %d" % 100);
		hbox.pack_start(self.oLifeBar);
		hbox.pack_start(self.oScoreBar);
		self.oVBox.pack_start(hbox);

	pass

	def _addCanvas(self) :
		self.oCanvas = self.oGame.oCanvas;
		self.oVBox.pack_start(self.oCanvas);
		self.oCanvas.show();
	pass


	def _addMenu(self) :
		self.oMenu = Menu(self);
		self.oVBox.pack_start(self.oMenu.oMenuBar, False, True, 0);
		self.oMenu.oMenuBar.show();
	pass

	def _windowSetUp(self, title, size) :
		self.set_title(title);
		self.set_size_request(size['w'], size['h']);
	pass # / _windowSetUp

	def _addMainVBox(self) :
		self.oVBox = gtk.VBox(False, 1);
		self.oVBox.show();
		self.add(self.oVBox);
	pass # /_addMainVBox

	def _addEventListeners(self) :
		self.attachEvent("destroy", self._closeWindow);
		self.attachEvent('key-press-event', self._keyboardEvents);
	pass # /_addEventListeners

	def attachEvent(self, event, handler, data = None) :
		self.connect(event, handler, data);
	pass # /attacheEvent

	def _closeWindow(self, window, event, data = None) :
		gtk.main_quit();
	pass # /_closeWindow

	def _keyboardEvents(self, window, event, data = None) :
		keyval = event.keyval;
		if self.keyPressed('left', keyval) :
			self.moveLeft();
		elif self.keyPressed('right', keyval) :
			self.moveRight();
		elif self.keyPressed('up', keyval) :
			self.moveUp();
		elif self.keyPressed('down', keyval) :
			self.moveDown();
		pass # /if
	pass # /_keyboardEvents

	def moveDown(self):
		self.oGame.oPlayer.down();
	pass # /moveDown

	def moveUp(self):
		self.oGame.oPlayer.up();
	pass # /moveUp

	def moveLeft(self):
		self.oGame.oPlayer.left();
	pass # /moveLeft

	def moveRight(self):
		self.oGame.oPlayer.right();
	pass #/ moveRight

	def keyPressed(self, key, val):
		if self.KEY[key] == val :
			return True;
		return False;
	pass # /keyPressed

	def displayScore(self, score):
		self.oScoreBar.set_text("Wynik: %d" % score);
	pass

	def displayLifes(self, lifes):
		self.oLifeBar.set_text("Życia: %d" % lifes);
	pass

pass # klasa
