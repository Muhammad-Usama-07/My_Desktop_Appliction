#**********************************  LIBRARY MANAGEMENT SYSTEM  **************************


from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk
from Library_Management_project import MenuPage


r = Tk()
# Creating Function for login button.
def login():
    d = MenuPage.MenuPageClass( r )

    # Creating Login Condition
    if (User_name.get() == "" and passd.get() == ""):
        messagebox.showerror( "Alert" ,"Please Enter Username \n and Password" )  # First Condition (Checking weather the fields are empty)
    elif (User_name.get() == "a" and passd.get() == "b"):  # When Both are true
        d.MenuFunc()
        r.destroy()
    elif (User_name.get() == "a" and passd.get() != "b"):  # When username was true
        messagebox.showerror( "Not Correct" , "Please Enter Correct Password" )
    elif (User_name.get() != "a" and passd.get() == "b"):  # When password was true
        messagebox.showerror( "Not Correct" , "Please Enter Correct Username" )
    else:
        messagebox.showerror( "Alter" , "Enter Correct Username and password" )


# Creating format
r.title( 'Module' )  # title
r.configure( bg = '#bcdebb' ) # Changing backgroud colour.
r.geometry( "900x600+300+50" )  # (width X hight + from_right + from_left)) # assigning size and position to widndow
# minimum and maximum size of window.
r.minsize( 400 , 200 )
r.maxsize( 1100 , 700 )
Label( r , text = " Note: Here you can make your study perfect... :) " , bg = "#66bd6d" , relief = "solid" ,
       anchor = "w" , height = 2 , font = "Times%New%Roman 11 bold italic" ).pack( side = TOP , fill = X ) # Creating a top highlight lable

# Creating Frame

lf1 = LabelFrame( r , text = "Login Your Account" , fg = "red" , bg = '#33ff9e' ,
                  relief = "solid" , font = "Times%New%Roman 16 bold" , height = 550 )
lf1.pack( fill = "both" , expand = TRUE , padx = 20 , pady = 20 )

# Creating Label in a frame

lbl = Label(lf1 , text = "User Name:" , bg = '#33ff9e' , font = ("Times%New%Roman" , 15 , "italic" , "bold") )
lbl.place( x = 270 , y = 190 )

lbl = Label( lf1 , text = "Password:" , bg = '#33ff9e' , font = ("Times%New%Roman" , 15 , "italic" , "bold") )
lbl.place( x = 270 , y = 240 )


# Creating input Fields

# Variables of password and username.
passd = StringVar()
User_name = StringVar()

Login_Name = Entry( lf1 , textvariable = User_name , width = 25 , relief = "solid" ,
                    font = ("Times%New%Roman" , 15 , "bold") ) # Creating Entry Field of username.
Login_Name.place( x = 400 , y = 190 )

enter_passd = Entry( lf1 , textvariable = passd , show = "*", width = 25 , relief = "solid" ,
                     font = ("Times%New%Roman" , 15 , "bold") )
enter_passd.place( x = 400 , y = 240 )

# Login Button

submit_Button = Button( lf1 , text = "Sign in", bg = '#4dff4d' , font = ("Times%New%Roman" , 15 , "bold") ,
                        relief = "groove", command = login)

submit_Button.place( x = 400 , y = 310 )

r.mainloop()