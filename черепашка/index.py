import turtle as t
t.shape('turtle')
t.speed(10)

L1=10*2
L2=10*(2**0.5)*2
L3=20*2

dfont = []  #список кортежей

def read_data(file_name):
    input = open(file_name,encoding='utf8')
    lines = input.read().split('\n')
    for each_line in lines:
        dfont.append(eval(each_line))

def t_print(text):
    text=str(text)
    for i in text:
        for length, angle in dfont[int(i)]:
            t.forward(length)
            t.left(angle)
        t.penup()
        t.forward(2*L1)
        t.pendown()

read_data('dfont.txt')

#t_print('01234567')
t_print(141700)
