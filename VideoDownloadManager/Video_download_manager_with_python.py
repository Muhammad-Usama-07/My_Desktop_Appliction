from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar
from pytube import *
from pytube import YouTube
from tqdm import tqdm
import time


root = Tk()
root.title('Video Download Manager ')
root.geometry("900x350+300+50")
root.minsize(400, 200)
root.maxsize(1100, 700)
root.configure(bg='#0F5CD6')
Label(root, text=" Welcome to my Video Downloader", bg="#6A91CF",
      relief="solid",
      anchor="w", height=2, font="Times%New%Roman 11 bold italic").pack(fill=X)

lf = LabelFrame(root, text="Download Panel", fg="red", bg='#6A91CF',
                relief="solid", font="Times%New%Roman 16 bold", height=370)
lf.pack(fill="both", padx=20, pady=20)

"""Variables
   *********"""
link_address_var = StringVar()
yt = StringVar()
a = StringVar()
'''Functions
  ************'''
def download_complete(stream = None, file_handle =  None):
    messagebox.showinfo('Completion', 'Your Video has been downloaded')
def download():

    # getting youtube link
    link = link_address_var.get()
    yt = YouTube(link, on_complete_callback=download_complete)

    # getting qualities
    videos = yt.streams.filter(subtype='mp4', progressive=True, res="360p")
    print(videos)
    vid = videos[0]
    # getting Path of video
    path = save_entry.get()
    vid.download(path)
    #print("your file: '{}'\nhas been downloaded...:)".format(yt.title))
    return

def save_path():
    file = filedialog.askdirectory()
    if file is None:
        print("Any name is required")
    save_entry.insert(0,file)
    print("Your Selected Location is: "+file)



# Labels

link_address_Label = Label(lf, text="Link Address: ", bg="#6A91CF",
                           anchor="w", height=2, font=("Times%New%Roman", 12, "bold italic"))
link_address_Label.place(x=20, y=20)

Quality_Label = Label(lf, text="your Location: ", bg="#6A91CF",
                      anchor="w", height=2, font=("Times%New%Roman", 12, "bold italic"))
Quality_Label.place(x=20, y=70)

'''Progress_Label = Label(lf, text="Progress: ", bg="#33ff9e",
                      anchor="w", height=2, font=("Times%New%Roman", 12, "bold italic"))
Progress_Label.place(x=30, y=200)'''

'''Entries
  ********'''


link_address_entry = Entry(lf,  textvariable = link_address_var,width=55, relief="solid",
                           font=("Times%New%Roman", 13))
link_address_entry.place(x=140, y=30)
save_entry = Entry(lf,width=55, relief="solid",
                           font=("Times%New%Roman", 13))
save_entry.place(x=140, y=78)

'''Progress Bar
  ******** 
progbar = Progressbar(lf,  orient = HORIZONTAL,
              length = 790, mode = 'determinate')
progbar.place(x = 30, y = 240)'''

'''Button
  ******** '''
save_button = Button(lf, text="Select Location", bg='#0F5CD6', font=("Times%New%Roman", 15, "bold"),
                     relief="groove", command=save_path)
save_button.place(x=660, y=75)

download_button = Button(lf, text="Download", bg='#0F5CD6', font=("Times%New%Roman", 15, "bold"),
                         relief="groove", command = download)
download_button.place(x=300, y=130)




root.mainloop()


