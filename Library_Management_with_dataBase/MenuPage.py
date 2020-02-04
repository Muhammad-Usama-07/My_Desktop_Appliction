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

        Books_detail = Label( lf1 , text = "Books detail" , fg = "red" , bg = '#33ff9e'
                          , font = ("Times%New%Roman" , 20 , "bold" , "underline") )
        Books_detail.place( x = 60 , y = 30 )

        member_detail = Label( lf1 , text = "Members detail" , fg = "red" , bg = '#33ff9e'
                               , font = ("Times%New%Roman" , 20 , "bold" , "underline") )
        member_detail.place( x = 450 , y = 30 )

        Stock_detail = Label( lf1 , text = "Stock detail" , fg = "red" , bg = '#33ff9e'
                              , font = ("Times%New%Roman" , 20 , "bold" , "underline") )
        Stock_detail.place( x = 450 , y = 220 )


        # Creating Buttons

        add_books = Button( lf1 , text = "Add a Book" , bg = '#4dff4d' , font = ("Times%New%Roman" , 15 , "bold") ,
                        relief = "ridge" )
        add_books.place( x = 65 , y = 85 )

        remove_books = Button( lf1 , text = "Remove a Book" , bg = '#4dff4d' ,
                               font = ("Times%New%Roman" , 15 , "bold") ,
                               relief = "ridge" )
        remove_books.place( x = 65 , y = 155 )

        issue_books = Button( lf1 , text = "Issue a Book" , bg = '#4dff4d' , font = ("Times%New%Roman" , 15 , "bold") ,
                              relief = "ridge"  )
        issue_books.place( x = 65 , y = 220 )

        list_issue_books = Button( lf1 , text = "List of Book issue" , bg = '#4dff4d' ,
                                   font = ("Times%New%Roman" , 15 , "bold") ,
                                   relief = "ridge"  )
        list_issue_books.place( x = 65 , y = 290 )


r = Tk()

Menu_class_obj = MenuPageClass(r)
r.mainloop()