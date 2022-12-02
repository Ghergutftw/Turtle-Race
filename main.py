from turtle import *
from random import *

all_turtles = []

with open('art.txt', 'r') as f:
    for line in f:
        print(line.rstrip())


def generate_turtle(x_cord, y_cord, colour) :
    new_turtle = Turtle ( "turtle" )
    new_turtle.penup ()
    new_turtle.goto ( x=x_cord, y=y_cord )
    new_turtle.color ( colour )
    all_turtles.append ( new_turtle )


is_race_on = False

screen = Screen ()
screen.title("Turtle race")
ls


screen.setup ( width=500, height=400 )
user_color = screen.textinput ( title="Make your bet", prompt="Which Turtle will win the race ? Enter a color : " )
user_color = user_color.lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_axis = -100
for i in range ( len ( colors ) ) :
    generate_turtle ( -230, y_axis, colors[i] )
    y_axis = y_axis + 40

if user_color :
    is_race_on = True

while is_race_on :
    for turtle in all_turtles :
        if turtle.xcor () > 230 :
            is_race_on = False
            winning_color = turtle.pencolor ()
            if winning_color == user_color :
                print ( "You won!" )
                print ( winning_color )
            else :
                print ( "You lost!" )
                print ( "The winning color is : " + winning_color )

        random_distance = randint ( 0, 10 )
        turtle.forward ( random_distance )

screen.exitonclick ()
