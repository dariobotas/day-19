"""Understanding the Turtle Coordinate System"""
from turtle import Turtle, Screen  

"""mike = Turtle(shape="turtle")
leo = Turtle(shape="turtle")
don = Turtle(shape="turtle")
raph = Turtle(shape="turtle")
tim= Turtle(shape="turtle")
tom= Turtle(shape="turtle")"""

screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red","blue","orange","purple","green","yellow"]
y_positions = [150, 90, 30, -30, -90, -150]

for turtle_index in range(0, 6):
  tim = Turtle(shape="turtle")
  tim.color(colors[turtle_index])
  tim.penup()
  tim.goto(x=-240, y=y_positions[turtle_index])

"""def set_turtle_inicial_position(turtle, x, y, color):
  turtle.color(color)
  turtle.penup()
  turtle.goto(x, y)


set_turtle_inicial_position(mike, -240, 150,"orange")
set_turtle_inicial_position(leo, -240, 90,"blue")
set_turtle_inicial_position(don, -240, 30,"purple")
set_turtle_inicial_position(raph, -240, -30,"red")
set_turtle_inicial_position(tim, -240, -90,"green")
set_turtle_inicial_position(tom, -240, -150,"yellow")"""

screen.listen()
screen.exitonclick()