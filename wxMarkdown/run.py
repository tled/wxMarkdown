
from markdownViewer import *
import os, sys

def main():
    mdfile = None
    try:
        os.stat(sys.argv[1])
        mdfile = os.path.abspath(sys.argv[1])
    except:
        pass
    
    app = wx.PySimpleApp(0)
    mdViewF = mdFrame(None, -1, "", size = [800,600])
    app.SetTopWindow(mdViewF)
    mdViewF.Show()
    mdViewF.addWebkit()
    if mdfile is not None:
        mdViewF.openFile(mdfile)
    app.MainLoop()

