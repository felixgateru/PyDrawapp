import wx
from constants import PyDraw_Constants

class PyDrawController:

    def __init__(self, view):
        self.view = view
        self.mode = PyDraw_Constants.SQUARE_MODE
    
    def set_circle_mode(self):
        self.mode = PyDraw_Constants.CIRCLE_MODE
    
    def set_line_mode(self):
        self.mode = PyDraw_Constants.LINE_MODE
    
    def set_square_mode(self):
        self.mode = PyDraw_Constants.SQUARE_MODE
    
    def set_text_mode(self):
        self.mode = PyDraw_Constants.TEXT_MODE
    
    def clear_drawing(self):
        self.view.drawing_controller.clear()
    
    def get_mode(self):
        return self.mode
    
    def command_menu_handler(self, command_event):
        id = command_event.GetId()
        if id == wx.ID_NEW:
            print('Clear the drawing area')
            self.clear_drawing()
        elif id == wx.ID_OPEN:
            print('Open a drawing file')
        elif id == wx.ID_SAVE:
            print('Save a drawing file')
        elif id == wx.ID_EXIT:
            print('Quite the application')
            self.view.Close()
        elif id == PyDraw_Constants.LINE_ID:
            print('set drawing mode to line')
            self.set_line_mode()
        elif id == PyDraw_Constants.SQUARE_ID:
            print('set drawing mode to square')
            self.set_square_mode()
        elif id == PyDraw_Constants.CIRCLE_ID:
            print('set drawing mode to circle')
            self.set_circle_mode()
        elif id == PyDraw_Constants.TEXT_ID:
            print('set drawing mode to Text')
            self.set_text_mode()
        else:
            print('Unknown option', id)
