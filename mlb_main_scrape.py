'''
Created on Apr 17, 2015

@author: rkehl
'''

from mlb_scrape import Scrape

fdmlb = Scrape('https://www.fanduel.com/e/Game/12110?new_contest=1&stakelist=1x0&isLeague=false&isPublic=true')
fdmlb.run_player_scrape(fdmlb.pile)

for p in fdmlb.finalData: print p

rotoinj = Scrape('http://www.rotoworld.com/teams/injuries/mlb/all/')
rotoinj.run_roto_inury(rotoinj.pile)
