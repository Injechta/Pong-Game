# Basic Pong with python2

import turtle
import os

wn = turtle.Screen()
wn.title("Pong for beginners, using python")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0



# ------------- Game Objects ------------------


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.150
ball.dy = 0.150

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))


# ------------------------/ Game Objects /-----------------------------------

# ------------------------------------------ Make The Objects Move --------------------------------------------

# ----------------------------------- Functions ------------------------------------------------------------------

# Paddle A Functions
def paddle_a_up(): # Define a function nammed paddle_a_up
    y = paddle_a.ycor() # Get The Y coordinates
    y += 20 # Add 20 To The Coordinates
    paddle_a.sety(y) # Set The Y To The New Y Coordinates

def paddle_a_down(): #Define a function nammed paddle_a_down
    y = paddle_a.ycor() # Get The Y coordinates
    y -= 20 # Take Off 20 To The Coordinates
    paddle_a.sety(y) # Set The Y To The New Y Coordinates

# -------------------- /End Paddle A Functions / ------------------------

# Paddle B Functions
def paddle_b_up(): #Define a function nammed paddle_b_up
    y = paddle_b.ycor() # Get The Y coordinates
    y += 20 # Add 20 To The Coordinates
    paddle_b.sety(y) # Set The Y To The New Y Coordinates

def paddle_b_down(): #Define a function nammed paddle_b_down
    y = paddle_b.ycor() # Get The Y coordinates
    y -= 20 # Take Off 20 To The Coordinates
    paddle_b.sety(y) # Set The Y To The New Y Coordinates

# ----------- / End Paddle B Functions / ------------------------- 

# ---------------------------------------- / End Functions /-----------------------------------------------------

# -------------------- Keyboard Binding ------------------------

# Paddle A Keyboard Binding
wn.listen() # Will Listen For Keyboard Input
wn.onkey(paddle_a_up, "z") # The paddle_a_up function is called when the z is press on keyboard
wn.onkey(paddle_a_down, "s") # The paddle_a_down function is called when the s is press on keyboard


# Paddle B Keyboard Binding
wn.listen() # Will Listen For Keyboard Input
wn.onkey(paddle_b_up, "p") # The paddle_b_up function is called when the p is press on keyboard
wn.onkey(paddle_b_down, "m") # The paddle_b_up function is called when the p is press on keyboard

#  ------------------------/  End Keyboard Binding / -------------------------------


# ------------/ Make The Objects Move /------------------

# Main Game Loop
while True:
    wn.update()

    # Move The Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking, top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    # Border Checking, bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    # Border Checking, right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))



    # Border Checking, left border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))



    # --------------------------- Paddle And Ball Collisions ---------------------------------------
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
    # ------------------------ / End Paddle And Ball Collisions /--------------------------------


    # ---------------------------------------- Scoring -------------------------------------------------------




