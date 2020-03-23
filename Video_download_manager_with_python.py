from tkinter import *
from tkinter import filedialog
import pytube
import os
import sys

root = Tk()
root.title('Video Download Manager ')
root.geometry("900x600+300+50")
root.minsize(400, 200)
root.maxsize(1100, 700)
root.configure(bg='#bcdebb')
Label(root, text=" Welcome to my Video Downloader", bg="#66bd6d",
      relief="solid",
      anchor="w", height=2, font="Times%New%Roman 11 bold italic").pack(fill=X)

lf = LabelFrame(root, text="Whatr you want", fg="red", bg='#33ff9e',
                relief="solid", font="Times%New%Roman 16 bold", height=550)
lf.pack(fill="both", expand=True, padx=20, pady=20)

'''Functions
  ************'''
def download():
    pass

def save_path():
    filename = filedialog.askdirectory()
    if filename is None:
        print("Any name is required")


# Labels

link_address_Label = Label(lf, text="Enter Your Link Address: ", bg="#33ff9e",
                           anchor="w", height=2, font=("Times%New%Roman", 12, "bold italic"))
link_address_Label.place(x=20, y=20)

Quality_Label = Label(lf, text="Select Quality: ", bg="#33ff9e",
                      anchor="w", height=2, font=("Times%New%Roman", 12, "bold italic"))
Quality_Label.place(x=20, y=70)

'''Entries
          ********'''

link_address_var = StringVar()
link_address_entry = Entry(lf, width=55, relief="solid",
                           font=("Times%New%Roman", 13))
link_address_entry.place(x=220, y=30)

yt = pytube.YouTube(str(link_address_var))
videos = yt.streams.filter(subtype='mp4', progressive=True)

'''Menu
    ****'''
items = []
for v in videos:
    items.append(str(v))

select_resolution_var = StringVar()
select_resolution_var.set(items[0])

select_resolution = OptionMenu(lf, select_resolution_var, *items)
select_resolution.config(width=90, relief="solid", font=("Times%New%Roman", 8),
                         bd=1.3)
select_resolution.place(x=220, y=80)

vid = select_resolution_var.get()

filename = filedialog.askdirectory()

dest = str(os.path.dirname(filename))

if filename is None:
    print("Any name is required")
    vid.download(dest)
    print("\n Downloaded succssesfully")
    sys.exit()

'''Button
  ******** '''
save_button = Button(lf, text="Save to", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"),
                     relief="groove", command=save_path)
save_button.place(x=750, y=20)

download_button = Button(lf, text="Download", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"),
                         relief="groove", command = download)
download_button.place(x=700, y=130)





