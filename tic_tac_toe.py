''' https://www.youtube.com/watch?v=8eHpXLDhi6w&ab_channel=JuniLearningUser video used to help create the project.
User will play against the computer and will always play X while the computer takes O. The code will check if anyone has
 gotten 3 in a row. Also needs to check that no two X's or O's share the same spot'''

import turtle # turtle is a pre-installed Python library that enables users to create pictures and shapes by providing a virtual canvas
import math # allows us to use math.pi to draw circles for our playing pieces

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

# This function activates all the event listeners
def activate(functions): # Assigns all the functions in the list to different numerical keys
    for i in range(9):
        screen.onkey(functions[i], str(i + 1)) # This assigns the i'th function in the list to the i + 1 key

# This function activates all the event listeners
def deactivate():
    for i in range(9):
        screen.onkey(None, str()) # Assigns all the numerical keys to no functions

# This function will try to add an x to the inputted location 
def addX(row, column):
    # Clear announcer everytime they try to add an "x"
    announcer.clear()
    # Before everything else, check if the space they want to add to is full
    if board[row][column] == "x" or board[row][column] == "o":
        # Tell them they cannot take that spot 
        announcer.write("That spot is taken!", font = ("Arial", 36))
        screen.update()
    else:
        # Draw an x in the correct spot
        drawX(-200 + 200 * column, 200 - 200 * row) # Call drawX() function

        # Add an x to the computer's board
        board[row][column] = "x"

# Define functions for the event listeneres
def squareOne():
    addX(0, 0)
def squareTwo():
    addX(0, 1)
def squareThree():
    addX(0, 2)
def squareFour():
    addX(1, 0)
def squareFive():
    addX(1, 1)
def squareSix():
    addX(1, 2)
def squareSeven():
    addX(2, 0)
def squareEight():
    addX(2, 1)
def squareNine():
    addX(2, 2)

# Create a list of event listener functions 
functions = [squareOne, squareTwo, squareThree, squareFour, squareFive, squareSix, squareSeven, squareEight, squareNine]

# Create turtle
drawer = turtle.Turtle() 
# Will write messages to the user
announcer = turtle.Turtle()

drawer.pensize(10) # Increase pen size
drawer.ht() # Hide turtle using the ht() -> hideturtle() function

announcer.penup()
announcer.ht()
announcer.goto(-200, 0)
announcer.color("red")

# Create screen
screen = turtle.Screen() 
screen.tracer(0) # .tracer(0) is how to turn the animations off

# Draw the board
drawBoard() 

# Create the board
board = []
for i in range(3): # each row is its own list 
    row = []
    for j in range(3):  
        row.append(" ") # Adds three empty spaces to row
    board.append(row) # This will make a grid filled with spaces, computer will read spaces as empty slots

# Call your activate function, activates the event listeners
activate(functions)
screen.listen()

screen.exitonclick() # Included to fix this bug where the screen flashes and closes on VSCode