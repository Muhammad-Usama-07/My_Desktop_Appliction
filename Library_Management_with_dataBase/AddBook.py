from tkinter import *
class AddBookClass:
    def __init__(self, root):
        self.root = root
    def AddBookFunc(self):
        self.root.title( 'Add Book' )
        self.root.geometry( "900x600+300+50" )
        self.root.minsize( 400 , 200 )
        self.root.maxsize( 1100 , 700 )
        self.root.configure( bg = '#bcdebb' )
        Label( self.root , text = " Note: Here you can make your study perfect... :) " , bg = "#66bd6d" , relief = "solid" ,
               anchor = "w" , height = 2 , font = "Times%New%Roman 11 bold italic" ).pack()

        lf = LabelFrame( self.root , text = "Fill the Details" , fg = "red" , bg = '#33ff9e' ,
                         relief = "solid" , font = "Times%New%Roman 16 bold" , height = 550 )
        lf.pack( fill = "both" , expand = True , padx = 20 , pady = 20 )

        # Labels
        new_ISBN_number_Label = Label( lf , text = "Write new ISBN of the book:" , bg = "#33ff9e" ,
                                     anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        new_ISBN_number_Label.place( x = 30 , y = 20 )

        new_book_name_Label = Label( lf , text = "Enter Book Name: " , bg = "#33ff9e" ,
                                     anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        new_book_name_Label.place( x = 30 , y = 90 )

        Book_auther_Label = Label( lf , text = "Enter Book Auther: " , bg = "#33ff9e" ,
                                   anchor = "w" , height = 2 , font = ("Times%New%Roman" , 14 , "bold italic") )
        Book_auther_Label.place( x = 30 , y = 150 )

        # Entries

        new_ISBN_number = StringVar()
        new_ISBN_number_entry = Entry( lf , textvariable = new_ISBN_number , width = 25 , relief = "solid" ,
                                     font = ("Times%New%Roman" , 15 , "bold") )
        new_ISBN_number_entry.place( x = 300 , y = 30 )

        new_book_name = StringVar()
        new_book_name_entry = Entry( lf , textvariable = new_book_name , width = 25 , relief = "solid" ,
                                     font = ("Times%New%Roman" , 15 , "bold") )
        new_book_name_entry.place( x = 215 , y = 100 )

        new_book_auther_name = StringVar()
        new_book_auther_entry = Entry( lf , textvariable = new_book_auther_name , width = 25 , relief = "solid" ,
                                       font = ("Times%New%Roman" , 15 , "bold") )
        new_book_auther_entry.place( x = 215 , y = 160 )

        next_button = Button( lf , text = "Back" , bg = '#4dff4d' , font = ("Times%New%Roman" , 15 , "bold")
                              , command = self.root.destroy )
        next_button.place( x = 750 , y = 450 )


r = Tk()
obj = AddBookClass(r)
obj.AddBookFunc()
r.mainloop()