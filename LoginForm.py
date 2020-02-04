from tkinter import *


r = Tk()
# Creating format
r.title( 'Module' )  # title
r.configure( bg = '#bcdebb' ) # Changing backgroud colour.
r.geometry( "900x600+300+50" )  # (width X hight + from_right + from_left)) # assigning size and position to widndow
# minimum and maximum size of window.
r.minsize( 400 , 200 )
r.maxsize( 1100 , 700 )
r.iconbitmap( r'model_icon.ico' ) #
Label( r , text = " Note: Here you can make your study perfect... :) " , bg = "#66bd6d" , relief = "solid" ,
       anchor = "w" , height = 2 , font = "Times%New%Roman 11 bold italic" ).pack( side = TOP , fill = X ) # Creating a top highlight lable
r.mainloop()