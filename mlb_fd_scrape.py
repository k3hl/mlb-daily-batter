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

f = open('c:\\temp\\goup.out','w')

playerAtt = []
for player in goup('td'):
    if  player.text is None:
        print(player.findtext('div'), file=f)
    else:
        print(player.text,file=f)








