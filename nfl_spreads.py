#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a script called “nfl_spreads.py” that will load this URL, parse it using BeautifulSoup, 
# and output the favorite, the underdog and the spread of a given game.

from bs4 import BeautifulSoup
import json
import urllib.request as request 

url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'
webPage = request.urlopen(url)
soup = BeautifulSoup(webPage.read(), "html.parser")
table = soup.find_all('table', attrs={"cols":"4"})

def main():
    for row in table:
        td = row.find_all("tr")

        try:
            favorite = str(td[1].get_text())
            underdog= td[3].get_text()
            spread = td[2].get_text()

        except:
            continue
    
        print ("{} {} {}".format(favorite, underdog, spread))


if __name__ == '__main__':
    main()
 


# In[ ]:




