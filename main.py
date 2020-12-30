from tkinter import *
import datetime
import sys
import os
import pytube

root = Tk()
root.title('YouTube Downloader')
# root.iconbitmap('favicon.ico')
root.geometry("1000x400")

my_menu = Menu(root)
root.config(menu=my_menu)


def paste_url():
    if len(url_get.get()) == 0:
        url_get.event_generate('<<Paste>>')
        paste_btn['state'] = DISABLED
    else:
        error_text = Label(mainFrame, text="Some URL already present!")
        error_text.grid(row=4, column=1, columnspan=4, sticky=N+E+S+W)
        paste_btn['state'] = DISABLED


# def analyse_video():
#     video = pytube.YouTube(url_get.get())
#     x = 5
#     for stream in video.streams:
#         # print(stream)
#         url = Label(mainFrame, text=stream)
#         url.grid(row=x, column=1, columnspan=4, sticky=N+E+S+W)
#         x += 1


def download_720():
    # 22
    downloading_txt = Label(mainFrame, text="Downloading in 720p...")
    downloading_txt.grid(row=5, column=1, columnspan=4, sticky=N+E+S+W)
    video = pytube.YouTube(url_get.get())
    stream = video.streams.get_by_itag(22)
    stream.download()
    success_txt = Label(mainFrame, text="Download Complete: " + video.title)
    success_txt.grid(row=6, column=1, columnspan=4, sticky=N+E+S+W)


def download_360():
    # 18
    downloading_txt = Label(mainFrame, text="Downloading in 360p...")
    downloading_txt.grid(row=5, column=1, columnspan=4, sticky=N+E+S+W)
    video = pytube.YouTube(url_get.get())
    stream = video.streams.get_by_itag(18)
    stream.download()
    success_txt = Label(mainFrame, text="Download Complete: " + video.title)
    success_txt.grid(row=6, column=1, columnspan=4, sticky=N+E+S+W)


def download_audio():
    # 140
    downloading_txt = Label(mainFrame, text="Downloading Audio...")
    downloading_txt.grid(row=5, column=1, columnspan=4, sticky=N+E+S+W)
    video = pytube.YouTube(url_get.get())
    stream = video.streams.get_by_itag(140)
    stream.download()
    success_txt = Label(mainFrame, text="Download Complete: " + video.title)
    success_txt.grid(row=6, column=1, columnspan=4, sticky=N+E+S+W)


def new_download():
    python = sys.executable
    os.execl(python, python, * sys.argv)


# Header
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New Download', command=new_download)
file_menu.add_command(label='Exit', command=root.quit)


# Main Body - Download
mainFrame = LabelFrame(root, padx=10, pady=10)
mainFrame.pack(padx=10, pady=60)

title_label = Label(mainFrame, text="Download Video")
url_label = Label(mainFrame, text="Enter URL:")
url_get = Entry(mainFrame, width=50)
paste_btn = Button(mainFrame, text="Paste URL", command=paste_url)
# analyse_video = Button(mainFrame, text="Analyse", command=analyse_video)
download_720 = Button(mainFrame, text="Download 720p",
                      command=download_720)
download_360 = Button(mainFrame, text="Download 360p",
                      command=download_360)
download_audio = Button(mainFrame, text="Download Audio",
                        command=download_audio)

title_label.config(font=("Courier", 44))
title_label.grid(row=0, column=1, columnspan=4, sticky=N+E+S+W)
url_label.grid(row=1, column=0)
url_get.grid(row=1, column=1, columnspan=4, sticky=N+E+S+W)
paste_btn.grid(row=1, column=5)
download_720.grid(row=2, column=1, pady=10)
download_360.grid(row=2, column=2)
download_audio.grid(row=2, column=3)
# analyse_video.grid(row=3, column=3)

# Footer
now = datetime.datetime.now()
status = Label(root, text="Copyright © " + str(now.year) + " All rights reserved | Developed By Priyansh Thakar",
               bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
