from tkinter import *
from tkinter import filedialog
import pytube
from pytube import YouTube
import os
import sys

root = Tk()
root.title('Video Download Manager ')
root.geometry("900x400+300+50")
root.minsize(400, 200)
root.maxsize(1100, 700)
root.configure(bg='#bcdebb')
Label(root, text=" Welcome to my Video Downloader", bg="#66bd6d",
      relief="solid",
      anchor="w", height=2, font="Times%New%Roman 11 bold italic").pack(fill=X)

lf = LabelFrame(root, text="Whatr you want", fg="red", bg='#33ff9e',
                relief="solid", font="Times%New%Roman 16 bold", height=370)
lf.pack(fill="both", padx=20, pady=20)

"""Variables
   *********"""
link_address_var = StringVar()

'''Functions
  ************'''
def download():
    # Select youtube link you want to upload and print contents
    link = link_address_var.get()
    yt = YouTube(link)

def save_path():
    filename = filedialog.askdirectory()
    if filename is None:
        print("Any name is required")


# Labels

link_address_Label = Label(lf, text="Link Address: ", bg="#33ff9e",
                           anchor="w", height=2, font=("Times%New%Roman", 12, "bold italic"))
link_address_Label.place(x=20, y=20)

Quality_Label = Label(lf, text="your Location: ", bg="#33ff9e",
                      anchor="w", height=2, font=("Times%New%Roman", 12, "bold italic"))
Quality_Label.place(x=20, y=70)

'''Entries
  ********'''


link_address_entry = Entry(lf,  textvariable = link_address_var,width=55, relief="solid",
                           font=("Times%New%Roman", 13))
link_address_entry.place(x=140, y=30)
save_entry = Entry(lf,width=55, relief="solid",
                           font=("Times%New%Roman", 13))
save_entry.place(x=140, y=78)

'''Button
  ******** '''
save_button = Button(lf, text="Select Location", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"),
                     relief="groove", command=save_path)
save_button.place(x=660, y=75)

download_button = Button(lf, text="Download", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"),
                         relief="groove", command = download)
download_button.place(x=300, y=130)


root.mainloop()


