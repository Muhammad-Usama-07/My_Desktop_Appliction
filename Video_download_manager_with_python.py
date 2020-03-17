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





r = Tk()
VDM()
r.mainloop()