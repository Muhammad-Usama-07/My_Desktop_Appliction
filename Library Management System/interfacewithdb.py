from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
class IssueBookClass():
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

        def Insert():
            ISBN = Book_ISBN_entry.get()
            code = Book_Name_entry.get()
            if (Book_ISBN_entry.get() == "" and Book_Name_entry.get() == ""):
                messagebox.showerror( "Warning" , "Please Enter ISBN and code of member" )
            else:
                conn = mysql.connect(host="localhost", user = "root", password = "", database = "check")
                cursor = conn.cursor()
                cursor.execute("insert into check_table values('"+ ISBN +"','"+ code +"' )")
                cursor.execute("commit")

                Book_ISBN_entry.delete(0, 'end')
                Book_Name_entry.delete(0, 'end')
                messagebox.showinfo("insert status", "Inserted successfully")
                conn.close()
        def delet():
            pass
        def udate():
            pass
        # Labels

        Book_ISBN_Label = Label( lf , text = "Enter ISBN of Book: " , bg = "#33ff9e" ,
                                    anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Book_ISBN_Label.place( x = 50 , y = 20 )

        Book_Name_Label = Label( lf , text = "Enter Name of Book: " , bg = "#33ff9e" ,
                                     anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Book_Name_Label.place( x = 45 , y = 80 )

        # Entries
        # ********


        Book_ISBN_entry = Entry( lf  , width = 25 , relief = "solid" ,
                                           font = ("Times%New%Roman" , 15 , "bold") )
        Book_ISBN_entry.place( x = 250 , y = 30 )


        Book_Name_entry = Entry( lf , width = 25 , relief = "solid" ,
                                      font = ("Times%New%Roman" , 15 , "bold") )
        Book_Name_entry.place( x = 250 , y = 90 )

        Book_Insert_button = Button( lf , text = "Add Book" , bg = '#4dff4d' , font = ("Times%New%Roman" , 15 , "bold") ,
                                  relief = "groove"
                                  , command = Insert )
        Book_Insert_button.place( x = 50 , y = 160 )
        Clear_button = Button(lf, text="Clear data", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"),
                                    relief="groove"
                                    , command=Insert)
        Clear_button.place(x=250, y=160)

        Delete_button = Button(lf, text="Delete data", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"),
                              relief="groove"
                              , command=Insert)
        Delete_button.place(x=50, y=250)

        Update_button = Button(lf, text="Update data", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"),
                               relief="groove"
                               , command=Insert)
        Update_button.place(x=250, y=250)

        Get_button = Button(lf, text="Get data", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"),
                               relief="groove"
                               , command=Insert)
        Get_button.place(x=50, y=350)

        Quit_button = Button( lf , text = "Quit" , bg = '#4dff4d' , font = ("Times%New%Roman" , 20 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Quit_button.place( x = 710 , y = 350 )

    def IssueBookFunc(self):
        self.root.mainloop()




r = Tk()
IssueBookClass()
r.mainloop()