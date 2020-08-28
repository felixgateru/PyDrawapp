
class Figure(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY, pos=None,size=None, style=wx.TAB_TRAVERSAL):
        wx.Panel.__init__(self, parent, id=id, pos=pos,size=size, style=style)
        self.point = pos
        self.size = size

    @abstractmethod
    def on_paint(self, dc):
       pass

class Square(Figure):
    def __init__(self, parent, pos, size):
        super().__init__(parent=parent, pos=pos, size=size)
    
    def on_paint(self, dc):
        dc.DrawRectangle(self.point, self.size)

class Circle(Figure):
    def __init__(self, parent, pos, size):
        super().__init__(parent=parent, pos=pos,size=wx.Size(size, size))
        self.radius = (size - 10) / 2
        self.circle_center = wx.Point(self.point.x +self.radius, self.point.y + self.radius)
    
    def on_paint(self, dc):
        dc.DrawCircle(pt=self.circle_center,radius=self.radius)

class Line(Figure):
    def __init__(self, parent, pos, size):
        super().__init__(parent=parent, pos=pos,size=wx.Size(size, size))
        self.end_point = wx.Point(self.point.x + size,self.point.y + size)
    
    def on_paint(self, dc):
        dc.DrawLine(pt1=self.point, pt2=self.end_point)
    

class Text(Figure):
    def __init__(self, parent, pos, size):
        super().__init__(parent=parent, pos=pos,size=wx.Size(size, size))
    
    def on_paint(self, dc):
        dc.DrawText(text='Text', pt=self.point)