'''
Created on Apr 15, 2015

@author: rkehl
'''
class Player():
    'Base class for fd players'
    playerCount = 0
    
    def __init__(self, list):
        position  = ""
        firstName = ""
        lastName  = ""
        avgPoints = "0"
        gamesPlyd = "0"
        nextOpp   = ""
        dollarVal = "0"
        
        Player.playerCount += 1
    
    def displayPlayer(self):
        print("Position:  ",        self.position,   "\n",
              "First Name:  ",      self.firstName,  "\n",
              "Last Name:  ",       self.lastName,   "\n",
              "Average Points:  ",  self.avgPoints,  "\n",
              "Games Played:  ",    self.gamesPlyd,  "\n",
              "Next Opponent:  ",   self.nextOpp,    "\n",
              "Cost ($):  ",        self.dollarVal,  "\n")