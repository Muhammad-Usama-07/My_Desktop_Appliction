

from tkinter import *
from Library_Management_project import AddBook
from Library_Management_project import AddMember
from Library_Management_project import RemoveBook

class MenuPageClass(AddBook.AddBookClass, AddMember.AddMemberClass):
    def __init__(self):
        self.root = Tk()
        self.root.title( 'Module' )  # title
        self.root.configure( bg = '#bcdebb' )
        self.root.geometry( "900x600+300+50" )  # (width X hight + from_right + from_left))
        self.root.minsize( 400 , 200 )
        self.root.maxsize( 1100 , 700 )
        Label( self.root , text = " Note: Here you can make your study perfect... :) " , bg = "#66bd6d" , relief = "solid" ,
               anchor = "w" , height = 2 , font = "Times%New%Roman 11 bold italic" ).pack()

        # Creating Frame
        lf1 = LabelFrame( self.root , text = "Enter Your choice" , fg = "red" , bg = '#33ff9e' ,
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
                            relief = "ridge", command = AddBook.AddBookClass)
        add_books.place( x = 65 , y = 85 )

        add_member = Button( lf1 , text = "Add a Member" , bg = '#4dff4d' , font = ("Times%New%Roman" , 15 , "bold") ,
                             relief = "ridge" , command = AddMember.AddMemberClass )
        add_member.place( x = 450 , y = 85 )

        remove_books = Button( lf1 , text = "Remove a Book" , bg = '#4dff4d' ,
                               font = ("Times%New%Roman" , 15 , "bold") ,
                               relief = "ridge" , command = RemoveBook.RemoveBookClass)
        remove_books.place( x = 65 , y = 155 )

        issue_books = Button( lf1 , text = "Issue a Book" , bg = '#4dff4d' , font = ("Times%New%Roman" , 15 , "bold") ,
                              relief = "ridge" )
        issue_books.place( x = 65 , y = 220 )

        list_issue_books = Button( lf1 , text = "List of Book issue" , bg = '#4dff4d' ,
                                   font = ("Times%New%Roman" , 15 , "bold") ,
                                   relief = "ridge" )
        list_issue_books.place( x = 65 , y = 290 )

        remove_member = Button( lf1 , text = "Remove a Member" , bg = '#4dff4d' ,
                                font = ("Times%New%Roman" , 15 , "bold") ,
                                relief = "ridge" )
        remove_member.place( x = 450 , y = 155 )

        view_stock_button = Button( lf1 , text = "View Stock" , bg = '#4dff4d' ,
                                    font = ("Times%New%Roman" , 15 , "bold") ,
                                    relief = "ridge" )
        view_stock_button.place( x = 450 , y = 280 )

        Quit_button = Button( lf1 , text = "Quit" , bg = '#4dff4d' , font = ("Times%New%Roman" , 17 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Quit_button.place( x = 710 , y = 350 )

    def MenuFunc(self):
        self.root.mainloop()


r = Tk()

onj = MenuPageClass()

r.mainloop()