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
        print( "Loading " + self.url)
        self.site =  site.read()
        self.getLinks()

class Down:
    links=[]
    localpath =""
    ptype = ""
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

    def load(self, url, i):
        #downloads the iPhone Wallpaper from mantia.me/wallpaper/XXX
        # webFile = urllib2.urlopen(url)
        # if not os.path.exists(self.localpath):
        #     os.makedirs(self.localpath)
        # localFile = open(self.localpath + "/"+ url.split('/')[-1], 'w')
        # localFile.write(webFile.read())
        # webFile.close()
        # localFile.close()

        webFile = urllib2.urlopen(url)
        localFile = open(self.localpath + "/" + url.split('/')[-1], 'w')
        meta = webFile.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print("[" + str(i) + "/" + str(len(c.links)) + "] Downloading: {0} Bytes: {1}".format(url, file_size))

        file_size_dl = 0
        block_sz = 4096
        while True:
            buffer = webFile.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            localFile.write(buffer)
            p = float(file_size_dl) / file_size
            status = r"{0}  [{1:.2%}]".format(file_size_dl, p)
            status = status + chr(8)*(len(status)+1)
            sys.stdout.write(status)

        localFile.close()

def usage():
    print "Usage:"
    print ""
    print "python mantiacrawl.py <localpath> <type>"
    print ""
    print "Es werden ZWEI Argumente erwartet:"
    print "<LOCALPATH> lokaler Pfad in dem die Bilder gespeichert werden sollen."
    print "<TYPE> 3 Möglichkeiten: iphone, wallpaper, fullscreen; bestimmt die Art des Wallpapers"
    print ""
    print "Example: python mantiacrawl.py mantia/iphone/ iphone"
    print ""
    exit()

if len(sys.argv)==3: #check for right number of arguments
    if sys.argv[1] is not None and sys.argv[2] is not None:
        localpath = sys.argv[1]
        ptype = sys.argv[2]
        print "Downloading everything on " + site_url + ptype + " to " + localpath
        c = Crawl(site_url)
        print "Fetched all links."

        d = Down(c.links,localpath,ptype)
        print "Starting download."
        i = 1
        for link in c.links:
            d.load(d.getDownloadLink(link), i)
            i += 1
            
else:
    usage()