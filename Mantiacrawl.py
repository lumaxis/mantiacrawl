#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
site_url = "http://mantia.me/wallpaper/"

def getLinks(html):
	dom = BeautifulSoup(html)
	alinks = dom.find("div", id="archives").find_all("a")
	for link in alinks:
		print link.get("href")

def sitecrawl(site_url):
	site = urllib2.urlopen(site_url)
	print "opened: " + site_url
	dom_string =  site.read()
	getLinks(dom_string)

url = "http://mantia.me/wallpaper/"

