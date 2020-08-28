from constants import PyDraw_Constants

class DrawingController:
    def __init__(self, view, model, get_mode):
        self.view = view
        self.model = model
        self.get_mode = get_mode
    
    def on_mouse_click(self, mouse_event):
        point = mouse_event.GetPosition()
        self.add(self.get_mode(), point)
    
    def add(self, mode, point, size=30):
        if mode == PyDraw_Constants.SQUARE_MODE:
            fig = Square(self.view, point, wx.Size(size, size))
        elif mode == PyDraw_Constants.CIRCLE_MODE:
            fig = Circle(self.view, point, size)
        elif mode == PyDraw_Constants.TEXT_MODE:
            fig = Text(self.view, point, size)
        elif mode == PyDraw_Constants.LINE_MODE:
            fig = Line(self.view, point, size)
        
        self.model.add_figure(fig)

    def clear(self):
        self.model.clear_figures()
        self.view.Refresh()
