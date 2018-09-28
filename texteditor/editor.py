from tkinter import Tk, scrolledtext, Menu, filedialog,messagebox, END


root = Tk(className= " Editor")
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
    if len(textArea.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno("Save","Do you wish to save ?"):
            saveFile()

    root.title("Untitled-Editor")
    textArea.delete('1.0',END)

def openFile():
    file = filedialog.askopenfile(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    
    if file is not None:
        data = file.read()
        textArea.insert('1.0', data)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

    if file is not None:
        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def exitFile():
    if messagebox.askyesno("Quit","Are you sure you waana quit ?"):
        root.destroy()
    
filemenu.add_command(label = "New",command = newFile)
filemenu.add_command(label = "Open",command = openFile)
filemenu.add_command(label = "Save",command = saveFile)
# filemenu.add_separator()
filemenu.add_command(label = "Exit",command = exitFile)

# def cutFile():

# def copyFile():
    
# def pasteFile():
    

#adding to our editmenu
# editmenu.add_cascade(label="Cut",command=cutFile)
# editmenu.add_cascade(label="Copy",command=copyFile)
# editmenu.add_cascade(label="Paste",command=pasteFile)

def helpEditor():
    messagebox.showinfo("Help", "README.md -/\- check it out")

def aboutEditor():
    messagebox.showinfo("About", "A tkinter based editor in python")
#adding to our help menu
helpmenu.add_command(label="Help",command=helpEditor)
helpmenu.add_separator()
helpmenu.add_command(label="About",command=aboutEditor)


textArea.pack()
root.mainloop()