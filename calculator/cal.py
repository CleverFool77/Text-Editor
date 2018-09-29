from tkinter import*

e = ""
def press(n):
    global e
    if n == "=":
        num.set(str(eval(e)))
    else:
        e = e + str(n)
        num.set(e)


def clearb():
    txtd.delete(0,END)
    global e
    e = ""
    return

root = Tk()
large_font = ('',13)
num = StringVar()
root.title("Calculator") 

txtd= Entry(root,textvariable=num,bd = 6,font=large_font)
txtd.grid(row=0,columnspan =4, ipadx=0)

w1 = Button( root, bg='light gray',text="1",fg='black',height=3,width=4,command=lambda: press(1) )
w1.grid(row=1, column=0)
w2 = Button( root, bg='light gray',text="2",fg='black',height=3,width=4 ,command=lambda: press(2))
w2.grid(row=1, column=1)
w3 = Button( root, bg='light gray',text="3",fg='black',height=3,width=4 ,command=lambda: press(3))
w3.grid(row=1, column=2)
w4 = Button( root, bg='light gray',text="4",fg='black',height=3,width=4 ,command=lambda: press(4))
w4.grid(row=1, column=3)
w5 = Button( root, bg='light gray',text="5",fg='black',height=3,width=4 ,command=lambda: press(5))
w5.grid(row=2, column=0)
w6 = Button( root, bg='light gray',text="6",fg='black',height=3,width=4 ,command=lambda: press(6))
w6.grid(row=2, column=1)
w7 = Button( root, bg='light gray',text="7",fg='black',height=3,width=4 ,command=lambda: press(7))
w7.grid(row=2, column=2)
w8 = Button( root, bg='light gray',text="8",fg='black',height=3,width=4 ,command=lambda: press(8))
w8.grid(row=2, column=3)
w9 = Button( root, bg='light gray',text="9",fg='black',height=3,width=4 ,command=lambda: press(9))
w9.grid(row=3, column=0)
w10 = Button( root, bg='light gray',text="0",fg='black',height=3,width=4 ,command=lambda: press(0))
w10.grid(row=3, column=1)
w11 = Button( root, bg='light gray',text="+",fg='black',height=3,width=4 ,command=lambda: press("+"))
w11.grid(row=3, column=2)
w12 = Button( root, bg='light gray',text="-",fg='black',height=3,width=4 ,command=lambda: press("-"))
w12.grid(row=3, column=3)
w13 = Button( root, bg='light gray',text="/",fg='black',height=3,width=4 ,command=lambda: press("/"))
w13.grid(row=4, column=0)
w14 = Button( root, bg='light gray',text="*",fg='black',height=3,width=4 ,command=lambda: press("*"))
w14.grid(row=4, column=1)
w15 = Button( root, bg='light gray',text="c",fg='black',height=3,width=4 ,command = clearb)
w15.grid(row=4, column=2)
w16 = Button( root, bg='light gray',text="=",fg='black',height=3,width=4 ,command=lambda: press("="))
w16.grid(row=4, column=3)

root.mainloop()