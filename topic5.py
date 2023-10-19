from turtle import Turtle, Screen  
import random

"""Aaaand, we’re off to the races!"""

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(
  title="Make your bet: ",
                            prompt="Which turtle will win the race? Enter a color (red, blue, orange, purple, green, yellow): ")
colors = ["red","blue","orange","purple","green","yellow"]
y_positions = [150, 90, 30, -30, -90, -150]
all_trutles = []

for turtle_index in range(len(colors)):
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(colors[turtle_index])
  new_turtle.penup()
  new_turtle.goto(x=-240, y=y_positions[turtle_index])
  all_trutles.append(new_turtle)

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_trutles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"The {winning_color} turtle won! You're the winner!")
      else:
        print(f"The winner is the {winning_color} turtle! You lose!")
    
    random_distance = random.randint(0, 10)
    turtle.forward(random_distance)
  


screen.exitonclick()