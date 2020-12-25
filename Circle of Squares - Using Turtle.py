#                                       ...Circle Of Squares...

import turtle

pri = turtle.Turtle()
pri.speed(100)


def square(angle):
    pri.forward(100)
    pri.right(angle)
    pri.forward(100)
    pri.right(angle)
    pri.forward(100)
    pri.right(angle)
    pri.forward(100)
    pri.right(angle + 10)


for i in range(36):
    square(90)
