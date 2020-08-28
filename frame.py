import wx
from controller import PyDrawController
from drwingpanel import DrawingPanel
from menubar import PyDrawMenuBar
from toolbar import PyDrawToolBar

class App_Frame(wx.Frame):
    def __init__(self, title):
        super().__init__(parent=None,title=title,size=(300,300))

        self.controller = PyDrawController(self)
        self.vertical_box_sizer = wx.BoxSizer(wx.VERTICAL)

        self.SetSizer(self.vertical_box_sizer)
        
        self.SetMenuBar(PyDrawMenuBar())

        self.vertical_box_sizer.Add((PyDrawToolBar(self),wx.ID_ANY,wx.EXPAND | wx.ALL, 20 ))
        self.drawing_panel = DrawingPanel(self, self.controller.get_mode)
        self.drawing_controller = self.drawing_panel.controller
        self.vertical_box_sizer.Add(self.drawing_panel,wx.ID_ANY,wx.EXPAND | wx.ALL)
        self.Bind(wx.EVT_MENU, self.controller.command_menu_handler)
        self.Center()
