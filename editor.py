from tkinter import Tk, scrolledtext, Menu, filedialog


root = Tk(className= " Untitled-Editor")
textArea = scrolledtext.ScrolledText(root, width=200, height=150)

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar)
editmenu = Menu(menubar)
helpmenu = Menu(menubar)

#adding options to our menu
menubar.add_cascade(label = "File", menu=filemenu)
menubar.add_cascade(label = "Edit", menu=editmenu)
menubar.add_cascade(label= "Help", menu=helpmenu)

#adding to filemenu
def newFile():

# def openFile():
# def saveFile():
# def exitFile():
filemenu.add_command(label = "New",command = newFile)
filemenu.add_command(label = "Open",command = openFile)
filemenu.add_command(label = "Save",command = saveFile)
filemenu.add_separator()
filemenu.add_command(label = "Exit",command = exitFile)

#adding to our editmenu
editmenu.add_cascade(label="Cut")
editmenu.add_cascade(label="Copy")
editmenu.add_cascade(label="Paste")

#adding to our help menu
helpmenu.add_cascade(label="Help")
helpmenu.add_separator()
helpmenu.add_cascade(label="About")


textArea.pack()
root.mainloop()