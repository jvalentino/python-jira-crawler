from chart_constants import ChartConstants

import turtle
from PIL import Image

class DrawingService:
    def __init__(self):
        pass

    def draw(self, chart_settings):
        # FIXME: need to generate the height and width
        width = 1500
        height = 1000
        
        # Set up the turtle screen
        screen = turtle.Screen()
        screen.setup(width=width, height=height)
        screen.bgcolor("white")
        
        # Starting position
        margin_x = (width // 10)
        start_x = -width // 2 + margin_x
        start_y = height // 2 - 50

        self.draw_background(chart_settings, width, height, start_x, start_y)

        # Save the drawing to a PNG file
        canvas = screen.getcanvas()
        canvas.postscript(file="target/chart.eps")

        # Convert EPS to PNG using Pillow
        img = Image.open("target/chart.eps")
        img.save("target/chart.png")

        # Clean up
        turtle.bye()
        
    def draw_background(self, chart_settings, width, height, start_x, start_y):
        pen = turtle.Turtle()
        pen.speed(0)
    
        for i in range(chart_settings.column_max + 1):
            # Move to the starting position of the line
            pen.penup()
            pen.goto(start_x + i * 100, start_y)
            
            # Write the index
            pen.write(str(i), align="center", font=("Arial", 12, "normal"))
            print(f"Drawing line {i} at {start_x + i * 100}, {start_y}")
            
            # Move down to start drawing the line
            pen.right(90)
            pen.forward(20)
            pen.pendown()
            
            # Draw the line
            pen.forward(height - 100)
            
            # Reset the pen position and orientation
            pen.penup()
            pen.goto(start_x + i * 100, start_y)
            pen.left(90)
        
        # Hide the turtle and display the window
        pen.hideturtle()








        