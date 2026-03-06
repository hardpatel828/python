# Write a Python program to print a triangle using Turtle.

# Import turtle module
import turtle

# Create turtle object
t = turtle.Turtle()

# Draw triangle
for i in range(3):
    t.forward(100)   # move forward
    t.left(120)      # turn left

# Keep the window open
turtle.done()