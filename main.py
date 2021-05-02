
import tkinter
from tkinter import *
from PIL import Image,ImageTk
import cv2
import PIL.Image # cài đặt pillow
import PIL.ImageTk
window = Tk()
window.title("Phần mềm điểm danh")
window.resizable(False,False)
window.geometry("500x600")
window.iconbitmap("Image/UET-logo.ico")

bg_loading = Image.open("Image/background.jpg")
bg_render = ImageTk.PhotoImage(bg_loading)
bg = Label(window,image=bg_render)
bg.place(x=00,y=00)

video =cv2.VideoCapture(0)
canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH)//2.5
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT)//2.5
canvas = Canvas(window,width = canvas_w,height = canvas_h, bg ="#EEDD2F")
canvas.pack(pady = 10)

photo = None
def updateFrame():
    global canvas, photo
    # Đọc từ Camera
    ret, frame = video.read()
    # Resize
    frame = cv2.resize(frame, dsize=None, fx=0.5,fy=0.5)
    # Chuyển hệ màu
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Convert thành ImageTk
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    # Show lên
    canvas.create_image(0,0, image = photo,anchor = tkinter.NW)
    window.after(15,updateFrame)
updateFrame()

note_lbl = Label(window,text="Please look directly at the camera ",font=("Goudy old style",15,"italic"),fg="#d77337")
note_lbl.place(x=125,y=206.5)

frame_info = Frame(window,bg="white")
frame_info.place(x=80,y=250,height=300,width=350)
frame_title = Label(frame_info,text="Information",font=("Impact",30,"bold"),fg="#d77337",bg="white").place(x=30,y=30)
desc = Label(frame_info,text="Time deals gently only with those who take it gently")
desc.config(font=("Goudy old style",10,"bold"),fg="#d77337",bg="white")
desc.place(x=30,y=80)

lbl_username = Label(frame_info,text="Name",font=("Goudy old style",13,"bold"),bg ="white",fg="gray").place(x=30,y=110)
txt_username = Entry(frame_info,font=("times new roman",15),bg="light gray")
txt_username.place(x=30,y=135,width=250,height=30)

lbl_id = Label(frame_info,text="ID",font=("Goudy old style",13,"bold"),bg ="white",fg="gray").place(x=30,y=165)
txt_id = Entry(frame_info,font=("times new roman",15),bg="light gray")
txt_id.place(x=30,y=190,width=250,height=30)

lbl_attendanceTime = Label(frame_info,text="Attendance Time",font=("Goudy old style",13,"bold"),bg ="white",fg="gray").place(x=30,y=220)
txt_attendanceTime = Entry(frame_info,font=("times new roman",15),bg="light gray")
txt_attendanceTime.place(x=30,y=245,width=250,height=30)

export_btn = Button(window,text="Export",font=("times new roman",13),fg="white",bg="#d77337").place(x=225,y=538)
window.mainloop()