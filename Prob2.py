########################################
# Name: Lola Cordero
# Collaborators: 
# Estimated time spent (hrs): 2-3
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 70
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 7

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    CENTERW= WIDTH*.5
    CENTERH= HEIGHT*.5
    gw = GWindow(WIDTH, HEIGHT)

    def n_bricks(width, height, base): #height is brick height, width is brick width, and base is the number of bricks in base
        startingX=CENTERW -(width*.5) #this gives us the X coordinate of the very first brick in row one
        startingY=(CENTERH - ((height * base)*.5)) #this gives us the Y coordinate of the very first brick in row one
        #the following loop will repeat for however many rows are needed to get the given number of bricks for the base (since it's the same 
        #number as the height)
        for i in range(base):
            X= startingX - (width*0.5*(i)) #This will determine the X coordinate of the first brick in each row
            Y= startingY + (height*i) #This will determine the Y coordinate we will be using for every brick in a singular row
        #the following loop will be how we determine how many bricks are in each row (row number represented as i + 1, since i starts at 0), 
        # as well as determine the coordinate of each brick's top left corner
            for j in range (i+1): 
                brick=GRect(X,Y, width, height) #this is our brick's dimensions and coordinate
                gw.add(brick) #adds brick to the window
                print("Coordinates:", X, ",",  Y) #This is just something I added for myself to check and make sure there are no mistakes
                X= X + width #This will adjust the X coordinate, so we don't have a ton of bricks overlapping (this is how we print the other
                # bricks in the row)

    n_bricks(BRICK_WIDTH, BRICK_HEIGHT, BRICKS_IN_BASE)

if __name__ == '__main__':
    draw_pyramid()
