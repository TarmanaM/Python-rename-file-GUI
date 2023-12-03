import os
from tkinter import Tk, Label, Button, Entry, PhotoImage, Canvas, filedialog
from PIL import Image, ImageTk

class ImageRenamer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Renamer")

        self.folder_path = "C:\Users\tipti\Documents\My Cheat Tables\temp\Temp"
        self.image_files = []
        self.current_index = 0

        self.load_images()
        self.create_widgets()

    def load_images(self):
        self.image_files = [file for file in os.listdir(self.folder_path) if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    def create_widgets(self):
        self.image_label = Label(self.root)
        self.image_label.pack(pady=10)

        self.name_label = Label(self.root, text="Nama Gambar Sebelumnya:")
        self.name_label.pack()

        self.name_entry = Entry(self.root)
        self.name_entry.pack()

        self.next_button = Button(self.root, text="Next", command=self.show_next_image)
        self.next_button.pack(side="right", padx=10)

        self.prev_button = Button(self.root, text="Prev", command=self.show_prev_image)
        self.prev_button.pack(side="left", padx=10)

        self.update_display()

    def show_next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_files)
        self.update_display()

    def show_prev_image(self):
        self.current_index = (self.current_index - 1) % len(self.image_files)
        self.update_display()

    def update_display(self):
        if self.image_files:
            image_path = os.path.join(self.folder_path, self.image_files[self.current_index])
            image = Image.open(image_path)
            image.thumbnail((400, 400))
            tk_image = ImageTk.PhotoImage(image)

            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image

            # Menampilkan nama file sebelumnya
            if self.current_index > 0:
                self.name_entry.delete(0, 'end')
                self.name_entry.insert(0, self.image_files[self.current_index - 1])
            else:
                self.name_entry.delete(0, 'end')

        else:
            self.image_label.config(image=None)
            self.name_label.config(text="No images found.")
            self.name_entry.delete(0, 'end')

if __name__ == "__main__":
    root = Tk()
    app = ImageRenamer(root)
    root.mainloop()
    input("Press Enter to exit...")
