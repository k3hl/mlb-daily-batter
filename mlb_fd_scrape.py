'''
Created on Apr 15, 2015

@author: rkehl
'''
from __future__ import print_function
from pyquery import PyQuery as pquery
from lxml import etree
import requests


site = requests.get('https://www.fanduel.com/e/Game/12096?new_contest=1&stakelist=1x0&isLeague=false&isPublic=true')
goup = pquery(site.content)

counter	= 0
s_data	= ""
playerAtt = []
for player in goup('td'):
    if  player.text is None and player.findtext('div') is not None:
        s_data+=player.findtext('div').lstrip() + "|"
    elif player.text is not None:
        s_data+=player.text.lstrip() + "|"
    else:
        s_data+="HOME|"
    counter+=1
    
    if counter == 7:
        playerAtt.append(s_data)
        counter = 0
        s_data=""

for p in playerAtt: print(p)




