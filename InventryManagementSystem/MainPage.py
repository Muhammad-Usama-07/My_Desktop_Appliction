#**********************************  LIBRARY MANAGEMENT SYSTEM  **************************
import tkinter
from tkinter import *
from tkinter import messagebox

# Creating Function for login button.
import PIL
from PIL import ImageTk, Image



def login():
    # Creating Login Condition
    if (User_name.get() == "" and passd.get() == ""):
        messagebox.showerror( "Alert" ,"Please Enter Username \n and Password" )  # First Condition (Checking weather the fields are empty)
    elif (User_name.get() == "a" and passd.get() == "b"):  # When Both are true
        exit_func()
    elif (User_name.get() == "a" and passd.get() != "b"):  # When username was true
        messagebox.showerror( "Not Correct" , "Please Enter Correct Password" )
    elif (User_name.get() != "a" and passd.get() == "b"):  # When password was true
        messagebox.showerror( "Not Correct" , "Please Enter Correct Username" )
    else:
        messagebox.showerror( "Alter" , "Enter Correct Username and password" )

def exit_func():
    r.destroy()

r = Tk()

# Color Themes
lightbluecolor = '#00d0ff'
darkbluecolor = '#05b8ea'
buttoncolor = '#00aed6'
# Creating format
r.title( 'IMS' )  # title
r.configure( bg = lightbluecolor ) # Changing backgroud colour.
r.geometry( "900x600+300+50" )  # (width X hight + from_right + from_left)) # assigning size and position to widndow
# minimum and maximum size of window.
r.minsize( 400 , 200 )
r.maxsize( 1100 , 700 )

# Creating Frame

lf1 = LabelFrame( r , text = "Welcome to Inventory Management System" , fg = "black" , bg = darkbluecolor ,
                  relief = "solid" , font = "Times%New%Roman 16 bold" , height = 550)
lf1.pack( fill = "both" , expand = TRUE , padx = 20 , pady = 20 )

# image
image = PIL.Image.open(r"Inventoryicon.png")
img = ImageTk.PhotoImage(image)
l = Label(image=img,bg=darkbluecolor)
l.place(relx=0.5, rely=0.3, anchor=CENTER)

# Creating Label in a frame

lbl = Label(lf1 , text = "User Name:" , bg = darkbluecolor , font = ("Times%New%Roman" , 18 , "italic" , "bold") )
lbl.place( relx=0.3, rely=0.5, anchor=CENTER)

lbl = Label( lf1 , text = "Password:" , bg = darkbluecolor , font = ("Times%New%Roman" , 18 , "italic" , "bold") )
lbl.place(relx=0.3, rely=0.6, anchor=CENTER )


# Creating input Fields

# Variables of password and username.
passd = StringVar()
User_name = StringVar()

Login_Name = Entry( lf1 , textvariable = User_name , width = 25 , relief = "solid" ,
                    font = ("Times%New%Roman" , 18 , "bold") ) # Creating Entry Field of username.
Login_Name.place(relx=0.6, rely=0.5, anchor=CENTER )

enter_passd = Entry( lf1 , textvariable = passd , show = "*", width = 25 , relief = "solid" ,
                     font = ("Times%New%Roman" , 18 , "bold") )
enter_passd.place(relx=0.6, rely=0.6, anchor=CENTER)

# Login Button

submit_Button = Button( lf1 , text = "Sign in", bg = buttoncolor , font = ("Times%New%Roman" , 18 , "bold") ,
                        relief = "groove", command = login)
submit_Button.place( relx=0.4, rely=0.8, anchor=CENTER )
#submit_Button.bind('<Enter>', login)

Leave_Button = Button( lf1 , text = "Leave it", bg = buttoncolor , font = ("Times%New%Roman" , 18 , "bold") ,
                        relief = "groove", command = exit_func)
Leave_Button.place( relx=0.6, rely=0.8, anchor=CENTER )

#Leave_Button.bind('<Enter>', exit_func)

r.mainloop()