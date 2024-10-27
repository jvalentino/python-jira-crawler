
class ChartConstants:
    WEEK_WIDTH_PX = 100
    LIGHT_COLORS = [
        'lightblue',
        'lightcoral',
        'lightcyan',
        'lightgreen',
        'lightpink',
        'lightsalmon',
        'lightseagreen',
        'lightskyblue',
        'lightsteelblue'
    ]
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.margin_x = 50
        self.margin_y = 50
        
        self.start_x = -self.width // 2 + self.margin_x
        self.start_y = self.height // 2 - self.margin_y
        
        self.end_x = self.width // 2 - self.margin_x
        self.end_y = -self.height // 2 + self.margin_y
        
    def get_color(i):
        return ChartConstants.LIGHT_COLORS[i % len(ChartConstants.LIGHT_COLORS)]