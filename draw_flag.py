from graphics import Canvas
import random

""" I am creating a Ugandan National Flag"""

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # Draw the stripes 
    canvas.create_rectangle(0, 50, 450, 0, "black")
    canvas.create_rectangle(0, 100, 450, 50, "yellow")
    canvas.create_rectangle(0, 150, 450, 100, "red")
    canvas.create_rectangle(0, 200, 450, 150, "black")
    canvas.create_rectangle(0, 250, 450, 200, "yellow")
    canvas.create_rectangle(0, 300, 450, 250, "red")

    # Draw the white oval in the middle
    canvas.create_oval (185, 102, 265, 198, "white")

    # Add a crasted crane image 
    canvas.create_image(195, 115, "https://i.postimg.cc/v8Nx2c8c/uganda-government-crested-crane-logo-png-seeklogo-556491.png")

    print("The Ugandan National Flag!")
    

if __name__ == '__main__':
    main()
