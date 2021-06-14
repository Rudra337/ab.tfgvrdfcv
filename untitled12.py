from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
 
root = Tk()
root.title("Image")
root.geometry("1100x1100")
root.configure(background="black")

image1 = Image.open("mercury.jpg")
img1 = image1.rotatation(180)
Mercury = ImageTk.PhotoImage(img1)




label_planet = Label(root, bg="black")
label_planet_name = Label(root,font=("courier",10,"bold"),bg="black")
label_planet_image = Label(root,highlightthickness=5,bg="white", borderwidth=2,relief=SOLID)
label_planet_gravity_radius = Label(root,font=("castellar"),bg="black")
label_planet_info = Label(root,font=("courier",10,"bold"),bg="black",wraplength=100)

planets = ["mercury","Venus","Earth"]
selectdeval = StringVar()
dropdown = ttk.Combobox(root, values=planets, textvariable=selectdeval)

def planetinfo():
   global Mercury
   imm = label_planet_image["image"] = Mercury
   
   
   
def rotate():
    
    imm = label_planet_image["image"] = image1
    rotated_image  = Mercury
    img11 = ImageTk.PhotoImage(Image.open(rotated_img))
    label_planet_image["image"] = img11



    
btn = Button(root, text="Open Image" ,command=planetinfo)  
btn.place(relx=0.5, rely=0.18, anchor=CENTER)
btn = Button(root, text="Rotate" ,command=rotate)  
btn.place(relx=0.5, rely=0.8, anchor=CENTER)

label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
label_planet_image.place(relx=0.5,rely=0.5,anchor=CENTER)
label_planet_gravity_radius.place(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
