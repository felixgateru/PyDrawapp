from drawingmodel import DrawingModel
import wx

class DrawingPanel(wx.Panel):
    def __init__(self,parent, get_mode):
        super().__init__(parent,-1)
        self.SetBackgroundColor(wx.Color(255,255,255))
        self.model = DrawingModel()
        self.controller = DrawingController(self, self.model,get_mode)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN,self.controller.on_mouse_click)
    
    def on_paint(self, event):
        dc =wx.PaintDC(self)
        for figure in self.model.contents:
            figure.on_paint(dc)