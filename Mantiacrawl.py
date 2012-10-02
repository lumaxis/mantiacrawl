#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import urllib2

site = urllib2.urlopen("http://mantia.me/wallpaper/")
print site.read()

