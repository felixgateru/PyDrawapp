
class DrawingModel:
    def __init__(self):
        self.contents = []
    
    def clear_figures(self):
        self.contents = []
    
    def add_figure(self, figure):
        self.contents.append(figure)