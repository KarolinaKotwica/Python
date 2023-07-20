from turtle import *
import random

is_race_on = False
screen = Screen()
screen.bgcolor("grey")
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bed', prompt='Choose color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [ -70, -40, -10, 20, 50, 80 ]
all_turtles = []


for i in range(0,6):
    newTurtle = Turtle(shape='turtle')
    newTurtle.color(colors[i])
    newTurtle.penup()
    newTurtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(newTurtle)
  
if user_bet:
    is_race_on = True
      
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You have won! The winning color is {winning_color}')
            else:
                print(f"{winning_color} won!")
        number = random.randint(0,10)
        turtle.forward(number)

screen.exitonclick()