from tkinter import *


r = Tk()
# Creating format
r.title( 'Module' )  # title
r.configure( bg = '#bcdebb' ) # Changing backgroud colour.
r.geometry( "900x600+300+50" )  # (width X hight + from_right + from_left)) # assigning size and position to widndow
# minimum and maximum size of window.
r.minsize( 400 , 200 )
r.maxsize( 1100 , 700 )
r.iconbitmap( r'model_icon.ico' ) # assigning icon
r.mainloop()