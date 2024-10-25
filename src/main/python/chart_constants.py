
class ChartConstants:
    WEEK_WIDTH_PX = 100
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.margin_x = 50
        self.margin_y = 50
        
        self.start_x = -self.width // 2 + self.margin_x
        self.start_y = self.height // 2 - self.margin_y
        
        self.end_x = self.width // 2 - self.margin_x
        self.end_y = -self.height // 2 + self.margin_y