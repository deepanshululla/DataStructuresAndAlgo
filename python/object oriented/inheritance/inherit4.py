from __future__ import print_function
import math

class Shape():
	def __init__(self):
		self.color="red"
		self.sides=0
	def calcArea(self):
		return 0
		
class Square(Shape):
	#square class is child of Shape parent class
	def __init__(self,w,c):
		Shape.__init__(self)
		self.width=w
		self.color=c
		
class Circle(Shape):
	def __init__(self,r,c):
		Shape.__init__(self)
		self.radius=r
		self.color=c
		
sq1=Square(5,"Blue")
sq2=Square(9,"green")
circle1=Circle(10,"orange")

print("Square 1: ",sq1.width,',',sq1.color,", \n","Square 2:",sq2.width,",",sq2.color)
print("Circle1: ",circle1.radius,circle1.color)
print("area of circle is ",circle1.calcArea())