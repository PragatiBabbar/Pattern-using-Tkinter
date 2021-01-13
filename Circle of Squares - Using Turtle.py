"""   code by @PragatiBabbar   """

#importing module
import turtle

# storing module in a variable
pri = turtle.Turtle()

# specifying the speed
pri.speed(100)

# function to create circle using squares 
# moving the cursor accordingly
def square(angle):
    pri.forward(100)
    pri.right(angle)
    pri.forward(100)
    pri.right(angle)
    pri.forward(100)
    pri.right(angle)
    pri.forward(100)
    pri.right(angle + 10)

# using loop to generate pattern
for i in range(36):
    square(90)
