"""Challgenge: Make an Etch-A-Sketch App"""
from turtle import Turtle, Screen

def set_turtle_inicial_position(turtle, x, y, shape, color):
  turtle.shape(shape)
  turtle.color(color)
  turtle.penup()
  turtle.setpos(x,y)
  turtle.pendown()
  

mike = Turtle()
leo = Turtle()
don = Turtle()
raph = Turtle()
screen = Screen()
screen.setup(width=500,height=400)

set_turtle_inicial_position(mike,-150,-100,"turtle","orange")
set_turtle_inicial_position(leo,-150,-50,"turtle","blue")
set_turtle_inicial_position(don,-150,0,"turtle","purple")
set_turtle_inicial_position(raph,-150,50,"turtle","red")


screen.listen()
screen.exitonclick()