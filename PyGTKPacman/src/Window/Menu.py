#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk
from Forms import *
from Game.Settings import *

__version__ = "0.1"
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>"
__date__    = "$2010-04-11 13:04:12$"


class Menu :

	'''
	Klasa odpowiedzialna za menu
	'''

	oMenuBar = None;
	oWindow  = None;
	oSettings = None;

	def _newGame(self, w, data):
		'''
		handler wlaczenia nowej gry
		'''
		self.oWindow.oGame.restart();
	pass

	def _aboutGame(self, w, data):
		'''
		handler pomocy
		'''
		self.oWindow.help("PACMAN\nautor: Patryk Jar\nZbieraj Ciasteczka,\nuciekaj przed duchami,\nzjadaj je");
	pass

	def _quit(self, w, data):
		'''
		handler zakonczenia gry
		'''
		self.oWindow.quit();
	pass

	def __init__(self, window):
		'''
		konstruktor
		'''
		self.oWindow = window;
		self.oSettings = self.oWindow.oGame.oSettings;
		self.menu_items = (
			( "/_Plik",	None, None, 0, "<Branch>" ),
			( "/Plik/_Nowa Gra", "<control>N", self._newGame, 0, None ),
			( "/Plik/sep1", None, None, 0, "<Separator>" ),
			( "/Plik/Quit", "<control>Q", self._quit, 0, None ),
			( "/_Opcje", None, None, 0, "<Branch>" ),
			( "/Opcje/Ustawienia", None, self._settings, 0, None ),
			( "/_Pomoc", None, None, 0, "<LastBranch>" ),
			( "/_Pomoc/O Programie", None, self._aboutGame, 0, None ),
		);
		self.oMenuBar = self._createMainMenu();
	pass

	def _settings(self, button, widget, data=None) :
		'''
		ustawienia gry
		'''
		settings = Options()\
				.add(	'iLifes',
						label = "Liczba żyć",
						value = self.oSettings.iLifes,
						style="integer(lower=0, upper = 5)")\
				.add(	'iEnemies',
						label = "Liczba wrogów",
						value = self.oSettings.iEnemies,
						style="integer(lower=0, upper = 10)");
		create_gtk_dialog(settings).run();
		self.oSettings.iLifes = settings.iLifes;
		self.oSettings.iEnemies = settings.iEnemies;
	pass

	def _createMainMenu(self):
		'''
		Tworzenie glownego menu
		'''
		window = self.oWindow;
		accel_group = gtk.AccelGroup()
		item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", accel_group)
		item_factory.create_items(self.menu_items)
		window.add_accel_group(accel_group)
		self.item_factory = item_factory
		return item_factory.get_widget("<main>")
	pass
pass

