#(c) Alexander Peat, 2024
#All rights reserved

from turtle import *
import random

listen()

screen = Screen()
screen.bgcolor('black')
screen.title("Peat's Pong Player (PPP)")
screen.setup(800, 800)
screen.tracer(False)

ball = Turtle()
ball.color('white')
ball.penup()
ball.shape('circle')
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.goto(0, 0)
random_heading = 0
random_heading = random.randint(-45, 45)
ball.setheading(random_heading)
screen.update()

paddle_1 = Turtle()
paddle_1.color('white')
paddle_1.penup()
paddle_1.shape('square')
paddle_1.shapesize(stretch_wid=1, stretch_len=5)
paddle_1.setheading(90)
paddle_1.goto(380, 0)
screen.update()

paddle_2 = paddle_1.clone()
paddle_2.goto(-380, 0)
screen.update()

pad1_score_display = Turtle()
pad1_score_display.color('white')
pad1_score_display.penup()
pad1_score_display.goto(200, 200)
pad1_score_display.hideturtle()
screen.update()

pad2_score_display = pad1_score_display.clone()
pad2_score_display.goto(-200, 200)
screen.update()

winner = Turtle()
winner.color('white')
winner.penup()
winner.goto(0, 50)
winner.hideturtle()

def pad1up():
    paddle_1.forward(20)
    screen.update()
    
def pad1down():
    paddle_1.backward(20)
    screen.update()
    
def pad2up():
    paddle_2.forward(20)
    screen.update()
    
def pad2down():
    paddle_2.backward(20)
    screen.update()
    
onkey(pad1up, 'Up')
onkey(pad1down, 'Down')
onkey(pad2up, 'w')
onkey(pad2down, 's')

go_forward = True
pad1_score = 0
pad1_score_display.write("0", align = 'center', font = ('Arial Black', 16, 'normal'))
pad2_score = 0
pad2_score_display.write("0", align = 'center', font = ('Arial Black', 16, 'normal'))

while True:
    screen.update()
    
    yball = int(ball.ycor())   
    xball = int(ball.xcor())
    
    ypaddle_1 = paddle_1.ycor()
    ypaddle_2 = paddle_2.ycor()
    
    if go_forward == True:
        ball.forward(0.3)
        screen.update()
    elif go_forward == False:
        ball.backward(0.3)
        screen.update()
    
    if xball == 380:
        if yball <= (ypaddle_1 + 45) and yball >= (ypaddle_1 - 45):
            go_forward = False
            
            inverted_heading = 0
            ball_heading = ball.heading()
            absolute_heading_value = abs(ball_heading)
            if ball_heading < 0:
                inverted_heading = ball_heading + (absolute_heading_value * 2)
            elif ball_heading > 0:
                inverted_heading = ball_heading - (absolute_heading_value * 2)
                
            ball.setheading(inverted_heading)
            screen.update()
    elif xball == -380:
        if yball <= (ypaddle_2 + 45) and yball >= (ypaddle_2 - 45):
            go_forward = True
            
            inverted_heading = 0
            ball_heading = ball.heading()
            absolute_heading_value = abs(ball_heading)
            if ball_heading < 0:
                inverted_heading = ball_heading + (absolute_heading_value * 2)
            elif ball_heading > 0:
                inverted_heading = ball_heading - (absolute_heading_value * 2)
            
            ball.setheading(inverted_heading) 
            screen.update()
            
    if yball >= 400 or yball <= -400:
        inverted_heading = 0
        ball_heading = ball.heading()
        absolute_heading_value = abs(ball_heading)
        if ball_heading < 0:
            inverted_heading = ball_heading + (absolute_heading_value * 2)
        elif ball_heading > 0:
            inverted_heading = ball_heading - (absolute_heading_value * 2)
        if yball >= 400:
            ball.setheading(270)
            ball.forward(3)
        elif yball <= -400:
            ball.setheading(90)
            ball.forward(3)
        ball.setheading(inverted_heading)
        screen.update()
            
    if xball >= 400:
        ball.goto(0, 0)
        pad2_score += 1
        pad2_score_display.clear()
        pad2_score_display.write(pad2_score, align = 'center', font = ('Arial Black', 16, 'normal'))
        screen.update()
    elif xball <= -400:
        ball.goto(0, 0)
        pad1_score += 1
        pad1_score_display.clear()
        pad1_score_display.write(pad1_score, align = 'center', font = ('Arial Black', 16, 'normal'))
        screen.update()
        
    if pad1_score >= 10:
        winner.write("Paddle 2 Wins!", align = 'center', font = ('Arial Black', 16, 'normal'))
        break
    elif pad2_score >= 10:
        winner.write("Paddle 1 Wins!", align = 'center', font = ('Arial Black', 16, 'normal'))
        break
        
screen.update()

done()
