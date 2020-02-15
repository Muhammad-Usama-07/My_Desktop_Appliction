from tkinter import *
from tkinter import messagebox
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

        def BookIssued():
            if ():
                pass
            else:
                messagebox.showerror( "Alter" , "Enter Correct Username and password" )

        # Labels

        Book_ISBN_Label = Label( lf , text = "Enter isbn of Book: " , bg = "#33ff9e" ,
                                    anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Book_ISBN_Label.place( x = 80 , y = 200 )

        Member_code_Label = Label( lf , text = "Enter code of member: " , bg = "#33ff9e" ,
                                     anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Member_code_Label.place( x = 70 , y = 260 )


        # Entries
        # ********



        Book_Issued_button = Button( lf , text = "Issue this Book" , bg = '#4dff4d' , font = ("Times%New%Roman" , 20 , "bold") ,
                                  relief = "groove"
                                  , command = BookIssued )
        Book_Issued_button.place( x = 120 , y = 350 )

        Back_button = Button( lf , text = "Back" , bg = '#4dff4d' , font = ("Times%New%Roman" , 20 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Back_button.place( x = 710 , y = 350 )

    def IssueBookFunc(self):
        self.root.mainloop()




r = Tk()
IssueBookClass()
r.mainloop()