from turtle import *

from time import sleep

def soma_2(x):
    return x + 2

def plano_cartesiano():
    #plano cartesino
   t.pu()
   t.goto(-300, 0)
   t.pd()
   t.goto(300, 0)
   t.stamp()

# Eixo do Y
   t.pu()
   t.goto(0, -300)
   t.pd()
   t.goto(0, 300)
   t.lt(90)
   t.stamp()

t = Turtle()

plano_cartesiano()

def função_1(X):
    return X**0.5

def função_2(x):
    return 1//x

def função_3(x):
    return 2**x


#funcao 1
t.color('blue')
t.pu()
t.goto(0, função_1(0))
t.pd()
for x in range(0, 201):
    t.goto(x, função_1(x))

sleep(2)
t.clear()

#funcao 2
t.seth(0)
t.color('black')
plano_cartesiano()

t.seth(0)
t.color('red')
t.pu()
t.goto(1, função_2(100))
t.pd()
for x in range(50, 301):
    t.goto(x, função_2(x))

sleep(2)
t.clear()


#funçaõ 3
t.seth(0)
t.color('black')
plano_cartesiano()

t.seth(0)
t.color('red')
t.pu()
t.goto(1, função_3(100))
t.pd()
for x in range(50, -301):
    t.goto(x, função_3(x))

mainloop()