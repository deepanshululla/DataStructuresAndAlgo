#!/usr/bin/python
## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.
class ParkingLot:
    def __init__(self,numSpotsTotal):
        super(ParkingLot, self).__init__()
        self.nst=numSpotsTotal
        self.nsf=0
        self.nsv=numSpotsTotal
    
    def isVacant(self,v):
        if self.nsv>v.spotsNeeded:
            return True
        else:
            return False
            
    
    def parkVehicle(self,v):
        if (self.isVacant(v)):
            self.nsv-=v.spotsNeeded
            print "Your vehicle of color %s is parked.Remaining spts=%d"%(v.color,self.nsv)
        else:
            print "Sorry no space left"
    
    def unparkVehicle(self,v):
        self.nsv+=v.spotsNeeded
        print "Your vehicle of color %s is unparked.Remaining spts=%d"%(v.color,self.nsv)
            
class Vehicle(object):
    def __init__(self):
        super(Vehicle, self).__init__()
        self.spotsNeeded=0
        self.color="red"
class Car(Vehicle):
    def __init__(self,color):
        super(Car, self).__init__()
        self.spotsNeeded=2
        self.color=color
        

c=Car('green')
p=ParkingLot(5)
p.parkVehicle(c)    