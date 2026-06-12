# test.py
import tkinter as tk

root = tk.Tk()
root.title("Umut Aydın Elidenk App")
root.geometry("300x200")

label = tk.Label(root, text="👋 Selam! Gerçek bir Mac Uygulamasıyım.", pady=20)
label.pack()

btn = tk.Button(root, text="Kapat", command=root.destroy)
btn.pack()

root.mainloop()