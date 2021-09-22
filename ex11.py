import turtle
import numpy as np

def circ(r):
	for i in range(0, 30, 1):
		turtle.left(6)
		turtle.forward(r)
		turtle.left(6)

turtle.shape('turtle')
r = 1
turtle.left(90)
for i in range(5, 16, 1):
	circ(r*i)
	circ(-r*i)
