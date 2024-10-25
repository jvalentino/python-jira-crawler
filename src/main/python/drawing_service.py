from chart_constants import ChartConstants

import turtle
from PIL import Image

class DrawingService:
    def __init__(self):
        pass

    def draw(self, chart_settings):
        # FIXME: need to generate the height and width
        constants = ChartConstants(1500, 1000)
        
        # Set up the turtle screen
        screen = turtle.Screen()
        screen.setup(width=constants.width, height=constants.height)
        screen.bgcolor("white")

        self.draw_background(chart_settings, constants)

        # Save the drawing to a PNG file
        canvas = screen.getcanvas()
        canvas.postscript(file="target/chart.eps")

        # Convert EPS to PNG using Pillow
        img = Image.open("target/chart.eps")
        img.save("target/chart.png")

        # Clean up
        turtle.bye()
        
    def draw_background(self, chart_settings, constants):
        pen = turtle.Turtle()
        pen.speed(0)
        
        date_list = list(chart_settings.date_to_column.keys())
        
        for i in range(chart_settings.column_max + 1):
            # Move to the starting position of the line
            pen.penup()
            pen.goto(constants.start_x + i * constants.WEEK_WIDTH_PX, constants.start_y)
            
            # Write the index
            pen.write(str(i), align="center", font=("Arial", 12, "normal"))
            
            # Move down to write Date
            pen.right(90)
            pen.forward(20)
            pen.write(date_list[i], align="center", font=("Arial", 12, "bold"))
            
            # Move down to start drawing the line
            pen.forward(20)
            pen.pendown()
            
            # Draw the line
            pen.forward(constants.height - constants.margin_y)
            
            # Reset the pen position and orientation
            pen.penup()
            pen.goto(constants.start_x + i * constants.WEEK_WIDTH_PX, constants.start_y)
            pen.left(90)
        
        # Hide the turtle and display the window
        pen.hideturtle()








        