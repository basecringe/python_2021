from random import randint
import turtle
import numpy as np
turtle.shape('turtle')
turtle.hideturtle()

L=300 
number_of_turtles = 50
steps_of_time_number = 10000
speed_of_turtles = 3

turtle.tracer(0, 0) 
turtle.penup() 
turtle.goto(L,L)
turtle.pendown()
turtle.goto(-L,L)
turtle.goto(-L,-L)
turtle.goto(L,-L)
turtle.goto(L,L) 

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.goto(randint(-L+10, L-10), randint(-L+10, L-10))
    unit.setheading(randint(-180,180))
    unit.speed(10)

def collision(unit):
    x,y = unit.position()
    angle=unit.heading()
    if(x>L or x<-L):
        unit.setheading(180-angle)
        unit.setposition(np.sign(x)*(L-1),y) 
    elif(y>L or y<-L):
        unit.setheading(-angle)
        unit.setposition(x,np.sign(y)*(L-1))


for i in range(steps_of_time_number):
    turtle.tracer(1, 1)
    for unit in pool:
        collision(unit)
        unit.forward(speed_of_turtles)
        turtle.tracer(0, 0)
