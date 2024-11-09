from turtle import *

# Setup
speed(5)
bgcolor("#87CEEB")  # light blue background to represent the ocean
penup()

# Draw the crab's body
goto(0, -50)
color("red")
begin_fill()
circle(50)  # Main body
end_fill()

# Draw the left claw
goto(-70, 20)
begin_fill()
circle(30)
end_fill()

# Draw the right claw
goto(70, 20)
begin_fill()
circle(30)
end_fill()

# Draw the left arm connecting to the left claw
goto(-30, -10)
pendown()
width(5)
goto(-70, 20)
penup()

# Draw the right arm connecting to the right claw
goto(30, -10)
pendown()
goto(70, 20)
penup()

# Draw the left eye
goto(-20, 20)
color("white")
begin_fill()
circle(10)
end_fill()

# Draw the right eye
goto(20, 20)
begin_fill()
circle(10)
end_fill()

# Draw the pupils
goto(-20, 25)
color("black")
begin_fill()
circle(5)
end_fill()

goto(20, 25)
begin_fill()
circle(5)
end_fill()

# Draw legs on the left side
for i in range(-40, -60, -10):
    goto(i, -30)
    pendown()
    goto(i - 20, -50)
    penup()

# Draw legs on the right side
for i in range(40, 60, 10):
    goto(i, -30)
    pendown()
    goto(i + 20, -50)
    penup()

hideturtle()
done()
