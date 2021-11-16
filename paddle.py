import requests
import turtle
import os
from playsound import playsound
# if __name__ == "__main__":
    #payload = {"first": "Kylie", "last":"Scharf"}
    #r = requests.get("https://httpbin.org/get", params=payload)
    #print(r.text)


wn = turtle.Screen()
wn.title("Pong Edit By Kylie Scharf")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation that sets speed to max possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #by default the size is 20 by 20 so if you stretch it by 5 you do 20 times 5 which is 100 by 20 times 1 which is still 20
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of animation that sets speed to max possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #by default the size is 20 by 20 so if you stretch it by 5 you do 20 times 5 which is 100 by 20 times 1 which is still 20
paddle_b.penup()
paddle_b.goto(+350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # speed of animation that sets speed to max possible speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2 # dx is change in x so every time the ball moves it moves by 2 pixels and both x and y are positibe rn so it moes right and up
ball.dy = 2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  PlayerB: 0", align="center", font=("Courier", 24, "normal")) # sets default score

# function
def paddle_a_up():
    y = paddle_a.ycor() # paddle a is the name of the object and the .ycor method is from the turtle module and returns the y coordinate
    y += 20
    paddle_a.sety(y)
    # having a function does not actually do anyhting until we call the function so we just defined a function but are not using it yet

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() # tells the program to listen for keyboard input
wn.onkeypress(paddle_a_up, "w") # says when the user presses lowercase w to call the paddle up function
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(paddle_b_down, "k")



# Main Game Loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    y = ball.ycor()
    x = ball.xcor()
    # border checking
    if y > 290:
        ball.sety(290)
        ball.dy *= -1
    if y < -290:
        ball.sety(-290)
        ball.dy *= -1
    if x > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1 # player a scored
        pen.clear()
        pen.write("Player A: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) # uses format method to add new things into the brackets when changed
    if x < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 # player b scored
        pen.clear() # clears whats on the screen first
        pen.write("Player A: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    # paddle and ball collisions
    if (x > 340 and x < 350) and y < paddle_b.ycor() + 50 and y > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    if (x < -340 and x > -350) and y < paddle_a.ycor() + 50 and y > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1