from tkinter import *
from tkinter import messagebox
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

        def MembersRemoved():
            pass

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
        scroll_Bar.place(x = 789, y = 80, height = 273)

        Members_Detail = Text(lf, width = 85, height = 15, relief = "solid" ,yscrollcommand =  scroll_Bar.set,font = ("Times%New%Roman" , 12 , "bold italic"))
        Members_Detail.place(x = 20, y = 80)
        scroll_Bar.config( command = Members_Detail.yview )

        '''Buttons
           ********'''

        Remove_Member_button = Button( lf , text = "Remove this member" , bg = '#4dff4d' , font = ("Times%New%Roman" , 17 , "bold") ,
                                  relief = "groove"
                                  , command = MembersRemoved )
        Remove_Member_button.place( x = 120 , y = 400 )

        Back_button = Button( lf , text = "Back" , bg = '#4dff4d' , font = ("Times%New%Roman" , 17 , "bold") ,
                              relief = "groove"
                              , command = self.root.destroy )
        Back_button.place( x = 710 , y = 400 )

    def RemoveMemberFunc(self):
        self.root.mainloop()



r = Tk()
RemoveMemberClass()

r.mainloop()