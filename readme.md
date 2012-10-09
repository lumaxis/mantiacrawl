#mantiacrawl
Created by Lukas Spieß (blubser) & Oliver Fesseler (ofesseler)

There are quite a lot of awesome wallpapers for your iPhones, iPads and Macs on http://mantia.me/wallpaper/. But if you're like me and like to browse through those comfortably on your computer without having to click through dozens of sub pages, mantiacrawl is made for you.
Just specify where and in which format you want to have them and this script does the job for you.

Also, we used this to play around with Python a little bit, so don't bother if something isn't done the most efficient or easy way.

## Usage:
python mantiacrawl.py <localpath> <type>
mantiacrawl expects two arguments:

    <localpath>      your local path where you want to save the downloaded files  
    <type>           choose which version of the wallpapers you want to download: iphone, wallpaper or fullscreen


Example: 

    python mantiacrawl.py download/iphone/ iphone

## Contributors:
[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) and their beautifully easy HTML scraping library.  
You need to install it either via

    pip install beautifulsoup4
or via

    easy_install beautifulsoup4

Also, you need to have Python installed. Obviously.
(Still only works on Unix operating systems)