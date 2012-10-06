#! /usr/bin/python
# -*- coding: utf-8 -*-
import os

import urllib2
from bs4 import BeautifulSoup
import sys

site_url = "http://mantia.me/wallpaper/"

class Crawl:
    url=""
    site=""
    links = []
    def __init__(self,url):
        self.url = url
        self.sitecrawl()

    def getLinks(self,html=None):
        if html==None:
            html = self.site
        dom = BeautifulSoup(html)
        alinks = dom.find("div", id="archives").find_all("a")
        for link in alinks:
            self.links.append(link.get("href"))

    def sitecrawl(self):
        site = urllib2.urlopen(self.url)
        print( "opened: " + self.url)
        self.site =  site.read()
        self.getLinks()

class Down:
    links=[]
    localpath ="iphone/"
    ptype = "iphone"
    def __init__(self,links, localpath, ptype):
        self.links = links
        self.localpath = localpath
        self.ptype = ptype

    def getDownloadLink(self,link):
        site = urllib2.urlopen(link)
        html =  site.read()
        dom = BeautifulSoup(html)
        dll = dom.find("a",class_=self.ptype)
        return dll.get("href")

    def load(self, url):
        """downloads the iPhone Wallpaper from mantia.me/wallpaper/XXX"""
        webFile = urllib2.urlopen(url)
        if not os.path.exists(self.localpath):
            os.makedirs(self.localpath)
        localFile = open(self.localpath + "/"+ url.split('/')[-1], 'w')
        localFile.write(webFile.read())
        webFile.close()
        localFile.close()
def usage():
    print "usage:"
    print ""
    print "python mantiacrawl.py <localpath> <type>"
    print ""
    print "Es werden ZWEI argumente erwartet:"
    print "<LOCALPATH> lokaler pfad wo die Bilder gespeichert werden sollen."
    print "<TYPE> 3 möglichkeiten: iphone, wallpaper, fullscreen bestimmt die art des wallpapers"
    print ""
    print "Example: python mantiacrawl.py mantia/iphone/ iphone"
    print ""
    exit()

if len(sys.argv)==3:
    if sys.argv[1] is not None and sys.argv[2] is not None:
        localpath = sys.argv[1]
        ptype = sys.argv[2]
        print localpath
        print ptype
        if ptype =="iphone" or ptype=="wallpaper" or ptype == "fullscreen":
            c = Crawl(site_url)
            print ""
            print ""
            print "Liste fertig"
            print ""

            d=Down(c.links,localpath,ptype)
            print "DOWN initialisiert"
            for link in c.links:
                print "wird aufgerufen: " + link
                d.load(d.getDownloadLink(link))
else:
    usage()