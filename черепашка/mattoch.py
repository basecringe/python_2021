import turtle as t
t.shape('turtle')
t.speed(10)
t.tracer(0, 0)
dt=0.3
ay=-9

x=-300
y=0
Vy=50
Vx=20

t.forward(500)
t.backward(1000)

t.goto(x,y)
t.tracer(1, 1)
for i in range(1,1000):
    x+=Vx*dt
    y+=Vy*dt
    Vy+=ay*dt
    if y<0:
        y=0
        Vy=-Vy*0.5
    t.goto(x,y)

