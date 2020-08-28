from frame import App_Frame
import wx

class PyDrawApp(wx.App):
    def OnInit(self):
        """ Initialise the GUI display"""
        frame = App_Frame(title='PyDraw')
        frame.Show()
        return True


# Run the GUI application
app = PyDrawApp()
app.MainLoop()