'''
Created on Apr 17, 2015

@author: rkehl
'''
from __future__ import print_function
from pyquery import PyQuery as pquery
from lxml import etree
import requests
import re
from itertools import tee, islice, chain, izip

class Scrape:
    
    def __init__(self, site):
        self.site = requests.get(site)
        self.siteID = ""
        self.xpath = ""
        self.pile = pquery(self.site.content)
        self.finalData = []
    
    def previous_and_next(self, iterable):
        prevs, items, nexts = tee(iterable, 3)
        prevs = chain([None], prevs)
        nexts = chain(islice(nexts, 1, None), [None])
        return izip(prevs, items, nexts)
    
    def run_player_scrape(self, pile):
        counter = 0
        s_data  = ""
        
        for player in pile('td'):
            if  player.text is None and player.findtext('div') is not None:
                s_data+=player.findtext('div').lstrip() + "|"
            elif player.text is not None:
                s_data+=player.text.lstrip() + "|"
            else:
                s_data+="HOME|"
            counter+=1
    
            if counter == 7:
                self.finalData.append(s_data)
                counter = 0
                s_data=""
    
    def run_roto_inury(self, pile):
        f = open('c:/temp/injury', 'w')
        counter = 0
        s_data  = ""
        
        for team in pile('div').filter('.pb'):
            epos_re=re.compile('^[0-9][0-9]...')
            esta_re=re.compile('(?=^[A-Z].* [A-Z])')
            data=(team.xpath('//div/div/div/table/tr[position()>1]/td//text()[normalize-space()]'))
            for previous, item, nxt in self.previous_and_next(data):
                if counter == 4 and nxt is not None and epos_re.match(nxt.encode('utf-8')):
                    s_data+=item.encode('utf-8') + "|NULL|"
                    counter+=1
                elif counter == 7 and nxt is not None and esta_re.match(nxt.encode('utf-8')):
                    s_data+=item.encode('utf-8') + "|NULL|"
                    counter+=2
                else:   
                    s_data+='|' + item.encode('utf-8') + "|"
                
                counter+=1
                if counter == 10:
                    self.finalData.append(s_data)
                    counter = 0
                    s_data=""
                
            print(*self.finalData,sep='\n\n', file=f)
        

