from functools import total_ordering
from math import floor

@total_ordering
class Party:
    def __init__(self,name, pct):
        self.name = name
        self.pct = pct
        self.seats = 0

    def __eq__(self, other):
        return self.effective() == other.effective()
    def __ne__(self, other):
        return self.effective() != other.effective()

    def __lt__(self, other):
        return self.effective() < other.effective()

    
    def __repr__(self):
        return "%s : %d (%f, %f)" % (self.name, self.seats, self.low, self.high)
    
    def effective(self):
        return self.pct / (1 + self.seats)

def dhondt(parties, seats):
    for i in range(seats):
        parties.sort()
        thresh = parties[-1].effective()
        parties[-1].seats += 1
        ls = parties[-1]
    for p in parties:
        td = parties[-2].effective()
        p.low = thresh* (1-p.pct/thresh + floor(p.pct/thresh))
        p.high = td*(p.pct/td - floor(p.pct/td))
        
    return parties

# data from https://hanburystrategycloud.filecloudonline.com/url/9c7c2cjz8c2ps8rb

SW = [
    Party("CON", 25.5),
    Party("LAB", 28.4),
    Party("LD", 13.4),
    Party("BRX", 16.8),
    Party("UKIP", 5),
    Party("CUTIG", 5.3),
    Party("GRN", 5)
    ]

SCO = [
    Party("CON", 24.30),
    Party("LAB", 21.70),
    Party("SNP", 32.20)
    ]    

def pprint(x):
    x.sort()
    for i in x:
        print (i)
    
x = dhondt(SCO, 6)
pprint (x)
