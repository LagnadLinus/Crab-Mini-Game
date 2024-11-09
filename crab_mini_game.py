


from turtle import *        # importing everything from turtle library 

# Register the crab image as a shape
addshape("crab.gif")        # Load the custom crab shape

speed(0)                    # adding speed 0 to make it bit faster


crab_travels = 20           # its the distance that crab moves when player press the keyboard which is 15px

bgcolor("#F4A460")          # Sandy Brown Color for the land

# Display Start Message
penup()
goto(0, 250)
color("black")
write("Help the crab reach the ocean!", align="center", font=("Arial", 16, "bold"))
goto(100, 200)              # Position for starting rectangle

# creating a sea as a rectangle using goto()
penup()                     # removing the initial line
goto(100, 200)              # starting from top right x-axis and y-axis 
pendown()                   # starting to draw rectangle now

color("#013A63")            # adding deep ocean blue color 
begin_fill()
goto(300, 200)              # another point
goto(300, -200)             # and another point 
goto(100, -200)             # another point 
goto(100, 200)              # last point 
end_fill()


# drawing the crab 
penup()                     # penup so that it doesnt create trails
goto(-200, 0)               # adding crab just behind the center of the screen 
shape("crab.gif")           # adding crab shape 

# Boundaries
LEFT_BOUNDARY = -300
RIGHT_BOUNDARY = 300
TOP_BOUNDARY = 300
BOTTOM_BOUNDARY = -300

# Creating logic for Crab Movement with boundaries
def travel_up():
    if ycor() + crab_travels <= TOP_BOUNDARY:
        setheading(90)          # rotating with 90 degree 
        forward(crab_travels)   #going forward by 15 px
        game_objective()        # checking if crossed the line inside or not

def travel_down():
    if ycor() - crab_travels >= BOTTOM_BOUNDARY:
        setheading(270)         # rotating with 270 degree 
        forward(crab_travels)   #going forward by 15 px
        game_objective()

def travel_left():
    if xcor() - crab_travels >= LEFT_BOUNDARY:
        setheading(180)         # rotating with 0 degree 
        forward(crab_travels)  #going forward by 15 px
        game_objective()

def travel_right():
    if xcor() + crab_travels <= RIGHT_BOUNDARY:
        setheading(0)           # rotating with 180 degree 
        forward(crab_travels)   #going forward by 15 px
        game_objective()


# Creating function to check the game objectives met or not 
# we are going to compare if the position is not greater than sea(rectangle) position i.e. 100 
def game_objective():
    if xcor() > 100:        # xcor is a turtle function thats gives x position
        hideturtle()        # it hides the turtle tip when the condition is true
        color("blue")      # making color white 
        write("Player Won") # game goal 

        # Adding these so that the player Won message won't get displayed after the crab reach sea
        onkey(None, "Up")   # We put None because there is no callback function so no player worn message. 
        onkey(None, "Down")
        onkey(None, "Left") 
        onkey(None, "Right")


# linking with key listen events 
onkey(travel_up, "Up")     # setting up Up key with call back function
onkey(travel_down, "Down") # setting Down Key
onkey(travel_left, "Left") # setting Right Key
onkey(travel_right, "Right")# setting Left key


listen()                   # Listening for key strokes


done()
 