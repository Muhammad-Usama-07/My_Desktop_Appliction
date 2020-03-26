from tkinter import *
from tkinter import messagebox
from Library_Management_project import AddBook
import mysql.connector as mysql
class RemoveBookClass():
    def __init__(self):
        self.root = Tk()
        self.root.title( 'Remove Book' )
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
            rb = Remove_book_ISBN_entry.get()
            if (rb == 0):
                messagebox.showerror( "Warning" , "Please Enter ISBN at least" )
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="lib_db")
                cursor = con.cursor()
                cursor.execute("delete from Book where ISBN='" + rb + "'")
                cursor.execute("commit")
                Remove_book_ISBN_entry.delete(0, 'end')
                messagebox.showinfo("Delete status", " Data Deleted successfully")
                con.close()

        '''Labels
          ********'''
        Remove_book_ISBN_Label = Label( lf , text = "Enter ISBN of Book:" , bg = "#33ff9e" ,
                                        anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Remove_book_ISBN_Label.place( x = 20 , y = 20 )


        '''Entries
           ********'''
        Remove_book_ISBN_entry = Entry( lf , width = 25 , relief = "solid" ,
                                           font = ("Times%New%Roman" , 15 , "bold") )
        Remove_book_ISBN_entry.place( x = 220 , y = 30 )

        #Creating ScrollBar

        scroll_Bar = Scrollbar(lf, width = 25, relief = "solid")
        scroll_Bar.place(x = 496, y = 80, height = 245)

        Book_Detail = Text(lf, width = 59, height = 15, relief = "solid" ,yscrollcommand =  scroll_Bar.set)
        Book_Detail.place(x = 20, y = 80)
        scroll_Bar.config( command = Book_Detail.yview )

        '''Buttons
           ********'''

        Remove_Book_button = Button( lf , text = "Remove this Book" , bg = '#4dff4d' , font = ("Times%New%Roman" , 17 , "bold") ,
                                  relief = "groove"
                                  , command = BookRemoved )
        Remove_Book_button.place( x = 120 , y = 400 )

        Back_button = Button( lf , text = "Back" , bg = '#4dff4d' , font = ("Times%New%Roman" , 17 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Back_button.place( x = 710 , y = 400 )

    def RemoveBookFunc(self):
        self.root.mainloop()

r = Tk()
RemoveBookClass()

r.mainloop()