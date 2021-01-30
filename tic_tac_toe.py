''' https://www.youtube.com/watch?v=8eHpXLDhi6w&ab_channel=JuniLearningUser video used to help create the project.
will play against the computer and will always play X while the computer takes O. The code will check if anyone has
 gotten 3 in a row. Also needs to check that no two X's or O's share the same spot'''

import turtle # turtle is a pre-installed Python library that enables users to create pictures and shapes by providing a virtual canvas
import math # allows us to use math.pi to draw circles for our pieces

# This function draws the grid the game will be played on 
def drawBoard(): 
    # Draw the horizontal lines, drawer draws the lines starting from different heights
    for i in range(2): # i counts how many times we repeated the loop
        drawer.penup() # drawer picks pen up
        drawer.goto(-300, 100 - 200 * i) # go to specific spot
        drawer.pendown() # drawer puts pen down
        drawer.forward(600) # move forward 600 pixels

    drawer.right(90) # turn drawer 90 degress

    # Draw both of the vertical lines
    for i in range(2):
        drawer.penup()
        drawer.goto(-100 + 200 * i, 300) # This time x coordinates change due to i, y stays the same
        drawer.pendown()
        drawer.forward(600)

    # Add numbers to the top corner of each square
    num = 1
    for i in range(3): # repeat 3 times
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j * 200, 280 - i * 200) # x coord depends on j and y coord depends on i
            drawer.pendown()

            drawer.write(num, font = ("Arial", 12)) # drawer then can write the value of what num is on each of the boxes
            num += 1 # makes num 1 more then it was before

    # Update the screen with new changes
    screen.update() 

# This function draws an "x" centered at the inputted coordinates
def drawX(x, y):
    # Move to the correct spot
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

    drawer.setheading(60)

    # Draw the lines of the x
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)
    
    # Update the screen
    screen.update()

# This function draws an "o" centered at the inputted coordinates
def drawO(x, y):
    # Move to the correct spot
    drawer.penup()
    drawer.goto(x, y + 75) # so that it goes with the center of the "o"
    drawer.pendown()

    drawer.setheading(0) # Get drawer to face in the right direction

    # Draw a circle with the correct size
    for i in range(180):
        drawer.forward((150 * math.pi)/180) # Go forward a bit then...
        drawer.right(2) # turn two degress to the right 
    
    # Update the screen
    screen.update()

# Create turtle
drawer = turtle.Turtle() 

# This function will try to add an x to the inputted location 
def addX(row, column):
    # Draw an x in the correct spot
    drawX() # Call drawX() function

drawer.pensize(10) # Increase pen size
drawer.ht() # Hide turtle using the ht() -> hideturtle() function
 
screen = turtle.Screen() # Create screen
screen.tracer(0) # .tracer(0) is how to turn the animations off

drawBoard() # draw the board

drawO(0, 0)

screen.exitonclick() # Included to fix this bug where the screen flashes and closes on VSCode