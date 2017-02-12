from __future__ import print_function
import math

class Shape():
	def __init__(self):
		self.color="red"
		self.sides=0

class Square(Shape):
	#square class is child of Shape parent class
	def __init__(self,w,c):
		Shape.__init__(self)
		self.width=w
		self.color=c
		
sq1=Square(5,"Blue")
sq2=Square(9,"green")

print("Square 1:",sq1.width,',',sq1.color,",","Square 2:",sq2.width,",",sq2.color)