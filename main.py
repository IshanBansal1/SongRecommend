from tkinter import *
import tkinter.messagebox
import secondary

def btn_clicked():
    playlist = entry0.get()
    ex = entry1.get()
    window.destroy()
    secondary.start(playlist_url=playlist, explicit=ex)

def btn1_clicked():
    tkinter.messagebox.showinfo("Playlist URL", "In your spotify playlist, press the three dots. Then hover over share and click Copy link to playlist to get playlist URL")

def btn2_clicked():
    tkinter.messagebox.showinfo("Explicit", "If you want explicit songs select yes, else select no")

window = Tk()

window.geometry("700x500")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    350.0, 250.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    349.5, 161.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 170, y = 132,
    width = 359,
    height = 56)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    349.5, 273.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 170, y = 244,
    width = 359,
    height = 56)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 252, y = 350,
    width = 196,
    height = 58)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn1_clicked,
    relief = "flat")

b1.place(
    x = 305, y = 96,
    width = 24,
    height = 25)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn2_clicked,
    relief = "flat")

b2.place(
    x = 384, y = 206,
    width = 24,
    height = 25)

window.resizable(False, False)
window.mainloop()
