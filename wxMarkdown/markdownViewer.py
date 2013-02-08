#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wxversion
wxversion.select("2.8")

import wx
from webkit_gtk import WKHtmlWindow as HtmlWindow

try:
    import markdown2 as markdown
except ImportError:
    import markdown as markdown

import sys, os, webkit
#import jswebkit, html2text


from ucode import decode
#some constants
from constants import *

class webkit_panel(wx.Panel):
    def __init__(self, *args, **kwd):
        wx.Panel.__init__(self, *args, **kwd)
        self.html = HtmlWindow(self)
        self.html.SetEditable(True)
        self.html.SetSettings(__name__, False) #User Agent, JavaScript (on/off)
        self.box = wx.BoxSizer(wx.VERTICAL)
        self.box.Add(self.html, 1, wx.EXPAND)
        self.SetSizer(self.box)
        self.Layout()
        
    def loadString(self,string, mime, coding, baseurl):
        self.html.ctrl.load_string(string,mime,coding,baseurl)

class mdFrame(wx.Frame):
    
    __current_file = None
    
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        self.menubar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_OPEN, "&Open\tCtrl+O", "", wx.ITEM_NORMAL)
        file_menu.Append(wx.ID_REFRESH, "&Reload\tCtrl+R","",wx.ITEM_NORMAL)
        file_menu.AppendSeparator()
        file_menu.Append(wx.ID_EXIT, "&Quit\tCtrl+Q","",wx.ITEM_NORMAL)
        
        self.menubar.Append(file_menu, "&File")
        self.SetMenuBar(self.menubar)

        self.statusbar = self.CreateStatusBar(1, 0)

        self.SetTitle("mdView")
        self.statusbar.SetStatusWidths([-1])
        self.statusbar.SetStatusText('File: none')

        self.Bind(wx.EVT_MENU, self.onOpenFile, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.onExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.onReload, id=wx.ID_REFRESH)

    def addWebkit(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.html_window = webkit_panel(self,-1)
        main_sizer.Add(self.html_window, 1, wx.EXPAND, 0)
        self.SetSizer(main_sizer)
        self.setContent('','','')
        self.Layout()

    def onOpenFile(self, event):
        dlg = wx.FileDialog(self,"Open file", wildcard = "All files (*.*)|*.*", style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.openFile(dlg.GetPath())
        else:
            pass
        dlg.Destroy()
        event.Skip()
    
    def onExit(self,event):
        self.Hide()
        self.Destroy()
    
    def openFile(self,fn):
        self.__current_file = fn
        f = open(fn,'rb')
        md = decode(f.read())
        f.close()
        self.setContent(fn,markdown.markdown(md),os.path.dirname(fn))
        self.statusbar.SetStatusText(u'File: ' + fn)
        
    def setContent(self,title,body,basepath):
        bgc = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW).GetAsString(wx.C2S_HTML_SYNTAX)
        fgc = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT).GetAsString(wx.C2S_HTML_SYNTAX)
        
        html = HEAD % (title, ( CSS % (fgc, bgc) + CUSTOM_CSS) ) + body + FOOT
        
        self.html_window.loadString(html,"text/html","utf-8",u"file://" + basepath + u"/")

    def onReload(self,event):
        if self.__current_file is not None:
            self.openFile(self.__current_file)
        event.Skip()
