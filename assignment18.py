#Q1. Create a dict with name and mobile number. Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.

import tkinter

from tkinter import *

def terminate():
    exit(0)

def show():
    search_name = l.get(ACTIVE)

root = Tk()
root.config(bg='light yellow')
var=StringVar()

d={'Amit':9729231169,'Lalit':9729787516,'Ashish':9815729751,'Adit':9817756454,'krishan':9807715297,'shakti':654545,'mohan':54435145,'prakas':684961656546,'satish':5685624684,'durga':65226648,'sanju':524646,'shrijana':5962598246,'subash':654845465}
name_list=list(d.keys())

root.resize=(True,True)
root.geometry('500x500')


entry1=Entry(root,width=20).pack()
entry2=Entry(root,width=20).pack()
b=Button(root,text='Click Here',width='10',bg='light green',fg='black').pack()

bm=Button(root,text="Exit",width=10,bg='light blue',font='black',command=terminate)
bm.pack()

f=Frame()
f.pack(side=LEFT)
label=Label(f,text="MyMenu",font=20,fg='black')
label.pack()

s=Scrollbar(f)
s.pack(side=RIGHT,fill=Y)
l=Listbox(f,yscrollcommand=s.set)
for name in name_list:
    l.insert(END,name)

l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview)
root.mainloop()



#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.

import tkinter

from tkinter import *

def terminate():
    exit(0)

def show():
    search_name = l.get(ACTIVE)

def insert():
    d[str(entry1.get())] =int(entry2.get())
    l.insert(END,entry1.get())
    print(d)


root = Tk()
root.config(bg='light yellow')
var=StringVar()

d={'Amit':9729231169,'Lalit':9729787516,'Ashish':9815729751,'Adit':9817756454,'krishan':9807715297,'shakti':654545,'mohan':54435145,'prakas':684961656546,'satish':5685624684,'durga':65226648,'sanju':524646,'shrijana':5962598246,'subash':654845465}
name_list=list(d.keys())

root.resize=(True,True)
root.geometry('500x500')


entry1=Entry(root,width=20)
entry1.pack()
entry2=Entry(root,width=20)
entry2.pack()
b=Button(root,text='Submit',width='10',bg='light green',fg='black',command=insert).pack()

bm=Button(root,text="Exit",width=10,bg='light blue',font='black',command=terminate)
bm.pack()

f=Frame()
f.pack(side=LEFT)
label=Label(f,text="MyMenu",font=20,fg='black')
label.pack()

s=Scrollbar(f)
s.pack(side=RIGHT,fill=Y)
l=Listbox(f,yscrollcommand=s.set)
for name in name_list:
    l.insert(END,name)

l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview)
root.mainloop()

