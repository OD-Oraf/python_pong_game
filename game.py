import turtle # library for games

win = turtle.Screen() # create window 
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height = 600)
win.tracer(0)

#paddle A
paddle_a = turtle.Turtle()


#paddle B 
paddle_b= turtle.Turtle()

# Ball 

# main game loop 
while True: 
    win.update()