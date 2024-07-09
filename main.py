import random
import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light pink")
turtle_screen.title("CatchTheTurtle")
FONT = ('Arial', 30, 'normal')
score = 0
time = 21
game_over = False
turtle_list = []

score_turtle = turtle.Turtle()
time_turtle = turtle.Turtle()


def setup_time_turtle():
    time_turtle.hideturtle()
    time_turtle.color("black")
    time_turtle.penup()
    time_turtle.setposition(0, 230)
    time_turtle.write(arg="Time: 20", move=False, align="center", font=FONT)


def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("yellow")
    score_turtle.penup()

    top_height = turtle_screen.window_height() / 2
    y = top_height * 0.95
    score_turtle.setposition(0, y)
    score_turtle.write(arg='Score: 0', move=False, align='center', font=FONT)


def make_turtle(x, y):
    t = turtle.Turtle()
    def handle_click(x, y):
         global score
         score+=1
         score_turtle.clear()
         score_turtle.write(arg='Score: {}'.format(score), move=False, align='center', font=FONT)


    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.color("dark green")
    t.shapesize(2, 2)
    t.goto(x*15,y*15)
    turtle_list.append(t)

x_list = [-20,-10,0,10,20]
y_list = [-20,-10,0,10]

def setup_turtles():
  for x in x_list:
    for y in y_list:
        make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles():
    if not game_over:
     hide_turtles()
     random.choice(turtle_list).showturtle()
     turtle.ontimer(show_turtles,750)

def countdown():
    global game_over

    global time
    if time > 0:
     time-=1
     time_turtle.clear()
     time_turtle.write(arg='Time: {}'.format(time), move=False, align='center', font=FONT)
     turtle.ontimer(countdown,1000 )
    else:
     game_over = True
     time_turtle.clear()
     hide_turtles()
     time_turtle.write(arg='GAME OVER!', move=False, align='center', font=FONT)


turtle.tracer(0)
setup_time_turtle()
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles()
countdown()
turtle.tracer(1)


turtle.mainloop()