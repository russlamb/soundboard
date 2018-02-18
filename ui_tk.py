from tkinter import *
import play_sound


button = None

def run_tk():
    print("run tk")
    root=Tk()
    button = Button(root, text="Play sound", command = play_sound.play_sound)
    face_image = PhotoImage(file ="face.ppm" )

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        photo = PhotoImage(file="face.ppm").zoom(new_width, new_height)

        button.config(image=photo)
        button.image = photo

    button.config(image=face_image)
    button.bind('<Configure>',resize_image)
    button.pack(fill=BOTH, expand=YES)
    root.mainloop()

