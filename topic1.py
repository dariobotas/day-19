"""Python Higher Order Functions & Event Listeners"""
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
  tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()

#Functions as Inputs
#def function_a(something):
	#Do this with something
	#Then do this
	#Finally do this

#def function_b():
	#Do this

#function_a(function_b)
#########################
#Example
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

#High order functions
def calculator(n1, n2, func):
  return func(n1, n2)

print(calculator(1, 2, add))

#########################
#Positional Arguments
#def function_a(a, b, c):
	#Do this with a
	#Then do this with b
	#Finally do this with c
#function(1, 2, 3)

#Keyword Arguments
#def function_a(a, b, c):
	#Do this with a
	#Then do this with b
	#Finally do this with c
#function(c=1, a=2, b=3)