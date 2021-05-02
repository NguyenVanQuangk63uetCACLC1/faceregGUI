import tkinter
from tkinter import *
from PIL import Image,ImageTk
import PIL.Image
import PIL.ImageTk
import cv2

from main import updateFrame

class GUI:
    def updateFrame(self,video):
        self.video = video
        global canvas, photo
        # Đọc từ Camera
        ret, frame = video.read()
        # Resize
        frame = cv2.resize(frame, dsize=None, fx=0.5, fy=0.5)
        # Chuyển hệ màu
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert thành ImageTk
        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        # Show lên
        canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
        self.root.after(15, updateFrame)

    def __init__(self,root):
        # Khởi tạo cửa sổ và background
        self.root=root
        self.root.title("Phần mềm điểm danh")
        self.root.resizable(False,False)
        self.root.geometry("500x600")
        self.root.iconbitmap("Image/UET-logo.ico")
        self.bg_loading = Image.open("Image/background.jpg")
        self.bg_render = ImageTk.PhotoImage(self.bg_loading)
        self.bg = Label(self.root, image=self.bg_render)
        self.bg.place(x=00, y=00)
        # Khởi tạo camera
        self.video = cv2.VideoCapture(0)
        self.canvas_w = self.video.get(cv2.CAP_PROP_FRAME_WIDTH) // 2.5
        self.canvas_h = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT) // 2.5
        self.canvas = Canvas(self.root, width=self.canvas_w, height=self.canvas_h, bg="#EEDD2F")
        self.canvas.pack(pady=10)
        self.photo=None

        #Camera
        updateFrame(self,self.video)

        # Dòng Note
        note_lbl = Label(self.root, text="Please look directly at the camera ", font=("Goudy old style", 15, "italic"),fg="#d77337")
        note_lbl.place(x=125, y=206.5)

        # Frame INFORMATION
        frame_info = Frame(self.root, bg="white")
        frame_info.place(x=80, y=250, height=300, width=350)
        frame_title = Label(frame_info, text="Information", font=("Impact", 30, "bold"), fg="#d77337",
                            bg="white").place(x=30, y=30)
        desc = Label(frame_info, text="Time deals gently only with those who take it gently")
        desc.config(font=("Goudy old style", 10, "bold"), fg="#d77337", bg="white")
        desc.place(x=30, y=80)
        lbl_username = Label(frame_info, text="Name", font=("Goudy old style", 13, "bold"), bg="white",
                             fg="gray").place(x=30, y=110)
        txt_username = Entry(frame_info, font=("times new roman", 15,"italic"), bg="light gray")
        txt_username.place(x=30, y=135, width=250, height=30)
        lbl_id = Label(frame_info, text="ID", font=("Goudy old style", 13, "bold"), bg="white", fg="gray").place(x=30,
                                                                                                                 y=165)
        txt_id = Entry(frame_info, font=("times new roman", 15), bg="light gray")
        txt_id.place(x=30, y=190, width=250, height=30)
        lbl_attendanceTime = Label(frame_info, text="Attendance Time", font=("Goudy old style", 13, "bold"), bg="white",
                                   fg="gray").place(x=30, y=220)
        txt_attendanceTime = Entry(frame_info, font=("times new roman", 15), bg="light gray")
        txt_attendanceTime.place(x=30, y=245, width=250, height=30)

        # Nút Export
        export_btn = Button(self.root, text="Export", font=("times new roman", 13), fg="white", bg="#d77337").place(x=225,
                                                                                                                 y=538)

root=Tk()
obj=GUI(root)
root.mainloop()


