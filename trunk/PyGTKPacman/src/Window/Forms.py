#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.0.2"
__author__  = "Oreste Notelli <oreste.notelli@sischema.com>"

'''
-------------------------------------------------------------------------------
    Copyright  (C) 2004, Oreste Notelli <oreste.notelli@sischema.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Library General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the
    Free Software Foundation, Inc.,
    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

    Sischema s.r.l.
    via Sebenico, 22
    20124 Milano - Italia
    tel-fax: (+39)0266823882
-------------------------------------------------------------------------------
'''


import types

class Options:
    def __init__(self):
        self.__options=[]

    def __get_type(self, value):
        return type(value)

    def add_object(self, object):
        return self.add_dict(object.__dict__)

    def add_dict(self, dict):
        for elem in dict:
            self.add(elem, value=dict[elem])
        return self

    def add(self, name, label=None, type=None, style=None, value = None):
        if (label == None):
            _label=name
        else:
            _label = label
        _type = types.StringType
        if (type == None):
            if (value != None):
                _type = self.__get_type(value)
        else:
            _type = type

        if (style == None):
            _style = self.__get_preferred_style(_type)
        else:
            _style = style

        self.__options.append({'name':name,
                               'label': _label,
                               'type':_type,
                               'style':_style,
                               'value':value})
        self.__dict__[name] = value
        return self

    def sync_dict(self):
        for o in self.__options:
            self.__dict__[o['name']]=o['value']

    def __get_preferred_style(self, type):
        style = 'entry()'
        if (type == types.IntType):
            style = 'integer()'
        if (type == types.BooleanType):
            style = "boolean()"
        return style

    def __iter__(self):
        return self.__options.__iter__()

    def __repr__(self):
        result ="option object:\n"
        for o in self.__options:
            result += str(o)+"\n"
        return result

###############################################################################

import gtk

class base_style:
    def create_label_widget(self, labels, option):
        l = gtk.Label(option['label']+ ": ")
        l.set_justify(gtk.JUSTIFY_RIGHT)
        a = l.get_alignment()
        l.set_alignment(0,a[1])
        labels.pack_start(l, True ,True,0)

class boolean:
    class __value_widget:
        def __init__(self, checkbutton, option):
            self.__entry = checkbutton
            self.__option = option

        def save_to_binding(self):
            self.__option['value'] = \
                               self.__option['type'](self.__entry.get_active())


    def create_label_widget(self, labels, option):
        labels.add(gtk.Label())

    def create_value_widget(self, values, option):
        e = gtk.CheckButton(option['label'])
        values.add(e)
        e.set_active(bool(option['value']))
        return self.__value_widget(e, option)

class integer(base_style):
    class __value_widget:
        def __init__(self, spin, option):
            self.__entry = spin
            self.__option = option

        def save_to_binding(self):
            self.__option['value'] = \
                                self.__option['type'](self.__entry.get_value())

    def __init__ (self, lower=-2147483647 , upper =2147483647, step = 1):
        self.__lower = lower
        self.__upper = upper
        self.__step = step

    def create_value_widget(self, values, option):
        if (option['value'] == None):
            val= 0
        else:
            val = int(option['value'])
        spin = gtk.SpinButton(gtk.Adjustment(val,
                                             self.__lower,
                                             self.__upper,
                                             self.__step))
        values.add(spin)
        return self.__value_widget(spin, option)

class entry(base_style):
    class __value_widget:
        def __init__(self, entry, option):
            self.__entry = entry
            self.__option = option

        def save_to_binding(self):
            self.__option['value'] = \
                                 self.__option['type'](self.__entry.get_text())

    def create_value_widget(self, values, option):
        e = gtk.Entry()
        values.add(e)
        val = option['value']
        if (val != None):
            e.set_text(str(val))
        return self.__value_widget(e, option)

def __get_style(style_string):
    return eval(style_string)

def __create_widgets(labels, values, option):
    style = __get_style(option['style'])
    style.create_label_widget(labels, option)
    return style.create_value_widget(values, option)

def __empty_callback():
    pass

def __response(dialog, b, widgets, options, callback):
    if (gtk.RESPONSE_OK == b):
        for widget in widgets:
            widget.save_to_binding()
        # hmmm, not aesthetically pleasing interface...
        options.sync_dict()
        callback()
    dialog.hide()

def create_gtk_widgets(options):
    labels = gtk.VBox()
    values = gtk.VBox()
    main = gtk.HBox()
    main.add(labels)
    main.add(values)
    widgets =[]
    for option in options:
        widgets.append(__create_widgets(labels, values, option))
    return main, widgets

def create_gtk_dialog(options,
                     title = None,
                     parent = None,
                     flags = 0,
                     buttons = None,
                     callback = __empty_callback):

    if (buttons==None):
        _buttons = ((gtk.STOCK_CANCEL,
                                     gtk.RESPONSE_CANCEL,
                                     gtk.STOCK_OK,
                                     gtk.RESPONSE_OK))
    else:
        _buttons = buttons
    window = gtk.Dialog(buttons = _buttons )
    window.set_default_response(gtk.RESPONSE_OK)
    main, widgets = create_gtk_widgets(options)
    window.vbox.add(main)
    window.connect("response", __response, widgets, options, callback)
    window.show_all()
    return window

class __sync_callback:
    def __init__(self, callback, dict, options):
        self.__dict = dict
        self.__options = options
        self.__callback = callback
    def __call__(self):
        dict = self.__options.__dict__.copy()
        del dict['_options__options']
        self.__dict.update(dict)
        self.__callback()

def create_gtk_dialog_from_dict (dictionary,
                                 title = None,
                                 parent = None,
                                 flags = 0,
                                 buttons = None,
                                 response_callback = __empty_callback):
    o = options().add_dict(dictionary)
    d = create_gtk_dialog(o,
                          title,
                          parent,
                          flags,
                          buttons,
                          __sync_callback(response_callback, dictionary, o))
    return d

def create_gtk_dialog_from_object (object,
                                 title = None,
                                 parent = None,
                                 flags = 0,
                                 buttons = None,
                                 response_callback=__empty_callback):
    return create_gtk_dialog_from_dict(object.__dict__,
                                       title,
                                       parent,
                                       flags,
                                       buttons,
                                       response_callback)
