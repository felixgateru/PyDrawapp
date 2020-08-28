import wx
from constants import PyDraw_Constants

class PyDrawMenuBar(wx.MenuBar):

    def __init__(self):
        super().__init__()
        fileMenu = wx.Menu()
        newMenuItem = wx.MenuItem(fileMenu,wx.ID_NEW, text="New",kind=wx.ITEM_NORMAL)
        newMenuItem.SetBitmap(wx.Bitmap("new.gif"))
        fileMenu.Append(newMenuItem)

        openMenuItem = wx.MenuItem(fileMenu,wx.ID_OPEN, text="Open",kind=wx.ITEM_NORMAL)
        openMenuItem.SetBitmap(wx.Bitmap("open.gif"))
        fileMenu.Append(openMenuItem)

        saveMenuItem = wx.MenuItem(fileMenu,wx.ID_SAVE, text="Save",kind=wx.ITEM_NORMAL)
        saveMenuItem.SetBitmap(wx.Bitmap("save.gif"))
        fileMenu.Append(saveMenuItem)

        fileMenu.AppendSeparator()
        quit = wx.MenuItem(fileMenu,wx.ID_EXIT,'&Quit\tCtrl+Q')

        fileMenu.Append(quit)
        self.Append(fileMenu, '&File') 

        drawingMenu = wx.Menu()
        lineMenuItem = wx.MenuItem(drawingMenu,PyDraw_Constants.LINE_ID, text="Line", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(lineMenuItem)
        squareMenuItem = wx.MenuItem(drawingMenu,PyDraw_Constants.SQUARE_ID, text="Square", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(squareMenuItem)
        circleMenuItem = wx.MenuItem(drawingMenu,PyDraw_Constants.CIRCLE_ID, text="Circle", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(circleMenuItem)
        textMenuItem = wx.MenuItem(drawingMenu,PyDraw_Constants.TEXT_ID, text="Text", kind=wx.ITEM_NORMAL)

        drawingMenu.Append(textMenuItem)
        
        self.Append(drawingMenu,"&Drawing")


