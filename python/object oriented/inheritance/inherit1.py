from __future__ import print_function
import math

class Shape():
	def __init__(self):
		self.color="red"
		self.sides=0

class Square(Shape):
	#square class is child of Shape parent class
	def __init__(self,w):
		Shape.__init__(self)
		self.width=w
		
sq1=Square(5)
sq2=Square(9)

print("Square size:",sq1.width,',',sq1.color,",",sq2.sides,",",sq2.color)