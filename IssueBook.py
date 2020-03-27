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
            if (Book_ISBN_var.get() == 0 and Member_code_var.get() == 0):
                messagebox.showerror( "Warning" , "Please Enter ISBN and code of member" )
            else:
                pass

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

        Titles = "          Code" + "                       Member Name" + "                     age" \
                  + "                         Vali: Year" + "                     Telephone NO:"
        dash = "          *******" + "                       ******************" + "                  ********" \
               + "                       ***********" + "                      ******************"
        Detail = Listbox(lf, width=90, height=15, relief="solid", yscrollcommand=scroll_Bar.set,
                              font=("Times%New%Roman", 12, "bold italic"))
        Detail.place(x=10, y=120)
        Detail.insert(0, Titles)
        Detail.insert(1, dash)

        scroll_Bar.config(command=Detail.yview)

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