#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk
from Forms import *

__version__ = "0.1"
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>"
__date__ ="$2010-04-11 13:04:12$"


class Menu :

	oMenuBar = None;
	oSettings = None;

	def _print_hello(self, w, data):
		print "Hello, World!";

	def __init__(self, window):
		self.menu_items = (
			( "/_Plik",	None, None, 0, "<Branch>" ),
			( "/Plik/_Nowa Gra", "<control>N", self._print_hello, 0, None ),
			( "/Plik/sep1", None, None, 0, "<Separator>" ),
			( "/Plik/Quit", "<control>Q", gtk.main_quit, 0, None ),
			( "/_Opcje", None, None, 0, "<Branch>" ),
			( "/Opcje/Ustawienia", None, self._settings, 0, None ),
			( "/_Pomoc", None, None, 0, "<LastBranch>" ),
			( "/_Pomoc/O Programie", None, None, 0, None ),
		);
		self.oMenuBar = self._createMainMenu(window);
	pass

	def _settings(self, button, widget, data=None) :
		self.oSettings = Options()\
				.add('iLives',
					label = "Liczba żyć",
					value = 3,
					style="integer(lower=0, upper = 5)")\
				.add('iEnemies', label = "Liczba wrogów", value = 3,
					style="integer(lower=0, upper = 10)")
		create_gtk_dialog(self.oSettings).run();
	pass

	def _createMainMenu(self, window):

		accel_group = gtk.AccelGroup()
		item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", accel_group)
		item_factory.create_items(self.menu_items)
		window.add_accel_group(accel_group)
		self.item_factory = item_factory

		return item_factory.get_widget("<main>")
	pass
pass
