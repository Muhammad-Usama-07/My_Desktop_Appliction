from tkinter import *
from tkinter import messagebox
from tkinter import ttk
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
        def Search():
            a = tv.get_children()
            for child in a:
                tv.delete(child)
            rb = Remove_book_ISBN_entry.get()
            if (rb == 0):
                messagebox.showerror( "Warning" , "Please Enter ISBN at least" )
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="lib_db")
                cursor = con.cursor()
                cursor.execute("select *  from Book where ISBN='" + rb + "'")
                rows = cursor.fetchall()
                for row in rows:
                    tv.insert('',END, values=row)
                con.close()


        def BookRemoved():
            a = tv.get_children()
            for child in a:
                tv.delete(child)
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
        scroll_Bar.place(x = 814, y = 80, height = 286)
        tv = ttk.Treeview(lf, column=(1, 2, 3, 4, 5), show='headings', yscrollcommand=scroll_Bar.set)
        tv.pack(padx=10, pady=80, ipadx=40, ipady=30)
        tv.heading(1, text='ISBN')
        tv.column(1, width=90)
        tv.heading(2, text='Book Name')
        tv.heading(3, text='Book auther')
        tv.heading(4, text='Book Edition')
        tv.column(4, width=100)
        tv.heading(5, text='Book Quantity')
        tv.column(5, width=100)

        scroll_Bar.config(command=tv.yview)

        '''Buttons
           ********'''

        Remove_Book_button = Button( lf , text = "Remove this Book" , bg = '#4dff4d' , font = ("Times%New%Roman" , 17 , "bold") ,
                                  relief = "groove"
                                  , command = BookRemoved )
        Remove_Book_button.place( x = 120 , y = 400 )

        Search_button = Button(lf, text="Search", bg='#4dff4d', font=("Times%New%Roman", 17, "bold"),
                             relief="groove"
                             , command=Search)
        Search_button.place(x=520, y=20)

        Back_button = Button( lf , text = "Back" , bg = '#4dff4d' , font = ("Times%New%Roman" , 17 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Back_button.place( x = 710 , y = 400 )

    def RemoveBookFunc(self):
        self.root.mainloop()

'''r = Tk()
RemoveBookClass()

r.mainloop()'''