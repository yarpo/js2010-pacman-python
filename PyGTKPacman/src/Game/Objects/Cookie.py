#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1";
__author__  = "Patryk yarpo Jar <jar.patryk@gmail.com>";
__date__    = "$2010-04-11 18:05:03$";

from Object import *

class Cookie(Object) :

	_TYPE = {
		'normal' : 0,
		'extra'  : 1
	};
	_type = 0;

	def __init(self, x, y, type):
		Object.__init__(self, x, y);
		self.setType(type);
	pass

	def setType(self, type):
		try :
			self._type = self._TYPE[type];
		except:
			self._type = self._normal();
	pass

	def _normal(self):
		return self._TYPE['normal'];
	pass

	def _extra(self):
		return self._TYPE['normal'];
	pass

	def getType(self, type):
		return self._type;
	pass

	def isExtra(self):
		return (self.getType() == self._extra());
	pass

	def isNormal(self):
		return (self.getType() == self._normal());
	pass

pass