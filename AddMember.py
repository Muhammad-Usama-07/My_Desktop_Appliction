from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
class AddMemberClass():
    def __init__(self):
        self.root = Tk()
        self.root.title( 'Add Member' )
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

        def MemberAdded():
            mc = member_code_variable_entry.get()
            mv = member_validity_variable_entry.get()
            mt = member_telephoneNo_variable_entry.get()
            mn = new_member_variable_entry.get()
            ma = Member_age_variable_entry.get()
            if (mn == "" and mc == 0 and mt == 0):
                messagebox.showerror( "Warning" , "Please Enter Name , code, \nand telephone number  at least" )

            else:
                try:
                    con = mysql.connect(host="localhost", user="root", password="", database="lib_db")
                    cursor = con.cursor()
                    cursor.execute("insert into members values('" + mc + "','" + mn + "','" + ma + "','" + mv + "','" + mt + "')")
                    cursor.execute("commit")
                    member_code_variable_entry.delete(0, 'end')
                    Member_age_variable_entry.delete(0, 'end')
                    new_member_variable_entry.delete(0, 'end')
                    member_validity_variable_entry.delete(0, 'end')
                    member_telephoneNo_variable_entry.delete(0, 'end')
                    messagebox.showinfo("Insert status", " Data insert successfully")
                    con.close()
                except mysql.errors.IntegrityError:
                    messagebox.showerror('Warning', 'insert another isbn')

        # Labels
        new_member_name_Label = Label( lf , text = "Enter name of new member:" , bg = "#33ff9e" ,
                                       anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        new_member_name_Label.place( x = 20 , y = 20 )

        member_age_Label = Label( lf , text = "Enter member's age: " , bg = "#33ff9e" ,
                                  anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        member_age_Label.place( x = 90 , y = 80 )

        Validity_year_Label = Label( lf , text = "Enter Validity in years: " , bg = "#33ff9e" ,
                                     anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Validity_year_Label.place( x = 70 , y = 140 )

        Member_telephoneNo_Label = Label( lf , text = "Enter telephone No: " , bg = "#33ff9e" ,
                                          anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Member_telephoneNo_Label.place( x = 95 , y = 200 )

        Member_code_Label = Label( lf , text = "Enter any Code of member: " , bg = "#33ff9e" ,
                                   anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Member_code_Label.place( x = 20 , y = 260 )

        # Entries
        # ********

        new_member_variable_entry = Entry( lf , width = 25 , relief = "solid" ,
                                           font = ("Times%New%Roman" , 15 , "bold") )
        new_member_variable_entry.place( x = 300 , y = 30 )

        Member_age_variable_entry = Entry( lf , width = 25 , relief = "solid" ,
                                           font = ("Times%New%Roman" , 15 , "bold") )
        Member_age_variable_entry.place( x = 300 , y = 90 )

        member_validity_variable_entry = Entry( lf  , width = 25 ,
                                                relief = "solid" ,
                                                font = ("Times%New%Roman" , 15 , "bold") )
        member_validity_variable_entry.place( x = 300 , y = 150 )

        member_telephoneNo_variable_entry = Entry( lf , width = 25 ,
                                                   relief = "solid" ,
                                                   font = ("Times%New%Roman" , 15 , "bold") )
        member_telephoneNo_variable_entry.place( x = 300 , y = 210 )

        member_code_variable_entry = Entry( lf , width = 25 , relief = "solid" ,
                                            font = ("Times%New%Roman" , 15 , "bold") )
        member_code_variable_entry.place( x = 300 , y = 270 )

        Add_Member_button = Button( lf , text = "Add member" , bg = '#4dff4d' ,
                                    font = ("Times%New%Roman" , 20 , "bold") , relief = "groove"
                                    , command = MemberAdded )
        Add_Member_button.place( x = 120 , y = 350 )

        Back_button = Button( lf , text = "Back" , bg = '#4dff4d' , font = ("Times%New%Roman" , 20 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Back_button.place( x = 710 , y = 350 )
    def AddMemberFunc(self):
        self.root.mainloop()



'''r = Tk()
AddMemberClass()

r.mainloop()'''