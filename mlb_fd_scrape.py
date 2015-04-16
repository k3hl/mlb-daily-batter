'''
Created on Apr 15, 2015

@author: rkehl
'''
from __future__ import print_function
from pyquery import PyQuery as pquery
from lxml import etree
import requests

site = requests.get('https://www.fanduel.com/e/Game/12093?new_contest=1&stakelist=1x0&isLeague=false&isPublic=false')
goup = pquery(site.content)

counter	= 0
s_data	= 0
playerAtt = []
for player in goup('td'):
    if  player.text is None:
        s_data+=player.findtext('div') + "\|"
    else:
        s_data+=player.text + "\|"
    count+=1
    
    if count == 6:
    	playerAtt.append(s_data)
    	count = 0
    	s_data=""

	
	








