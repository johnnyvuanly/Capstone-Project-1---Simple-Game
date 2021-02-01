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

# This function will check if the onputted player has won
def checkWon(letter):
    # Check if there are three in a row horizontally 
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == letter:
            return True
    
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == letter:
            return True

    # Check if there are three in a row diagonally down
    if board[0][0] ==  board[1][1] and board[1][1] == board[2][2] and board[0][0] == letter:
        return True

    # Check if there are three in a row diagonally up 
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == letter:
        return True

    # If at this point, the given letter has not won 
    return False

# This function checks if the game is a tie 
def checkDraw():
    # Count the number of x's on the board
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "x": # If the space we are looking at is an x then increase count by 1
                coount += 1

    if count > 3:
        return True
    else:
        return False

# This function will add an o to the board in the best place
def addO():
    # Check if any places would result in a win for o
    for i in range(3):
        for j in range(3): # Using nested for loops we look a the whole board and checking to see if the space the computer wants is blank
            if board[i][j] == " ": # If the space is empty
                board[i][j] = "o" # then add an o
                if checkWon("o"):
                    drawO(-200 + 200 * j, 200 - 200 * i)
                    return # Leave the function with this return
                board[i][j] = " " # If "o" doesn't win in this spot then change it back to empty

    # Check if there is any place that o should block x
    for i in range(3):
        for j in range(3): # Nested for loops to look at each spot on the board again
            if board[i][j] == " ":
                board[i][j] = "x"
                if checkWon("x"):
                    board[i][j] = "o"
                    drawO(-200 + 200 * j, 200 - 200 * i)
                    return
                board[i][j] = " "

    # Try to place an o in one of the corners
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            if board[i][j] == " ":
                board[i][j] = "o"
                drawO(-200 + 200 * j, 200 - 200 * i)
                return
    
    # Place an o in any open spot
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "o"
                drawO(-200 + 200 * j, 200 -200 * i)
                return


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

        # Check if that new x made x win
        if checkWon("x"):
            announcer.goto(-97, 0) # Have announcer move a bit and then write a message
            announcer.write("You Won!", font = ("Arial", 36))

            # Update the screen and deactivate the event listeners
            screen.update()
            deactivate()
        else:
            # If they didn't win, then an o gets added to the board
            addO()

            # Check if that new o made o win
            if checkWon("o"):
                # Tell the player that they lost
                announcer.goto(-90, 0)
                announcer.write("You lost!", font = ("Arial", 36))

                # Update the screen and deactivate the evvent listeners
                screen.update()
                deactivate()
            # Check if there is a tie
            elif checkDraw():
                # Tell the player they tied with the computer
                announcer.goto(-90, 0)
                announcer.write("It's a tie!", font = ("Arial", 36))

                # Update the screen and deactivate the event listeners
                screen.update()
                deactivate()

# Define functions for the event listeners
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