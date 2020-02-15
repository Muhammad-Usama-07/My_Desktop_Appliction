from tkinter import *
from tkinter import messagebox
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
            if (new_member_variable.get() == "" and Member_code_Label.get() == 0):
                messagebox.showerror( "Warning" , "Please Enter Name and code at least" )
                if ():
                    pass

            else:
                messagebox.showerror( "Alter" , "Enter Correct Username and password" )

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

        new_member_variable = StringVar()
        new_member_variable_entry = Entry( lf , textvariable = new_member_variable , width = 25 , relief = "solid" ,
                                           font = ("Times%New%Roman" , 15 , "bold") )
        new_member_variable_entry.place( x = 300 , y = 30 )

        Member_age_variable = IntVar()
        Member_age_variable_entry = Entry( lf , textvariable = Member_age_variable , width = 25 , relief = "solid" ,
                                           font = ("Times%New%Roman" , 15 , "bold") )
        Member_age_variable_entry.place( x = 300 , y = 90 )

        member_validity_variable = IntVar()
        member_validity_variable_entry = Entry( lf , textvariable = member_validity_variable , width = 25 ,
                                                relief = "solid" ,
                                                font = ("Times%New%Roman" , 15 , "bold") )
        member_validity_variable_entry.place( x = 300 , y = 150 )

        member_telephoneNo_variable = IntVar()
        member_telephoneNo_variable_entry = Entry( lf , textvariable = member_telephoneNo_variable , width = 25 ,
                                                   relief = "solid" ,
                                                   font = ("Times%New%Roman" , 15 , "bold") )
        member_telephoneNo_variable_entry.place( x = 300 , y = 210 )

        member_code_variable = IntVar()
        member_code_variable_entry = Entry( lf , textvariable = member_code_variable , width = 25 , relief = "solid" ,
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
obj = AddMemberClass(r)
obj.AddMemberFunc()
r.mainloop()'''