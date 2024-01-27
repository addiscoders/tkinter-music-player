from tkinter import filedialog
from tkinter import *
import pygame
import os


root = Tk()
root.title("Amoragadal Audio Solution")

width=600
height=420

x=(root.winfo_screenwidth()//2) - (width//2)
y=(root.winfo_screenheight()//2) - (height//2)

root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root.minsize(width,height)
root.maxsize(width,height)

img = PhotoImage(file="C:\\Users\\user\\Desktop\\play.png")
root.iconphoto(False,img)

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False 

def load_music():
    global current_song
    
    root.directory = filedialog.askdirectory() 
       
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)
    for song in songs:
        songList.insert("end", song)
        
    songList.selection_set(0)
    current_song = songs[songList.curselection()[0]]       

def play_music():
    global current_song, paused
    
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global pause
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_song, paused
    
    try:
        songList.selection_clear(0, END)
        songList.selection_set(songs.index(current_song) + 1)
        current_song = songs[songList.curselection()[0]]
        play_music()
    except:
        pass
        

def previous_music():
    global current_song, paused
    
    try:
        songList.selection_clear(0, END)
        songList.selection_set(songs.index(current_song) - 1)
        current_song = songs[songList.curselection()[0]]
        play_music()
        
    except:
        pass             
    

organize_menu = Menu(menubar, tearoff=False)
organize_menu.add_command(label="Select Folder", command=load_music)
menubar.add_cascade(label="Organize", menu=organize_menu)

songList = Listbox(root, bg="black", fg="white", width="100", height="20")
songList.pack()

play_btn_image = PhotoImage(file="images/play.png")
pause_btn_image = PhotoImage(file="images/pause.png")
next_btn_image = PhotoImage(file="images/next.png")
previous_btn_image = PhotoImage(file="images/previous.png")

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command=next_music)
previous_btn = Button(control_frame, image=previous_btn_image, borderwidth=0, command=previous_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
previous_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()

