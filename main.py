from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
color=screen.textinput(title='make your bet',prompt='which turtle will win the race?enter the color:')

list_color=['red','green','pink','yellow','blue','orange']
y_pos=[-150,-100,-50,0,50,100]
all_turtle=[]


for i in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(list_color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtle.append(new_turtle)

is_on=True

while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_on = False
            if turtle.pencolor()==color:
                print(f"you won!{turtle.pencolor()} turtle is the winner")
            else:
                print(f"you lose!{turtle.pencolor()} turtle is the winner")
        n=random.randint(0,10)
        turtle.forward(n)
















screen.exitonclick()