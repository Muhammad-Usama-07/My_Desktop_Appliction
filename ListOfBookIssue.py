from tkinter import *
from tkinter import messagebox
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

        lf1 = LabelFrame( self.root , text = "List of all Books" , fg = "red" , bg = '#33ff9e' ,
                         relief = "solid" , font = "Times%New%Roman 16 bold" )
        lf1.place(x = 5, y = 60, height = 150, width = 440)

        lf2 = LabelFrame( self.root , text = "Search for Specific Books" , fg = "red" , bg = '#33ff9e' ,
                          relief = "solid" , font = "Times%New%Roman 16 bold" )
        lf2.place( x = 445 , y = 60 , height = 150 , width = 450 )

        lf3 = Frame( self.root , bg = '#33ff9e' , highlightcolor="black", highlightbackground="black", highlightthickness = 2)
        lf3.place( x = 5 , y = 210 , height = 380 , width = 890 )

        '''Functions
          ***********'''


        '''Entries
          ********'''
        Book_name = StringVar()
        Book_name_entry = Entry( lf2 , textvariable = Book_name , width = 25 , relief = "solid" ,
                                       font = ("Times%New%Roman" , 15 , "bold") )
        Book_name_entry.place( x = 40 , y = 40 )

        '''Button
           ******'''
        List_All_books_button = Button( lf1 , text = "All books" , bg = '#4dff4d' ,
                                     font = ("Times%New%Roman" , 17 , "bold") ,
                                     relief = "groove")
        List_All_books_button.place( x = 280 , y = 30)

        Search_for_book_button = Button( lf2 , text = "Search" , bg = '#4dff4d' ,
                                        font = ("Times%New%Roman" , 17 , "bold") ,
                                        relief = "groove" )
        Search_for_book_button.place( x = 340 , y = 30 )

        Back_button = Button( lf3 , text = "Back" , bg = '#4dff4d' , font = ("Times%New%Roman" , 17 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Back_button.place( x = 790 , y = 300 )

        '''
        Text Field
        **********
        '''

        '''
        Scroll Bar
        *********
        '''
        scroll_Bar = Scrollbar( lf3 , width = 25 , relief = "solid" )
        scroll_Bar.place( x = 654 , y = 10 , height = 340 )

        Book_Details = Text( lf3 , width = 80 , height = 21 , relief = "solid" ,yscrollcommand =  scroll_Bar.set)
        Book_Details.place( x = 10 , y = 10 )

        scroll_Bar.config( command = Book_Details.yview )

    def ListBookIssueFunc(self):
        self.root.mainloop()




'''r = Tk()
obj = ListBookIssueClass()
r.mainloop()'''