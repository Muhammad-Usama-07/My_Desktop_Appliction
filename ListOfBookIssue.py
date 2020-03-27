from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
class ListBookIssueClass():
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

        lf1 = LabelFrame( self.root , text = "List of all Books issued" , fg = "red" , bg = '#33ff9e' ,
                         relief = "solid" , font = "Times%New%Roman 16 bold" )
        lf1.place(x = 5, y = 60, height = 150, width = 440)

        lf2 = LabelFrame( self.root , text = "Search for issued Books" , fg = "red" , bg = '#33ff9e' ,
                          relief = "solid" , font = "Times%New%Roman 16 bold" )
        lf2.place( x = 445 , y = 60 , height = 150 , width = 450 )

        lf3 = Frame( self.root , bg = '#33ff9e' , highlightcolor="black", highlightbackground="black", highlightthickness = 2)
        lf3.place( x = 5 , y = 210 , height = 380 , width = 890 )

        '''Functions
          ***********'''
        def search_for_issue_book():
            sb = Book_name_entry.get()
            if (sb == 0):
                messagebox.showerror("Warning", "Please Enter ISBN at least")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="lib_db")
                cursor = con.cursor()
                cursor.execute("select *  from Issue_book where Cm='" + sb + "'")
                rows = cursor.fetchall()
                for row in rows:
                    insertdata = "               " + str(row[0]) + '                                               ' + str(row[1])
                    Book_Detail.insert(Book_Detail.size() + 1, insertdata)
                con.close()
        def All_issue_books():
            pass

        '''Entries
          ********'''
        Book_name_entry = Entry( lf2 , width = 25 , relief = "solid" ,
                                       font = ("Times%New%Roman" , 15 , "bold") )
        Book_name_entry.place( x = 40 , y = 40 )

        '''
                Scroll Bar
                *********
                '''
        scroll_Bar = Scrollbar(lf3, width=25, relief="solid")
        scroll_Bar.place(x=834, y=10, height=288)

        Details = "          Member Code" + "                       Book Code"
        dash = "          *****************" + "                       **************"
        Book_Detail = Listbox(lf3, width=90, height=15, relief="solid", yscrollcommand=scroll_Bar.set,
                              font=("Times%New%Roman", 12, "bold italic"))
        Book_Detail.place(x=20, y=10)
        Book_Detail.insert(0, Details)
        Book_Detail.insert(1, dash)

        scroll_Bar.config(command=Book_Detail.yview)

        '''Button
           ******'''
        List_All_books_button = Button( lf1 , text = "All books" , bg = '#4dff4d' ,
                                     font = ("Times%New%Roman" , 17 , "bold") ,
                                     relief = "groove", command = All_issue_books)
        List_All_books_button.place( x = 150 , y = 30)

        Search_for_book_button = Button( lf2 , text = "Search" , bg = '#4dff4d' ,
                                        font = ("Times%New%Roman" , 17 , "bold") ,
                                        relief = "groove", command = search_for_issue_book )
        Search_for_book_button.place( x = 340 , y = 30 )

        Back_button = Button(lf3, text="Back", bg='#4dff4d', font=("Times%New%Roman", 17, "bold"),
                             relief="groove"
                             , command=self.root.destroy)
        Back_button.place(x=790, y=310)



    def ListBookIssueFunc(self):
        self.root.mainloop()



r = Tk()
obj = ListBookIssueClass()
r.mainloop()