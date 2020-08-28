import wx

class PyDrawToolBar(wx.ToolBar):
    def __init__(self,parent):
        super().__init__(parent)
        self.AddTool(toolId=wx.ID_NEW, label="New",bitmap=wx.Bitmap("new.gif"), shortHelp='Open drawing',kind=wx.ITEM_NORMAL)
        self.AddTool(toolId=wx.ID_OPEN, label="Open",bitmap=wx.Bitmap("load.gif"), shortHelp='Open drawing',kind=wx.ITEM_NORMAL)
        self.AddTool(toolId=wx.ID_SAVE, label="Save",bitmap=wx.Bitmap("save.gif"), shortHelp="Save drawing", kind=wx.ITEM_NORMAL)
        self.Realize()