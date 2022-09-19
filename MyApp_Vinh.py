# CODYGYM 2022
# Học viên : Nguyễn Văn Vinh
# Sản phẩm : Ứng dụng python cuối khóa học
# MUSIC PLAYER Pro Max

import os
import tkinter as tk
from tkinter import *
from tkinter import Tk, filedialog, messagebox
from pygame import mixer
from PIL import Image, ImageTk

app = Tk()
app.title('MUSIC PLAYER Pro Max')
app.geometry('820x500')
app.config(bg='#D3FFCE')
app.resizable(0, 0)
text1 = Label(app, text='MUSIC PLAYER Pro Max\nby vinhhd68@gmail.com\nCopyright Codygym 2022',
              font=('Cambria', 25), bg='#D3FFCE')
text1.place(x=190, y=18)

img1 = Image.open('images/G_open2.png')
img2 = Image.open('images/G_play.png')
img3 = Image.open('images/G_next.png')
img4 = Image.open('images/G_previous.png')
img5 = Image.open('images/G_stop.png')
img6 = Image.open('images/CG.jpg')
img7 = Image.open('images/vinhB256.jpg')
img1rs = img1.resize((60, 60), Image.ANTIALIAS)
img1get = ImageTk.PhotoImage(img1rs)
img2rs = img2.resize((80, 80), Image.ANTIALIAS)
img2get = ImageTk.PhotoImage(img2rs)
img3next0 = img3.resize((60, 60), Image.ANTIALIAS)
img3next = ImageTk.PhotoImage(img3next0)
img4pre0 = img4.resize((60, 60), Image.ANTIALIAS)
img4pre = ImageTk.PhotoImage(img4pre0)
img5stop0 = img5.resize((60, 60), Image.ANTIALIAS)
img5stop = ImageTk.PhotoImage(img5stop0)
img6CG0 = img6.resize((120, 120), Image.ANTIALIAS)
img6CG = ImageTk.PhotoImage(img6CG0)
img70 = img7.resize((120, 120), Image.ANTIALIAS)
img7 = ImageTk.PhotoImage(img70)

mixer.init()
Frame_music = Frame(app, relief=RIDGE)
Frame_music.place(x=220, y=150, width=265, height=300)
Playlist = Listbox(Frame_music, width=40, height=17)
Playlist.place(x=10, y=10)


def Add_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith('.mp3'):
                Playlist.insert(END, song)


def Play_music():
    Music_name = Playlist.get(ACTIVE)
    print(Music_name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


def Stop_music():
    Music_name = Playlist.get(ACTIVE)
    print(Music_name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.pause()


def Next_music():
    for songindex in Playlist.curselection():
        nextSongIndex = songindex + 1
    Playlist.activate(nextSongIndex)
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    Playlist.select_clear(0, END)


def Pre_music():
    for songindex in Playlist.curselection():
        nextSongIndex = songindex - 1
    Playlist.activate(nextSongIndex)
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    Playlist.select_clear(0, END)


def show_info():
    messagebox.showinfo('Codegym online 2022',
                        'Sản phẩm của học viên vinhhd68@gmail.com\nsau khóa học Python cơ bản 2022')


def show_avatar():
    messagebox.showinfo('Học viên vinhhd68@gmail.com',
                        'Gà lập trình python\nSở thích: nghe nhạc Tuấn Hưng')


GET = Button(app, image=img1get, command=Add_music, border='0')
GET.place(x=630, y=170)
PLAY = Button(app, image=img2get, command=Play_music, border='0')
PLAY.place(x=620, y=250)
NEXT = Button(app, image=img3next, command=Next_music,  border='0')
NEXT.place(x=720, y=260)
PRE = Button(app, image=img4pre, command=Pre_music, border='0')
PRE.place(x=540, y=260)
STOP = Button(app, image=img5stop, command=Stop_music,  border='0')
STOP.place(x=630, y=350)
CG = Button(app, image=img6CG, command=show_info)
CG.place(x=45, y=305)
AVATAR = Button(app, image=img7, command=show_avatar)
AVATAR.place(x=45, y=165)

app.mainloop()
