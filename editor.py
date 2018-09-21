from tkinter import*
import tkinter.scrolledtext as ScrolledText

root = Tk(className= " Untitled-Editor")
textArea = ScrolledText.ScrolledText(root, width=300, height=200)

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar)
menubar.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "New")
filemenu.add_command(label = "Open")
filemenu.add_command(label = "Save")
filemenu.add_command(label = "Exit")



textArea.pack()
root.mainloop()