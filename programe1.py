'''
Build a simple calulator using Tkinter or any other GUI library in Python.
'''

from tkinter import *

cal=Tk()
cal.title("Simple Calculator")
cal.geometry("250x400+600+200")
cal.resizable(0,0)

#Variables
num=""

#functions
def dispaly(number):
    global num
    num+=str(number)
    scr_lbl["text"]=num

    
def clearscr():
    global num
    num=" "
    scr_lbl['text']=num


def equaltn():
    global num
    add= str(eval(num))
    scr_lbl['text']=add
    num=" "
def equalbtn():
    global num
    sub= str(eval(num))
    scr_lbl['text']=sub
    num=" "
def equalbtn():
    global sum
    mul=str(eval(num))
    scr_lbl['text']=mul
    num=" "
def equalbtn():
    global num
    div= str(eval(num))
    scr_lbl['text']=div
    num=" "

var = StringVar()

#  Frames
frame1= Frame(cal)
frame1.pack(expand=True,fill=BOTH)

frame2= Frame(cal)
frame2.pack(expand=True,fill=BOTH)

frame3=Frame(cal)
frame3.pack(expand=True,fill=BOTH)

frame4=Frame(cal)
frame4.pack(expand=True,fill=BOTH)

# Label
scr_lbl = Label(
    frame1,
    textvariable='',
    font=('Arial', 20),
    anchor = SE,
    bg = '#595954',
    fg = 'white' 
    )

scr_lbl.pack(expand=True,fill=BOTH)

# buttons
key1 = Button(
    frame1,
    text='1',
    font=('Arial', 20),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda:dispaly(1)
    )

key1.pack(expand=True, fill=BOTH, side=LEFT)

key2 = Button(
    frame1,
    text='2',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda:dispaly(2)
    )

key2.pack(expand=True, fill=BOTH, side=LEFT)

key3 = Button(
    frame1,
    text='3',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda:dispaly(3)
    )

key3.pack(expand=True, fill=BOTH, side=LEFT)

key_add = Button(
    frame1,
    text='+',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda:dispaly('+')
    )

key_add.pack(expand=True, fill=BOTH, side=LEFT)

key4 = Button(
    frame2,
    text='4',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda:dispaly(4)
    )

key4.pack(expand=True, fill=BOTH, side=LEFT)

key5 = Button(
    frame2,
    text='5',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: dispaly(5)
    )

key5.pack(expand=True, fill=BOTH, side=LEFT)

key6 = Button(
    frame2,
    text='6',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: dispaly(6)
    )

key6.pack(expand=True, fill=BOTH, side=LEFT)

keysub = Button(
    frame2,
    text='-',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda:dispaly('-')
    )

keysub.pack(expand=True, fill=BOTH, side=LEFT)

key7 = Button(
    frame3,
    text='7',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda:dispaly(7)
    )

key7.pack(expand=True, fill=BOTH, side=LEFT)

key8 = Button(
    frame3,
    text='8',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: dispaly(8)
    )

key8.pack(expand=True, fill=BOTH, side=LEFT)

key9 = Button(
    frame3,
    text='9',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda:dispaly(9)
    )

key9.pack(expand=True, fill=BOTH, side=LEFT)

keymul = Button(
    frame3,
    text='*',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda:dispaly('*')
    )

keymul.pack(expand=True, fill=BOTH, side=LEFT)


keyclr = Button(
    frame4,
    text='C',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = clearscr 
    )

keyclr.pack(expand=True, fill=BOTH, side=LEFT)

key0 = Button(
    frame4,
    text='0',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda:dispaly(0)
    )

key0.pack(expand=True, fill=BOTH, side=LEFT)

keyres = Button(
    frame4,
    text='=',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = equalbtn
    )

keyres.pack(expand=True, fill=BOTH, side=LEFT)

keydiv = Button(
    frame4,
    text='/',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda:dispaly('/')
    )

keydiv.pack(expand=True, fill=BOTH, side=LEFT)

cal.mainloop()
