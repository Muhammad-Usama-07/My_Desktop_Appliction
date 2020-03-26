from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
class AddBookClass():
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

        def BookAdded():
            bn = new_book_name_entry.get()
            ba = new_book_auther_entry.get()
            isbn = new_ISBN_number_entry.get()
            be = Book_edition_number_entry.get()
            bq = Book_quantity_entry.get()
            if (new_book_name_entry.get() == "" and new_book_auther_entry.get() == "" and
                    new_ISBN_number_entry.get() == 0):
                messagebox.showerror( "Warning" , "Please Enter ISBN, name, and Auther at least" )
            else:
                con = mysql.connect(host = "localhost", user= "root", password = "", database= "lib_db")
                cursor = con.cursor()
                cursor.execute("insert into Book values('"+ isbn +"','"+ bn +"','"+ ba +"','"+ be +"','"+ bq +"')")
                cursor.execute("commit")
                new_book_name_entry.delete(0, 'end')
                new_book_auther_entry.delete(0, 'end')
                new_ISBN_number_entry.delete(0, 'end')
                Book_edition_number_entry.delete(0, 'end')
                Book_quantity_entry.delete(0, 'end')
                messagebox.showinfo("Insert status"," Data insert successfully")
                con.close()

        # Labels
        new_ISBN_number_Label = Label( lf , text = "Write new ISBN of the book:" , bg = "#33ff9e" ,
                                       anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        new_ISBN_number_Label.place( x = 30 , y = 20 )

        new_book_name_Label = Label( lf , text = "Enter Book Name: " , bg = "#33ff9e" ,
                                     anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        new_book_name_Label.place( x = 115 , y = 80 )

        Book_auther_Label = Label( lf , text = "Enter Book Auther: " , bg = "#33ff9e" ,
                                   anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Book_auther_Label.place( x = 105 , y = 140 )

        Book_edition_Label = Label( lf , text = "Enter edition of Book: " , bg = "#33ff9e" ,
                                    anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Book_edition_Label.place( x = 80 , y = 200 )

        Book_quantity_Label = Label( lf , text = "Enter quantity of Book: " , bg = "#33ff9e" ,
                                    anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Book_quantity_Label.place( x = 70 , y = 260 )

        # Entries
        # ********
        new_ISBN_number_entry = Entry( lf  , width = 25 , relief = "solid" ,
                                       font = ("Times%New%Roman" , 15 , "bold") )
        new_ISBN_number_entry.place( x = 300 , y = 30 )

        new_book_name_entry = Entry( lf , width = 25 , relief = "solid" ,
                                     font = ("Times%New%Roman" , 15 , "bold") )
        new_book_name_entry.place( x = 300 , y = 90 )

        new_book_auther_entry = Entry( lf , width = 25 , relief = "solid" ,
                                       font = ("Times%New%Roman" , 15 , "bold") )
        new_book_auther_entry.place( x = 300 , y = 150 )

        Book_edition_number_entry = Entry( lf  , width = 25 , relief = "solid" ,
                                           font = ("Times%New%Roman" , 15 , "bold") )
        Book_edition_number_entry.place( x = 300 , y = 210 )

        Book_quantity_entry = Entry( lf
                                      , width = 25 , relief = "solid" ,
                                      font = ("Times%New%Roman" , 15 , "bold") )
        Book_quantity_entry.place( x = 300 , y = 270 )

        Add_Book_button = Button( lf , text = "Add Book" , bg = '#4dff4d' , font = ("Times%New%Roman" , 20 , "bold") ,
                                  relief = "groove"
                                  , command = BookAdded )
        Add_Book_button.place( x = 120 , y = 350 )

        Back_button = Button( lf , text = "Back" , bg = '#4dff4d' , font = ("Times%New%Roman" , 20 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Back_button.place( x = 710 , y = 350 )


        def AddBookFunc(self):
            new_ISBN_number_entry.get()




'''r = Tk()
obj = AddBookClass()
r.mainloop()'''