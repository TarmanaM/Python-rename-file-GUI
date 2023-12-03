import tkinter as tk
from PIL import Image, ImageTk

index_gambar = 0  
gambar = []

max_width = 200
max_height = 300

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

def prev_gambar():
    global index_gambar
    index_gambar -= 1
    if index_gambar < 0:
        index_gambar = len(gambar)-1

    label_gambar.configure(image=gambar[index_gambar])
    

root = tk.Tk() 

for i in range(5):
    img = Image.open("gambar"+str(i)+".jpg") 
    img = resize_gambar(img)
    gambar.append(ImageTk.PhotoImage(img))

label_gambar = tk.Label(root, image=gambar[0])
label_gambar.pack()

btn_next = tk.Button(root, text="Next", command=next_gambar)
btn_back = tk.Button(root, text="Back", command=prev_gambar)

btn_next.pack()
btn_back.pack()

root.mainloop()