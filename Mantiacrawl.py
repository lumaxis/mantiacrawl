#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
site_url = "http://mantia.me/wallpaper/"
## der lange String ist nur zum testen da.. 
## kommt auch weg sobald das geht =)
site_string = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
	<head>
		<title>Mantia  &raquo; Wallpaper</title>
	</head>
	<body class="wallpaper thursday oct4">
		<div id="content">
			<ul id="navigation">
				<li class="home"><a href="http://mantia.me">Home</a></li>
				<li class="wallpaper"><a href="http://mantia.me/wallpaper/">Wallpaper</a></li>
			</ul>
			<div id="feature">
				<img src="http://mantia.me/images/tomorrowlandcocacola_large.jpg" alt="Tomorrowland Coca-Cola" />
			</div>
			<div id="featuremeta">
				<div id="downloads">
					<a class="iphone" href="http://mantia.me/goodies/desktops/tomorrowlandcocacola_iphone.jpg" title="Download iPhone Wallpaper">Download iPhone Wallpaper</a>
					<a class="fullscreen" href="http://mantia.me/goodies/desktops/tomorrowlandcocacola_full.jpg" title="Download iPad Wallpaper">Download iPad Wallpaper</a>
					<a class="widescreen" href="http://mantia.me/goodies/desktops/tomorrowlandcocacola_wide.jpg" title="Download Desktop Wallpaper">Download Desktop Wallpaper</a>
				</div>
				<h2>Tomorrowland Coca-Cola</h2>
			</div>
			<div id="archives">
				<a href="http://mantia.me/wallpaper/tomorrowland-coke/" id="selected_thumbnail"><img src="http://mantia.me/images/tomorrowlandcocacola_small.jpg" alt="Tomorrowland Coca-Cola" title="Tomorrowland Coca-Cola" /></a>
				<a href="http://mantia.me/wallpaper/red-bricks/"><img src="http://mantia.me/images/redbricks_small.jpg" alt="Red Bricks" title="Red Bricks" /></a>
				<a href="http://mantia.me/wallpaper/orange-bricks/"><img src="http://mantia.me/images/orangebricks_small.jpg" alt="Orange Bricks" title="Orange Bricks" /></a>
			<hr /></div>
		</div>
	</body>
</html>"""



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
## wenn die seite geparsed werden soll 
#sitecrawl(url)
## zum testen:
getLinks(site_string)

