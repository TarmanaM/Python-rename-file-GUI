import tkinter as tk
from PIL import Image, ImageTk

index_gambar = 0  
gambar = []

max_width = 100
max_height = 200
root = tk.Tk() 

label_nama = tk.Label(root, text="")
entry_nama = tk.Entry(root)

def update_nama():
    nama_baru = entry_nama.get()
    gambar[index_gambar].filename = nama_baru
    label_nama.config(text=nama_baru)

def resize_gambar(img):
    width, height = img.size
    ratio = max(max_width/width, max_height/height)

    return img.resize((int(width*ratio), int(height*ratio)))

def next_gambar():
    global index_gambar
    index_gambar += 1
    if index_gambar == len(gambar):
        index_gambar = 0
    label_gambar.configure(image=gambar[index_gambar])
    label_nama.config(text=gambar[index_gambar].filename)

def prev_gambar():
    global index_gambar
    index_gambar -= 1
    if index_gambar < 0:
        index_gambar = len(gambar)-1
    label_gambar.configure(image=gambar[index_gambar])
    label_nama.config(text=gambar[index_gambar].filename)
    



for i in range(5):
    img = Image.open("gambar"+str(i)+".jpg") 
    img = resize_gambar(img)

    photo = ImageTk.PhotoImage(img)
    photo.filename = "gambar"+str(i)+".jpg"
    gambar.append(photo)  

label_gambar = tk.Label(root, image=gambar[0])
label_gambar.pack()

btn_update = tk.Button(root, text="Update Nama", command=update_nama) 

btn_next = tk.Button(root, text="Next", command=next_gambar)
btn_back = tk.Button(root, text="Back", command=prev_gambar)


label_nama.pack()
entry_nama.pack() 
btn_update.pack()


btn_next.pack()
btn_back.pack()
root.mainloop()