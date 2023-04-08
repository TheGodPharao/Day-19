from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Choose the Winning Teeeeertle",
                            prompt="Choose a color of the winning turtle(red,orange,blue,yellow, purple,green)")
colors = ["red", "orange", "yellow", "green", "blue", "purple" ]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range (0,6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.speed("normal")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -235, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"CONGRATS !!! You've won !! the {winning_color} turtle won")
            else:
                print(f"SORRY.. YOU LOST!!! the {winning_color} turtle won! "
                      f"your {user_bet} turle was not fast enough")


        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)


screen.exitonclick()