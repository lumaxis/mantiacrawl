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

    def getFileLink(self,link):
        site = urllib2.urlopen(link)
        html =  site.read()
        dom = BeautifulSoup(html)
        dll = dom.find("a",class_=self.ptype)
        return dll.get("href")

    def load(self, url, i):
        print "[" + str(i) + "/" + str(len(c.links)) + "] " + url.split('/')[-1]      
        while True:
            webFile = urllib2.urlopen(url)
            meta = webFile.info()
            webFile_size = int(meta.getheaders("Content-Length")[0])
            # Check if a file with that name already exists
            if os.path.exists(self.localpath + "/" + url.split('/')[-1]):
                localFile_size = os.path.getsize(self.localpath + "/" + url.split('/')[-1])
                # If a file with that name exists check if it is the exact same file
                if webFile_size == localFile_size:
                    print "Skipping, already exists."
                    break
            # If the file either doesn't already exist or has been updated/corrupted start download
            else:
                localFile = open(self.localpath + "/" + url.split('/')[-1], 'w')
                print "Downloading: {0} Size: {1} Bytes".format(url, webFile_size)
                file_size_dl = 0
                block_size = 4096
                while True:
                    buffer = webFile.read(block_size)
                    if not buffer:
                        break
                    file_size_dl += len(buffer)
                    localFile.write(buffer)

                localFile.close()
            break

def usage():
    """
    Usage:
        
        python mantiacrawl.py <localpath> <type>
    
    mantiacrawl expects two arguments:

        <localpath>      your local path where you want to save the downloaded files  
        <type>           choose which version of the wallpapers you want to download: iphone, wallpaper or fullscreen

    Example: 
        
        python mantiacrawl.py download/iphone iphone
    
    """
    exit()

if len(sys.argv)==3: #check for right number of arguments
    if sys.argv[1] is not None and sys.argv[2] is not None:
        localpath = sys.argv[1]
        ptype = sys.argv[2]
        print "Downloading everything on " + site_url + ptype + " to " + localpath
        c = Crawl(site_url)
        print "Fetched all links.\n"

        d = Down(c.links,localpath,ptype)
        print "Starting download."
        i = 1
        for link in c.links:
            d.load(d.getFileLink(link), i)
            i += 1
            
else:
    usage()