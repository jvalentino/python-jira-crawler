from chart_constants import ChartConstants

import turtle
from PIL import Image
import canvasvg
import cairosvg


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
        
        y_offset = 0
        y_offset = self.draw_grouping(chart_settings, constants, chart_settings.epic_groupings[2], y_offset)
        y_offset = self.draw_grouping(chart_settings, constants, chart_settings.epic_groupings[0], y_offset)
        y_offset = self.draw_grouping(chart_settings, constants, chart_settings.epic_groupings[1], y_offset)


        # Save the drawing to a PNG file
        canvas = screen.getcanvas()
        self.save_as_png(canvas)

        # Clean up
        turtle.bye()
        
    def save_as_png(self, canvas):
        # Adjust font size in the SVG
        for item in canvas.find_all():
            if canvas.type(item) == 'text':
                font = canvas.itemcget(item, 'font')
                # Extract the font size from the font string
                font_parts = font.split()
                if len(font_parts) > 1:
                    try:
                        font_size = int(font_parts[1])
                        # Reduce the font size by a small factor (e.g., 0.9)
                        new_font_size = int(font_size * 0.9)
                        # Reconstruct the font string with the new font size
                        new_font = f"{font_parts[0]} {new_font_size} {' '.join(font_parts[2:])}"
                        canvas.itemconfig(item, font=new_font)
                    except ValueError:
                        # If font size extraction fails, skip this item
                        continue
        # Save the canvas as an SVG file
        canvasvg.saveall("target/chart.svg", canvas)
        
        # Convert the SVG to a high-resolution PNG using cairosvg
        cairosvg.svg2png(url="target/chart.svg", write_to="target/chart.png")
        
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

    def draw_grouping(self, chart_settings, constants, epic_grouping, y_offset=0):
        pen = turtle.Turtle()
        pen.speed(0)
        
        # Define padding
        top_padding = 10
        bottom_padding = 20  # Increased bottom padding
        
        # Calculate the starting y position with the y_offset
        start_y = constants.start_y - y_offset
        
        # Draw the light blue box around the entire area
        pen.color("black", "lightblue")  # Set the outline color to black and fill color to light blue
        pen.penup()
        pen.goto(
            constants.start_x + epic_grouping.column_min * constants.WEEK_WIDTH_PX, 
            start_y - constants.margin_y + top_padding)
        
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
            vertical_position = start_y - (epic_setting.row * 40) - constants.margin_y
            
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
                start_y - (epic_grouping.row_max + 1) * 40 - constants.margin_y - bottom_padding)
        pen.write(epic_grouping.grouping, align="left", font=("Arial", 14, "bold"))
        
        # Hide the turtle and display the window
        pen.hideturtle()
        
        # Calculate the height of the blue box
        blue_box_height = (epic_grouping.row_max + 1) * 40 + top_padding + bottom_padding
        
        # Return the new y_offset
        return y_offset + blue_box_height + 20



        