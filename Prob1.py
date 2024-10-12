############################################################
# Name: Lola Cordero
# Name(s) of anyone worked with:
# Est time spent (hr): 1-2
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    
    #background
    bg=GRect(0,0,WIDTH,HEIGHT)
    bg.set_filled(True)
    bg.set_fill_color("orange")
    gw.add(bg)

    #the base of the robot's head
    head= GRect(150,200, 300, 300 )
    head.set_filled(True)
    head.set_fill_color("gray")
    gw.add(head)

    #left eye
    lEye= GOval(187.5,275,75,75)
    lEye.set_filled(True)
    lEye.set_fill_color("blue")
    gw.add(lEye)

    #right eye
    rEye= GOval(337.5,275,75,75)
    rEye.set_filled(True)
    rEye.set_fill_color("blue")
    gw.add(rEye)

    #left pupil
    lPupil = GOval(200,287.5,50,50)
    lPupil.set_filled(True)
    lPupil.set_fill_color("white")
    gw.add(lPupil)

    #right pupil
    rPupil = GOval(350,287.5,50,50)
    rPupil.set_filled(True)
    rPupil.set_fill_color("white")
    gw.add(rPupil)

    #base of mouth
    mouth = GOval(225,410,150,30)
    mouth.set_filled(True)
    mouth.set_fill_color("white")
    gw.add(mouth)

    #teeth (lines)
    midTooth= GLine(300, 410, 300, 440)
    midTooth.set_line_width(5)
    gw.add(midTooth)

    leftTooth= GLine(262.5, 410, 262.5, 440)
    leftTooth.set_line_width(5)
    gw.add(leftTooth)

    rightTooth= GLine(337.5,410,337.5,440 )
    rightTooth.set_line_width(5)
    gw.add(rightTooth)

    #leftEar
    leftEar=GRect(120, 300, 30, 100)
    leftEar.set_filled(True)
    leftEar.set_fill_color("red")
    gw.add(leftEar)

    #rightEar
    rightEar=GRect(450, 300, 30, 100)
    rightEar.set_filled(True)
    rightEar.set_fill_color("red")
    gw.add(rightEar)

    #antenna stick
    stick= GLine(300, 175, 300, 200)
    stick.set_line_width(3)
    gw.add(stick)

    #top of antenna
    top= GOval (275, 125, 50, 50)
    top.set_filled(True)
    top.set_fill_color("yellow")
    gw.add(top)

    #text
    gw.add(GLabel("'Beep Boop, Hello There Human!'", 30, 50))


if __name__ == '__main__':
    draw_image()
