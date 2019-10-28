#!/usr/bin/env python
# coding: utf-8

# In[7]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Week 9 assingment part 1

# Write a script called “football_stats.py” that will load this URL, parse it using BeautiulSoup, 
# and output the list of top 20 players, including the player’s position, team and total number of touchdowns 

import urllib.request as request
from bs4 import BeautifulSoup


def main():
    url = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns'
    webPage = request.urlopen(url)
    soup = BeautifulSoup(webPage, 'html.parser')
    stats = soup.find_all("table", attrs={"class": "data"})[
        0].find_all('tr', attrs={"valign": "top"})
    counter = 0
    print ("Top 20 NFL players ranked by most touchdowns scored in 2018:\n")
    for stat in stats:
        name = stat.find_all('td')[0].find_all('a')[0].contents[0]
        position = stat.find_all('td')[1].contents[0]
        team = stat.find_all('td')[2].find_all('a')[0].contents[0]
        tds = stat.find_all('td')[6].contents[0]
        counter += 1
        print ("Rank:{}, Player Name: {}, Position: {}, "
               "Team: {}, TDs: {}".format(counter, name, position, team, tds))
        if counter >= 20:
            break


if __name__ == '__main__':
    main()


# In[ ]:




