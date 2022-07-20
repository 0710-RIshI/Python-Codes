suits=('Hearts','Spade','Clubs','Diamond')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
value={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

import random

class card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=value[rank]
    
    def __str__(self):
        return f"{self.suit} of {self.rank}"
    
class Deck:
    def __init__(self):
        self.l=[]
        
        for i in suits:
            for j in ranks:
                
                self.l.append(card(i,j))

    def shuffle(self):
        random.shuffle(self.l) 

class Player():
    def __init__(self,name):
        self.name=name
        self.Deck=[]
  

    def addcard(self,newcard):
            if type(newcard) == type([]):
                self.Deck.extend(newcard)
            else:
                self.Deck.append(newcard)
        
    def removecard(self):
            return self.deck.pop(0)
        
    def __str__(self):
        return f'player {self.name} has {len(self.Deck)} cards in hand'
        
def game(game,p1,p2):
    while(game!=0):
        x=p1.removecard()
        y=p2.removecard()

        


p1 = Player('rishi')
p2 = Player('Gopi')

d = Deck()
d.shuffle()

p1.addcard(d.l[:25])
p2.addcard(d.l[26:52])


game=1
    


