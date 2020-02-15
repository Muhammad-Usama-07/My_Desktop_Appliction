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

        lf = LabelFrame( self.root , text = "Enter your Choice" , fg = "red" , bg = '#33ff9e' ,
                         relief = "solid" , font = "Times%New%Roman 16 bold" , height = 550 )
        lf.pack( fill = "both" , expand = True , padx = 20 , pady = 20 )

        '''Functions
          ***********'''


        '''Labels'''


        '''Entries
          ********'''
        '''Button
           ******'''
        List_All_books_button = Button( lf , text = "All books" , bg = '#4dff4d' ,
                                     font = ("Times%New%Roman" , 17 , "bold") ,
                                     relief = "groove")
        List_All_books_button.place( x = 100 , y = 60)

        Search_for_book_button = Button( lf , text = "Search" , bg = '#4dff4d' ,
                                        font = ("Times%New%Roman" , 17 , "bold") ,
                                        relief = "groove" )
        Search_for_book_button.place( x = 700 , y = 60 )

        Back_button = Button( lf , text = "Back" , bg = '#4dff4d' , font = ("Times%New%Roman" , 17 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Back_button.place( x = 710 , y = 400 )



    def ListBookIssueFunc(self):
        self.root.mainloop()




r = Tk()
obj = ListBookIssueClass()
r.mainloop()