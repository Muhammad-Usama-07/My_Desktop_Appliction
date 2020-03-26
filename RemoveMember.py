from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
class RemoveMemberClass():
    def __init__(self):
        self.root = Tk()
        self.root.title( 'Remove Member' )
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
            rmm = Remove_Members_entry.get()
            if (rmm == 0):
                messagebox.showerror("Warning", "Please Enter ISBN at least")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="lib_db")
                cursor = con.cursor()
                cursor.execute("select *  from Book where ISBN='" + rmm + "'")
                rows = cursor.fetchall()
                for row in rows:
                    insertdata = "            " + str(row[0]) + '                           ' + row[1] + \
                                 '                                   ' + row[2] + '                                ' + row[3] + \
                                 '                                ' + str(row[4])
                    Members_Detail.insert(Members_Detail.size() + 1, insertdata)
                con.close()
        def MembersRemoved():
            rm = Remove_Members_entry.get()
            if (rm == 0):
                messagebox.showerror("Warning", "Please Enter ISBN at least")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="lib_db")
                cursor = con.cursor()
                cursor.execute("delete from Members where Code='" + rm + "'")
                cursor.execute("commit")
                Remove_Members_entry.delete(0, 'end')
                messagebox.showinfo("Delete status", " Data Deleted successfully")
                con.close()

        '''Labels
          ********'''
        Remove_Members_name_Label = Label( lf , text = "Enter name of Member:" , bg = "#33ff9e" ,
                                        anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Remove_Members_name_Label.place( x = 20 , y = 20 )


        '''Entries
           ********'''
        Remove_Members_var = StringVar()
        Remove_Members_entry = Entry( lf , textvariable = Remove_Members_var , width = 25 , relief = "solid" ,
                                           font = ("Times%New%Roman" , 15 , "bold") )
        Remove_Members_entry.place( x = 250 , y = 30 )

        #Creating ScrollBar

        scroll_Bar = Scrollbar(lf, width = 25, relief = "solid")
        scroll_Bar.place(x = 789, y = 80, height = 250)
        Details = "          Code" + "                       Member Name" + "                     age" \
                  + "                         Vali: Year" + "                     Telephone NO:"
        dash = "          *******" + "                       ******************" + "                  ********" \
               + "                       ***********" + "                      ******************"
        Members_Detail = Listbox(lf, width=85, height=13, relief="solid", yscrollcommand=scroll_Bar.set,
                              font=("Times%New%Roman", 12, "bold italic"))
        Members_Detail.place(x=20, y=80)
        Members_Detail.insert(0, Details)
        Members_Detail.insert(1, dash)
        scroll_Bar.config( command = Members_Detail.yview )

        '''Buttons
           ********'''

        Remove_Member_button = Button( lf , text = "Remove this member" , bg = '#4dff4d' , font = ("Times%New%Roman" , 17 , "bold") ,
                                  relief = "groove"
                                  , command = MembersRemoved )
        Remove_Member_button.place( x = 120 , y = 400 )

        Search_button = Button(lf, text="Search", bg='#4dff4d', font=("Times%New%Roman", 17, "bold"),
                               relief="groove"
                               , command=Search)
        Search_button.place(x=540, y=20)

        Back_button = Button( lf , text = "Back" , bg = '#4dff4d' , font = ("Times%New%Roman" , 17 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Back_button.place( x = 710 , y = 400 )

    def RemoveMemberFunc(self):
        self.root.mainloop()



r = Tk()
RemoveMemberClass()

r.mainloop()