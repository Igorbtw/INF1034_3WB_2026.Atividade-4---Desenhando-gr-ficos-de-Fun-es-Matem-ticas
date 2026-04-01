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

t.speed(10)


plano_cartesiano()

def função_1(X):
    return X**0.5

def função_2(x):
    return 1//x

def função_3(x):
    return 2**x

def função_4(x):
    return 5 - x**2

def função_5(x):
    return x**2 - 5*x + 6

def função_6(x):
    return x**3 - x**2 - x + 1


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
t.goto(-100, função_3(-100))
t.pd()
for x in range(-99, 9):
    t.goto(x, função_3(x))

sleep(2)
t.clear()


#funcao 4
t.seth(0)
t.color('black')
plano_cartesiano()

t.seth(0)
t.color('red')
t.pu()
t.goto(-20, função_4(-20))
t.pd()
for x in range(-21, 101):
    t.goto(x, função_4(x))

sleep(2)
t.clear()


#funcao 5
t.seth(0)
t.color('black')
plano_cartesiano()

t.seth(0)
t.color('red')
t.pu()
t.goto(-20, função_5(-20))
t.pd()
for x in range(-21, 101):
    t.goto(x, função_5(x))

sleep(2)
t.clear()

#funcao 6
t.seth(0)
t.color('black')
plano_cartesiano()

t.seth(0)
t.color('red')
t.pu()
t.goto(-30, função_6(-30))
t.pd()
for x in range(-30, 20):
    t.goto(x, função_6(x))

sleep(2)
t.clear()

mainloop()