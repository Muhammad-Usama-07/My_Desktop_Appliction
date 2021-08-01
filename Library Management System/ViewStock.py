from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as mysql
class AllBookClass():

    def __init__(self):
        self.root = Tk()
        self.root.title( 'List of Book issue' )
        self.root.geometry( "900x600+300+50" )
        self.root.minsize( 400 , 200 )
        self.root.maxsize( 1100 , 700 )
        self.root.configure( bg = '#bcdebb' )
        Label( self.root , text = " Note: Here you can make your study perfect... :) " , bg = "#66bd6d" ,
               relief = "solid" ,
               anchor = "w" , height = 2 , font = "Times%New%Roman 11 bold italic" ).pack()

        '''Frames
           ******'''

        lf1 = LabelFrame( self.root , text = "All Book click below" , fg = "red" , bg = '#33ff9e' ,
                         relief = "solid" , font = "Times%New%Roman 16 bold" )
        lf1.place(x = 5, y = 60, height = 150, width = 440)

        lf2 = LabelFrame( self.root , text = "Search for a Books" , fg = "red" , bg = '#33ff9e' ,
                          relief = "solid" , font = "Times%New%Roman 16 bold" )
        lf2.place( x = 445 , y = 60 , height = 150 , width = 450 )

        lf3 = Frame( self.root , bg = '#33ff9e' , highlightcolor="black", highlightbackground="black", highlightthickness = 2)
        lf3.place( x = 5 , y = 210 , height = 380 , width = 890 )

        '''Functions
          ***********'''

        def search_for_book():
            a = tv.get_children()
            for child in a:
                tv.delete(child)
            sb = Book_name_entry.get()
            if (sb == 0):
                messagebox.showerror("Warning", "Please Enter ISBN at least")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="lib_db")
                cursor = con.cursor()
                cursor.execute("select *  from Book where ISBN='" + sb + "'")
                rows = cursor.fetchall()
                for row in rows:
                    tv.insert('',END, values=row)
                con.close()
        def All_books():
            a = tv.get_children()
            for child in a:
                tv.delete(child)
            con = mysql.connect(host="localhost", user="root", password="", database="lib_db")
            cursor = con.cursor()
            cursor.execute("select *  from Book ")
            rows = cursor.fetchall()
            for row in rows:
                tv.insert('', END, values=row)
            con.close()
        '''Entries
          ********'''
        Book_name_entry = Entry( lf2 , width = 25 , relief = "solid" ,
                                       font = ("Times%New%Roman" , 15 , "bold") )
        Book_name_entry.place( x = 40 , y = 40 )

        '''
        Scroll Bar
        *********
        '''
        scroll_Bar = Scrollbar( lf3 , width = 25 , relief = "solid" )
        scroll_Bar.place( x = 849 , y = 10 , height = 288 )

        tv = ttk.Treeview(lf3, column=(1, 2, 3, 4, 5), show='headings', yscrollcommand=scroll_Bar.set)
        tv.pack(pady=10, ipadx=60, ipady=30)
        tv.heading(1, text='ISBN')
        tv.column(1, width=90)
        tv.heading(2, text='Book Name')
        tv.heading(3, text='Book auther')
        tv.heading(4, text='Book Edition')
        tv.column(4, width=100)
        tv.heading(5, text='Book Quantity')
        tv.column(5, width=100)

        scroll_Bar.config(command=tv.yview)

        '''Button
                   ******'''
        List_All_books_button = Button(lf1, text="All books", bg='#4dff4d',
                                       font=("Times%New%Roman", 17, "bold"),
                                       relief="groove", command=All_books)
        List_All_books_button.place(x=150, y=30)

        Search_for_book_button = Button(lf2, text="Search", bg='#4dff4d',
                                        font=("Times%New%Roman", 17, "bold"),
                                        relief="groove", command=search_for_book)
        Search_for_book_button.place(x=340, y=30)

        Back_button = Button(lf3, text="Back", bg='#4dff4d', font=("Times%New%Roman", 17, "bold"),
                             relief="groove"
                             , command=self.root.destroy)
        Back_button.place(x=790, y=310)

    def AllBookFunc(self):
        self.root.mainloop()




'''r = Tk()

AllBookClass()
r.mainloop()'''