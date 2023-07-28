#pong_game
#to learn coding

import turtle #built-in module for basic graphics

#creating a window
wn = turtle.Screen()
wn.title("Pong by Aarushi B.")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #makes the game speed up a bit, not stay too slow

# Paddle A
paddle_a = turtle.Turtle() 
paddle_a.speed(0) #sets the speed to the max possible speed, just graphically not actually
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)



# Paddle B



# Ball



#main game loop
while True:
    wn.update() #everytime the loop runs, it updates the screen
