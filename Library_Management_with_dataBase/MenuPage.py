from tkinter import *


class MenuPageClass:
    def __init__(self, root):

        self.root = root
        root.title( 'Module' )  # title
        root.configure( bg = '#bcdebb' )
        root.geometry( "900x600+300+50" )  # (width X hight + from_right + from_left))
        root.minsize( 400 , 200 )
        root.maxsize( 1100 , 700 )
        Label( root , text = " Note: Here you can make your study perfect... :) " , bg = "#66bd6d" , relief = "solid" ,
               anchor = "w" , height = 2 , font = "Times%New%Roman 11 bold italic" ).pack()

        # Creating Frame
        lf1 = LabelFrame( root , text = "Enter Your choice" , fg = "red" , bg = '#33ff9e' ,
                          relief = "solid" , font = "Times%New%Roman 16 bold" , height = 550 )
        lf1.pack( fill = "both" , expand = True , padx = 20 , pady = 20 )

        Books_detail = Label( lf1 , text = "Books detail")



r = Tk()

Menu_class_obj = MenuPageClass(r)
r.mainloop()