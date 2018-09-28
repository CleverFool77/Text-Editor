from tkinter import*


root = Tk()
root.title("Calculator")  

w1 = Button( root, bg='gray',text="1",fg='black',height=3,width=4 )
w2 = Button( root, bg='gray',text="2",fg='black',height=3,width=4 )
w3 = Button( root, bg='gray',text="3",fg='black',height=3,width=4 )
w4 = Button( root, bg='gray',text="4",fg='black',height=3,width=4 )
w5 = Button( root, bg='gray',text="5",fg='black',height=3,width=4 )
w6 = Button( root, bg='gray',text="6",fg='black',height=3,width=4 )
w7 = Button( root, bg='gray',text="7",fg='black',height=3,width=4 )
w8 = Button( root, bg='gray',text="8",fg='black',height=3,width=4 )
w9 = Button( root, bg='gray',text="9",fg='black',height=3,width=4 )
w10 = Button( root, bg='gray',text="0",fg='black',height=3,width=4 )
w11 = Button( root, bg='gray',text="+",fg='black',height=3,width=4 )
w12 = Button( root, bg='gray',text="-",fg='black',height=3,width=4 )
w13 = Button( root, bg='gray',text="/",fg='black',height=3,width=4 )
w14 = Button( root, bg='gray',text="*",fg='black',height=3,width=4 )
w15 = Button( root, bg='gray',text="c",fg='black',height=3,width=4 )
w16 = Button( root, bg='gray',text="=",fg='black',height=3,width=4 )

w1.pack(),w2.pack(),w3.pack(),w4.pack(),w5.pack(),w6.pack(),w7.pack(),w8.pack()


root.mainloop()