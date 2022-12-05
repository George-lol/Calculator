from tkinter import *

operation = ''
x = 0

root = Tk()
root.geometry('336x525')
root.resizable(height=True, width=True)

def addnum(num):
    global x
    global operation    
    match operation:
        case '+':
            x = float(inp.cget('text'))
            inp['text'] = ''
            inp['text'] = inp['text'] + str(num)
            operation = '++'
            print(x)
        case '-':
            x = float(inp.cget('text'))
            inp['text'] = ''
            inp['text'] = inp['text'] + str(num)
            operation = '--'
            print(x)
        case '*':
            x = float(inp.cget('text'))
            inp['text'] = ''
            inp['text'] = inp['text'] + str(num)
            operation = '**'
            print(x)
        case '/':
            x = float(inp.cget('text'))
            inp['text'] = ''
            inp['text'] = inp['text'] + str(num)
            operation = '//'
            print(x)    
        case '**':
            x = float(inp.cget('text'))
            inp['text'] = ''
            inp['text'] = inp['text'] + str(num)
            operation = '***'
            print(x)            
        case _:
            inp['text'] = inp['text'] + str(num)
               
def rav():
    value = float(inp.cget('text'))
    match operation:
        case '++':
            inp['text'] = value + x
        case '--':
            inp['text'] = x - value
        case '**':
            inp['text'] = value * x
        case '//':
            inp['text'] = x / value
        case '***':
            inp['text'] = x ** value

def addoper(op):
    global x
    global operation
    operation = op 

def cc():
    global x
    global operation
    operation = ''
    x = 0
    inp['text'] = ''
    
        

inp = Label(root, bg='#C9C9C9', width=10)
inp.grid(row=0, column=0, columnspan=4, sticky=EW)

Button(root, text='1', command=lambda: addnum(1), width=10, height=4, bg='white').grid(row=2, padx=2, pady=2, column=0)
Button(root, text='2', command=lambda: addnum(2), width=10, height=4, bg='white').grid(row=2, padx=2, pady=2, column=1)
Button(root, text='3', command=lambda: addnum(3), width=10, height=4, bg='white').grid(row=2, padx=2, pady=2, column=2)
Button(root, text='4', command=lambda: addnum(4), width=10, height=4, bg='white').grid(row=3, padx=2, pady=2, column=0)
Button(root, text='5', command=lambda: addnum(5), width=10, height=4, bg='white').grid(row=3, padx=2, pady=2, column=1)
Button(root, text='6', command=lambda: addnum(6), width=10, height=4, bg='white').grid(row=3, padx=2, pady=2, column=2)
Button(root, text='7', command=lambda: addnum(7), width=10, height=4, bg='white').grid(row=4, padx=2, pady=2, column=0)
Button(root, text='8', command=lambda: addnum(8), width=10, height=4, bg='white').grid(row=4, padx=2, pady=2, column=1)
Button(root, text='9', command=lambda: addnum(9), width=10, height=4, bg='white').grid(row=4, padx=2, pady=2, column=2)
Button(root, text='0', command=lambda: addnum(0), width=10, height=4, bg='white').grid(row=5, padx=2, pady=2, column=0,columnspan=3, sticky=EW)

Button(root, bg='#C9C9C9', command=lambda: addoper('+'), width=10, height=4, text='+').grid(row=1, padx=2, pady=2, column=3)
Button(root, bg='#C9C9C9', command=lambda: addoper('-'), width=10, height=4, text='-').grid(row=2, padx=2, pady=2, column=3)
Button(root, bg='#C9C9C9', command=lambda: addoper('*'), width=10, height=4, text='*').grid(row=3, padx=2, pady=2, column=3)
Button(root, bg='#C9C9C9', command=lambda: addoper('/'), width=10, height=4, text='/').grid(row=4, padx=2, pady=2, column=3)
Button(root, bg='#C9C9C9', command=lambda: addoper('**'), width=10, height=4, text='^').grid(row=5, padx=2, pady=2, column=3)
Button(root, bg='#00ABFF', fg='white', font='ARIAL, 30', command=rav, width=10, height=2, text='=').grid(row=6, padx=2, pady=2, column=0, columnspan=4, sticky=EW)

Button(root, text='C', bg='#006DA4', command=cc, height=4).grid(row=1, column=0, columnspan=3, sticky=EW)

root.mainloop()