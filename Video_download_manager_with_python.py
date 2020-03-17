from tkinter import *
from tkinter import messagebox
class VDM():
    def __init__(self):
        self.root = Tk()
        self.root.title( 'Video Download Manager ' )
        self.root.geometry( "900x600+300+50" )
        self.root.minsize( 400 , 200 )
        self.root.maxsize( 1100 , 700 )
        self.root.configure( bg = '#bcdebb' )
        Label( self.root , text = " Welcome to my Video Downloader" , bg = "#66bd6d" ,
               relief = "solid" ,
               anchor = "w" , height = 2 , font = "Times%New%Roman 11 bold italic" ).pack(fill = X)

        lf = LabelFrame(self.root, text="Whatr you want", fg="red", bg='#33ff9e',
                        relief="solid", font="Times%New%Roman 16 bold", height=550)
        lf.pack(fill="both", expand=True, padx=20, pady=20)

        # Labels

        link_address_Label = Label(lf, text="Enter Your Link Address: ", bg="#33ff9e",
                                anchor="w", height=2, font=("Times%New%Roman", 12, "bold italic"))
        link_address_Label.place(x=20, y=20)

        Quality_Label = Label(lf, text="Select Quality: ", bg="#33ff9e",
                                   anchor="w", height=2, font=("Times%New%Roman", 12, "bold italic"))
        Quality_Label.place(x=20, y=70)

        '''Quality Menu
           ************'''

        items = ["one","two","three","four" ]
        select_resolution_var = StringVar()
        select_resolution_var.set(items[0])

        select_resolution = OptionMenu(lf,select_resolution_var, *items)
        select_resolution.config(width = 90,relief="solid",font=("Times%New%Roman", 8),
                                                                            bd = 1.3)
        select_resolution.place(x=220, y=80)

        '''Entries
          ********'''

        link_address_entry = Entry(lf, width=55, relief="solid",
                                      font=("Times%New%Roman", 13))
        link_address_entry.place(x=220, y=30)

        '''Button
          ******** '''
        save_button = Button(lf, text="Save to", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"),
                                 relief="groove")
        save_button.place(x=750, y=20)

        download_button = Button(lf, text="Download", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"),
                                 relief="groove")
        download_button.place(x=700, y=130)






r = Tk()
VDM()
r.mainloop()