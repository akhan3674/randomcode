# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:01:03 2015

@author: akhan
"""

# IMDB
import imdbpie
title="The Hunger Games: Mockingjay - Part 2"
imdbApi=imdbpie.Imdb()
searchresults=imdbApi.find_by_title(title)
mj=[x for x in searchresults if x['title']==title][0]
mj=imdbApi.find_movie_by_id(mj['imdb_id'])
mj.rating

# Rotten Tomatoes
from bs4 import BeautifulSoup
import requests
import re

url="http://www.rottentomatoes.com/m/the_hunger_games_mockingjay_part_2/"
#url="http://www.rottentomatoes.com/m/secret_in_their_eyes_2015/"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")

table=soup.find("div",{"id":"mainColumn"})
table=soup.find("div",{"id":"topSection"})
table=soup.find("div",{"class":"audience-info hidden-xs superPageFontColor"})
print table.find_all("div")[0].text

# Metacrtic 
url="http://www.metacritic.com/movie/the-hunger-games-mockingjay---part-2/"
#url="http://www.rottentomatoes.com/m/secret_in_their_eyes_2015/"
r=requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
soup=BeautifulSoup(r.text)

table=soup.find_all("div",{"class":"metascore_w user large movie positive"})
table=table[0]
print table.text


