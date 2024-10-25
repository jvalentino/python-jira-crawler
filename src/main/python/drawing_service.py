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
        
        self.draw_grouping(chart_settings, constants, chart_settings.epic_groupings[2])

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

    def draw_grouping(self, chart_settings, constants, epic_grouping):
        pen = turtle.Turtle()
        pen.speed(0)
        
        # Define padding
        top_padding = 10
        bottom_padding = 20  # Increased bottom padding
        
        # Draw the light blue box around the entire area
        pen.color("black", "lightblue")  # Set the outline color to black and fill color to light blue
        pen.penup()
        pen.goto(
            constants.start_x + epic_grouping.column_min * constants.WEEK_WIDTH_PX, 
            constants.start_y - constants.margin_y + top_padding)
        
        pen.begin_fill()
        
        # Draw the light blue rectangle
        pen.pendown()
        pen.forward((epic_grouping.column_max - epic_grouping.column_min + 1) * constants.WEEK_WIDTH_PX)  # Top side
        pen.right(90)
        pen.forward((epic_grouping.row_max + 1) * 40 + top_padding + bottom_padding)  # Right side
        pen.right(90)
        pen.forward((epic_grouping.column_max - epic_grouping.column_min + 1) * constants.WEEK_WIDTH_PX)  # Bottom side
        pen.right(90)
        pen.forward((epic_grouping.row_max + 1) * 40 + top_padding + bottom_padding)  # Left side
        pen.right(90)
        
        pen.end_fill()
        
        # Draw each epic setting rectangle
        pen.color("black", "#CCCCCC")  # Set the outline color to black and fill color to #CCCCCC
        
        for epic_setting in epic_grouping.epic_settings:
            # Calculate the vertical position with additional 10px space between rectangles
            vertical_position = constants.start_y - (epic_setting.row * 40) - constants.margin_y
            
            # Move to the starting position of the rectangle
            pen.penup()
            pen.goto(
                constants.start_x + epic_setting.column_start * constants.WEEK_WIDTH_PX, 
                vertical_position)
            
            # Start filling the rectangle
            pen.begin_fill()
            
            # Draw the rectangle
            pen.pendown()
            pen.forward((epic_setting.column_end - epic_setting.column_start + 1) * constants.WEEK_WIDTH_PX)  # Top side
            pen.right(90)
            pen.forward(30)  # Right side
            pen.right(90)
            pen.forward((epic_setting.column_end - epic_setting.column_start + 1) * constants.WEEK_WIDTH_PX)  # Bottom side
            pen.right(90)
            pen.forward(30)  # Left side
            pen.right(90)
            
            # End filling the rectangle
            pen.end_fill()
            
            # Write the epic code
            pen.penup()
            pen.goto(constants.start_x + epic_setting.column_start * constants.WEEK_WIDTH_PX + 5, vertical_position - 15)
            pen.write(epic_setting.epic.key, align="left", font=("Arial", 12, "normal"))
            
            # Write the epic title under the key
            pen.goto(constants.start_x + epic_setting.column_start * constants.WEEK_WIDTH_PX + 5, vertical_position - 30)
            pen.write(epic_setting.epic.title, align="left", font=("Arial", 10, "normal"))
        
        # Write the epic grouping text at the bottom of the blue box
        pen.penup()
        pen.goto(constants.start_x + epic_grouping.column_min * constants.WEEK_WIDTH_PX + 5, 
                constants.start_y - (epic_grouping.row_max + 1) * 40 - constants.margin_y - bottom_padding)
        pen.write(epic_grouping.grouping, align="left", font=("Arial", 14, "bold"))
        
        # Hide the turtle and display the window
        pen.hideturtle()







        