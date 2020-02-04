from tkinter import *


class MenuPageClass:
    def __init__(self, root):

        self.root = root
        root.title( 'Module' )  # title
        root.configure( bg = '#bcdebb' )
        root.geometry( "900x600+300+50" )  # (width X hight + from_right + from_left))
        root.minsize( 400 , 200 )
        root.maxsize( 1100 , 700 )



r = Tk()

Menu_class_obj = MenuPageClass(r)
r.mainloop()