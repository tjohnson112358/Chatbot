#!/usr/bin/python
'''A simple gui for building xml phrase files'''
try:
    from Tkinter import *
    from ttk import *
except:
    from tkinter import *
    from tkinter.ttk import *
    
from phrases import Inphrase, Outphrase

root = Tk()

in_out_label = Label(root, text = "'in'[phrase] or 'out'[phrase]: ")
in_out_label.grid(row = 0, column = 0)

in_out = Entry(root)
in_out.insert(0, 'in')
in_out.grid(row = 0, column = 1)


type_label = Label(root, text = 'query/statement: ')
type_label.grid(row = 1, column = 0)

type = Entry(root)
type.insert(0, 'query')
type.grid(row = 1, column = 1)


question_label = Label(root, text = "Question: ")
question_label.grid(row = 2, column = 0)

question = Entry(root)
question.insert(0, "QUERY ")
question.grid(row = 2, column = 1)


action_label = Label(root, text = "Action: ")
action_label.grid(row = 3, column = 0)

action = Entry(root)
action.insert(0, "")
action.grid(row = 3, column = 1)


content_label = Label(root, text = "Content: ")
content_label.grid(row = 4, column = 0)

content = Entry(root)
content.insert(0, "")
content.grid(row = 4, column = 1)

data_text = Text(root)

def createphrase():
    io = in_out.get().lower().strip()
    t = type.get().lower().strip()
    q = question.get().lower().strip()
    a = action.get().lower().strip()
    c = content.get().strip()
    
    pre_q = t.upper()[:5] + ' ' #HACK: only works because 'state ' and 'query ' are the same length.
    print(t)
    if io.startswith('in'):
        phrase = Inphrase(t, c, question = pre_q + ' ' + q, action = pre_q + ' ' + a)
    elif io.startswith('out'):
        phrase = Outphrase(t, c, question = pre_q + ' ' + q, action = pre_q + ' ' + a)
    else: 
        print('ERROR')
        return
    
    data_text.insert('end', '\n' + phrase.toXML())

btn = Button(root, text = 'Create phrase', command = createphrase)
btn.grid(row = 5, columnspan = 2)

data_text.grid(row = 6, columnspan = 2)

root.mainloop()