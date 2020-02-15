from tkinter import *
from tkinter import messagebox
class RemoveBookClass():
    def __init__(self):
        self.root = Tk()
        self.root.title( 'Add Book' )
        self.root.geometry( "900x600+300+50" )
        self.root.minsize( 400 , 200 )
        self.root.maxsize( 1100 , 700 )
        self.root.configure( bg = '#bcdebb' )
        Label( self.root , text = " Note: Here you can make your study perfect... :) " , bg = "#66bd6d" ,
               relief = "solid" ,
               anchor = "w" , height = 2 , font = "Times%New%Roman 11 bold italic" ).pack()

        lf = LabelFrame( self.root , text = "Fill the Details" , fg = "red" , bg = '#33ff9e' ,
                         relief = "solid" , font = "Times%New%Roman 16 bold" , height = 550 )
        lf.pack( fill = "both" , expand = True , padx = 20 , pady = 20 )

        # Functions
        # ***********

        def BookRemoved():
            pass

        Remove_Book_button = Button( lf , text = "Add Book" , bg = '#4dff4d' , font = ("Times%New%Roman" , 20 , "bold") ,
                                  relief = "groove"
                                  , command = BookRemoved )
        Remove_Book_button.place( x = 120 , y = 350 )

        Back_button = Button( lf , text = "Back" , bg = '#4dff4d' , font = ("Times%New%Roman" , 20 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Back_button.place( x = 710 , y = 350 )

    def RemoveBookFunc(self):
        self.root.mainloop()



r = Tk()
RemoveBookClass()

r.mainloop()