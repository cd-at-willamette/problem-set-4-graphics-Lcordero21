########################################
# Name: Lola Cordero
# Collaborators: QUAD Center
# Estimate time spent (hrs): 4-5
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score
score=0  

def clicky_box():


    def get_r(value):
        return random.randint(0, value)
    # This is how we get our random value for x and y (so our square will go to a random coordinate)


    box= GRect((GW_WIDTH*0.5)-(SQUARE_SIZE*0.5),(GW_HEIGHT*0.5)-(SQUARE_SIZE*0.5),SQUARE_SIZE, SQUARE_SIZE)
    box.set_color("red")
    box.set_filled(True) 
    #This is our starter square size and coordinates 

    def on_mouse_down(event):
        x= get_r(GW_WIDTH-SQUARE_SIZE) #gives us a random x
        y= get_r(GW_HEIGHT-SQUARE_SIZE) #gives us a random y
        xMouse= event.get_x() #gives us the x coordinate of the mouse's click
        yMouse= event.get_y() #gives us the y coordinate of the mouse's click
        print("Coordinates of mouse: (", xMouse, ",", yMouse, ")" ) #this is just for me to debug and stuff
        if (xMouse>=box.get_x()) and (xMouse<=box.get_x() + SQUARE_SIZE): #These two lines check to see if the mouse click is within the 
            if (yMouse>=box.get_y()) and (yMouse <= box.get_y() +SQUARE_SIZE): #square dimesnions.
                box.set_location(x,y) #sets box in new location
                gw.score = gw.score + 1 #updates score variable
                gw.counter.set_label(str(gw.score)) # update score label
        else:
            box.set_location((GW_WIDTH*0.5)-(SQUARE_SIZE*0.5),(GW_HEIGHT*0.5)-(SQUARE_SIZE*0.5)) #if click is outside square dimensions, it resets to middle
            gw.score = 0 #score resets to 0
            gw.counter.set_label(str(gw.score)) #updates score label
        print (gw.score) #this is also for me to debug and stuff :)

    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    gw.score=0
    gw.add_event_listener("click", on_mouse_down)
    gw.counter= GLabel(str(gw.score), SCORE_DX, GW_HEIGHT-SCORE_DY)
    gw.counter.set_font(SCORE_FONT) #sets font of score label

    #the above variables are just gw variables I made to use anywhere in the program

    gw.add(box) 
    gw.add(gw.counter)

    #the above two variables are how we get our starting screen


if __name__ == '__main__':
    clicky_box()
