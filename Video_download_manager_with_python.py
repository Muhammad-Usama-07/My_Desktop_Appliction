from tkinter import *
from tkinter import messagebox
class VDM():
    def __init__(self):
        self.root = Tk()
        self.root.title( 'Video Download Manager ' )
        self.root.geometry( "900x600+300+50" )
        self.root.minsize( 400 , 200 )
        self.root.maxsize( 1100 , 700 )
        self.root.configure( bg = '#bcdebb' )
        Label( self.root , text = " Welcome to my Video Downloader" , bg = "#66bd6d" ,
               relief = "solid" ,
               anchor = "w" , height = 2 , font = "Times%New%Roman 11 bold italic" ).pack(fill = X)




r = Tk()
VDM()
r.mainloop()