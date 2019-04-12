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

def dhondt( parties, seats):
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

EastMidlands = [ 
Party("CON",25.20),
Party("LAB",50.40),
Party("LD",2.70),
Party("BRX",8.40),
Party("UKIP",3.40),
Party("TIG",4.50),
Party("GRN",3.40),
Party("SNP",0.00),
Party("PC",0.00),
Party("OTH",1.90)]
 

EastOfEngland = [
Party("CON",24.40),
Party("LAB",25.50),
Party("LD",13.20),
Party("BRX",13.10),
Party("UKIP",11.30),
Party("TIG",9.90),
Party("GRN",2.10),
Party("SNP",0.00),
Party("PC",0.00),
Party("OTH",0.50)]

London = [
Party("CON",14.70),
Party("LAB",48.00),
Party("LD",11.20),
Party("BRX",8.80),
Party("UKIP",10.40),
Party("TIG",4.90),
Party("GRN",1.50),
Party("SNP",0.00),
Party("PC",0.00),
Party("OTH",0.50)]

NorthEast = [
Party("CON",15.00),
Party("LAB",62.40),
Party("LD",2.00),
Party("BRX",6.00),
Party("UKIP",8.70),
Party("TIG",0.00),
Party("GRN",4.30),
Party("SNP",0.00),
Party("PC",0.00),
Party("OTH",1.70)]

NorthWest = [
Party("CON",22.00),
Party("LAB",48.20),
Party("LD",4.80),
Party("BRX",10.20),
Party("UKIP",11.70),
Party("TIG",1.00),
Party("GRN",2.10),
Party("SNP",0.00),
Party("PC",0.00),
Party("OTH",0.00)]

Scotland = [
Party("CON",24.30),
Party("LAB",21.70),
Party("LD",5.00),
Party("BRX",4.90),
Party("UKIP",3.90),
Party("TIG",6.00),
Party("GRN",1.80),
Party("SNP",32.20),
Party("PC",0.00),
Party("OTH",0.00)]

SouthEast = [
Party("CON",34.20),
Party("LAB",25.50),
Party("LD",8.90),
Party("BRX",11.60),
Party("UKIP",6.20),
Party("TIG",5.20),
Party("GRN",7.90),
Party("SNP",0.00),
Party("PC",0.00),
Party("OTH",0.50)]

SouthWest = [
Party("CON",25.50),
Party("LAB",28.40),
Party("LD",13.40),
Party("BRX",16.80),
Party("UKIP",5.00),
Party("TIG",5.30),
Party("GRN",5.00),
Party("SNP",0.00),
Party("PC",0.00),
Party("OTH",0.60)]

Wales = [
Party("CON",17.10),
Party("LAB",38.50),
Party("LD",12.20),
Party("BRX",11.00),
Party("UKIP",3.50),
Party("TIG",1.40),
Party("GRN",6.70),
Party("SNP",0.00),
Party("PC",3.20),
Party("OTH",6.40)]

WestMidlands = [
Party("CON",21.30),
Party("LAB",48.20),
Party("LD",4.90),
Party("BRX",11.00),
Party("UKIP",7.20),
Party("TIG",3.80),
Party("GRN",3.60),
Party("SNP",0.00),
Party("PC",0.00),
Party("OTH",0.00)]

YorkshireAndTheHumber = [
Party("CON",19.20),
Party("LAB",43.60),
Party("LD",7.30),
Party("BRX",11.60),
Party("UKIP",10.40),
Party("TIG",0.00),
Party("GRN",5.90),
Party("SNP",0.00),
Party("PC",0.00),
Party("OTH",2.10)]

regions = [ ("East Midlands", EastMidlands, 5),
            ("East", EastOfEngland, 7),
            ("London", London, 8),
            ("North East", NorthEast, 3),
            ("North West", NorthWest, 8),
            ("Scotland", Scotland, 6),
            ("South East", SouthEast, 10),
            ("South West", SouthWest, 6),
            ("Wales", Wales, 4),
            ("West Midlands", WestMidlands, 7),
            ("Yorkshire and the Humber", YorkshireAndTheHumber, 6) ]
            
    
def pprint(x):
    x.sort()
    for i in x:
        if i.pct > 5: #arbitrary cutoff
            print (i)
    print()
    
for n, r,s  in regions:
    print (n)
    pprint( dhondt(r, s) )
    
