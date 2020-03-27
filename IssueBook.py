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

        ''' Functions
            *********'''
        def CheckBook():
            bi = Book_ISBN_entry.get()
            if (bi == 0):
                messagebox.showerror("Warning", "Please Enter ISBN at least")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="lib_db")
                cursor = con.cursor()
                cursor.execute("select *  from Book where ISBN='" + bi + "'")
                rows = cursor.fetchall()
                for row in rows:
                    insertdata = "             " + str(row[0]) + '                   ' + row[1] + \
                                 '                           ' + row[2] + '                         ' + row[3] + \
                                 '                                             ' + str(row[4])
                    Detail.insert(Detail.size() + 1, insertdata)
                con.close()
        def CheckMemebr():
            mc = Member_code_entry.get()
            if (mc == 0):
                messagebox.showerror("Warning", "Please Enter Code of member at least")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="lib_db")
                cursor = con.cursor()
                cursor.execute("select *  from Members where Code='" + mc + "'")
                rows = cursor.fetchall()
                for row in rows:
                    insertdata = "            " + str(row[0]) + '                  ' + row[1] + \
                                 '                                   ' + str(row[2]) + '                                ' + \
                                 str(row[3]) + \
                                 '                                  ' + str(row[4])
                    Detail.insert(Detail.size() + 1, insertdata)
                con.close()

        def BookIssued():
            bi = Book_ISBN_entry.get()
            mc = Member_code_entry.get()
            if (bi == 0 and mc == 0):
                messagebox.showerror( "Warning" , "Please Enter ISBN and code of member" )
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="lib_db")
                cursor = con.cursor()
                cursor.execute("INSERT INTO `issue_book`(Cm, ISBN_of_book) SELECT members.Code, book.ISBN FROM members, book WHERE members.Code = '" + mc + "' AND book.ISBN = '" + bi + "'")
                con.close()

        # Labels

        Book_ISBN_Label = Label( lf , text = "Enter ISBN of Book: " , bg = "#33ff9e" ,
                                    anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Book_ISBN_Label.place( x = 55 , y = 10 )

        Member_code_Label = Label( lf , text = "Enter code of member: " , bg = "#33ff9e" ,
                                     anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Member_code_Label.place( x = 20 , y = 60 )

        # Entries
        # ********

        Book_ISBN_var = IntVar()
        Book_ISBN_entry = Entry( lf, textvariable = Book_ISBN_var,width = 25 , relief = "solid" ,
                                           font = ("Times%New%Roman" , 15 , "bold") )
        Book_ISBN_entry.place( x = 250 , y = 20 )

        Member_code_var = IntVar()
        Member_code_entry = Entry( lf,textvariable =Member_code_var  , width = 25 , relief = "solid" ,
                                      font = ("Times%New%Roman" , 15 , "bold") )
        Member_code_entry.place( x = 250 , y = 70 )

        '''
                Scroll Bar
                *********
                '''
        scroll_Bar = Scrollbar(lf, width=25, relief="solid")
        scroll_Bar.place(x=823, y=120, height=288)

        Titles = "          Code" + "               Member/Book" + "              age/Auther" \
                  + "            Vali: Year/Edition" + "              Telephone NO/Quantity:"
        dash = "          *******" + "              ******************" + "              *************" \
               + "              *********************" + "             *******************************"
        Detail = Listbox(lf, width=90, height=15, relief="solid", yscrollcommand=scroll_Bar.set,
                              font=("Times%New%Roman", 12, "bold italic"))
        Detail.place(x=10, y=120)
        Detail.insert(0, Titles)
        Detail.insert(1, dash)

        scroll_Bar.config(command=Detail.yview)

        '''Buttons
           *******'''
        check_button = Button(lf, text="Check Book", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"),
                                    relief="groove", command=CheckBook)
        check_button.place(x = 550 , y = 10)

        check_member = Button(lf, text="Check Member", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"),
                              relief="groove", command=CheckMemebr)
        check_member.place(x=550, y=65)

        Book_Issued_button = Button( lf , text = "Issue this Book" , bg = '#4dff4d' , font = ("Times%New%Roman" , 20 , "bold") ,
                                  relief = "groove", command = BookIssued )
        Book_Issued_button.place( x = 120 , y = 420 )

        Back_button = Button( lf , text = "Back" , bg = '#4dff4d' , font = ("Times%New%Roman" , 20 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Back_button.place( x = 710 , y = 420 )

    def IssueBookFunc(self):
        self.root.mainloop()




r = Tk()
IssueBookClass()
r.mainloop()