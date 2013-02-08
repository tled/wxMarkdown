import wx

import gobject
gobject.threads_init()

import pygtk,gtk, gtk.gdk, webkit
pygtk.require('2.0')

class WKHtmlWindow(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        whdl = self.GetHandle()
        window = gtk.gdk.window_lookup(whdl)
        self.pizza = pizza = window.get_user_data()
        self.scrolled_window = scrolled_window = pizza.parent
        scrolled_window.remove(pizza)
        self.ctrl = ctrl = webkit.WebView()
        scrolled_window.add(ctrl)
        scrolled_window.show_all()

    def SetEditable(self, editable=True):
        self.ctrl.set_editable(editable)

    def LoadUrl(self, url):
        self.ctrl.load_uri(url)

    def HistoryBack(self):
        self.ctrl.go_back()

    def HistoryForward(self):
        self.ctrl.go_forward()

    def StopLoading(self):
        self.ctrl.stop_loading()
    
    def SetSettings(self,user_agent = "whatever", scripting = False):
        settings = webkit.WebSettings()
        settings.set_property('user-agent', user_agent)
        settings.set_property("enable-scripts",scripting)
        self.ctrl.set_settings(settings)
