import tkinter as tk

root = tk.Tk()
root.title("Form Input") 

nama_label = tk.Label(root, text="Nama").grid(row=0, column=0)
nama_entry = tk.Entry(root)
nama_entry.grid(row=0, column=1)

umur_label = tk.Label(root, text="Umur").grid(row=1, column=0)  
umur_entry = tk.Entry(root)
umur_entry.grid(row=1, column=1)

root.mainloop()