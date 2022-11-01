# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import json
from playsound import playsound
from pynput.keyboard import Listener
from threading import Thread

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):

        try: 
            with open("gongde.json", "r") as f: 
                self.info = json.loads(f.read())
                self.gongdenum = self.info["gongde"]
        except FileNotFoundError: 
            with open("gongde.json", "w") as f:
                self.info = {"gongde": 0}
                f.write(json.dumps(self.info, indent=4))
            self.gongdenum = 0

        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"电子木鱼", pos = wx.DefaultPosition, size = wx.Size( 200,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 127, 127, 127 ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.number = wx.StaticText( self, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.number.Wrap( -1 )

        self.number.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
        self.number.SetLabelText(text = f"目前功德:{self.gongdenum}")

        bSizer3.Add( self.number, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.gongde = wx.StaticText( self, wx.ID_ANY, u"功德 + 1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gongde.Wrap( -1 )

        self.gongde.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.gongde.Hide()

        bSizer5.Add( self.gongde, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.muyutietu = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"./muyu.jpg", wx.BITMAP_TYPE_ANY ), wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
        bSizer2.Add( self.muyutietu, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        self.Bind(wx.EVT_CLOSE, self.exit_sys)

        self.new_thread = Thread(target=self.start).start()
        # self.start()
        # self.shouhu = Thread(target=self.quit).start()


    def __del__( self ):
        pass


    def on_press(self, key): 
        try: 
            if key.name == "space": 
                self.gongde.Show(True)
                self.gongdenum += 1
                self.info["gongde"] += 1
                # self.
                playsound("./muyu.mp3")
                self.number.SetLabelText(text = f"目前功德:{self.gongdenum}")
                with open("gongde.json", "w") as f: 
                    f.write(json.dumps(self.info, indent=4))
                self.gongde.Hide()
                # print("Add.")
        except AttributeError: 
            pass

    def start(self): 
        with Listener(on_press=self.on_press) as l: 
            l.join()

    def exit_sys(self, s): 
        import os
        pid = os.getpid()
        os.system(f"taskkill /F /PID {pid}")

if __name__ == "__main__": 
    app = wx.App()
    frame = MainFrame(None)
    frame.Show(True)
    # frame.start()
    app.MainLoop()
