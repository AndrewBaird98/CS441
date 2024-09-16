from tkinter import *
import re


##the click function
def click():
    inside_output = outputBox.get('1.0', 'end-1c')
    split_output = inside_output.split('\n')
    count = -1
    for line in split_output:
        count = count + 1
    entered_code = textentry.get('0.0', 'end-1c')
    split_code = entered_code.split('\n')
    if count < len(split_code):
        lexfinder(split_code[count])
        ##        outputBox.insert(END,split_code[count]+'\n')
        outputBox.insert(END, "\n")
        line_num.delete(0.0, END)
        line_num.insert(END, count + 1)


def lexfinder(inputstring):
    num = len(inputstring)
    for next in range(num):
        if re.match(r'\s*\w+\D\s', inputstring) is not None:
            keyword = re.match(r'\s*\w+\D\s', inputstring)
            ke = keyword.group()
            ke = ke.replace(" ", "")
            outputBox.insert(END, "<Keyword,%s> " % (ke))
            inputstring = inputstring[:keyword.start()] + inputstring[keyword.end():]
        if re.match(r'\s*[a-zA-z]+\d*\s*', inputstring) is not None:
            ident = re.match(r'\s*[a-zA-z]+\d*\s*', inputstring)
            ide = ident.group()
            ide = ide.replace(" ", "")
            outputBox.insert(END, "<identifier,%s> " % (ide))
            inputstring = inputstring[:ident.start()] + inputstring[ident.end():]
        if re.match(r'\s*[=+>-]\s*', inputstring) is not None:
            oper = re.match(r'\s*[=+>]\s*', inputstring)
            ope = oper.group()
            ope = ope.replace(" ", "")
            outputBox.insert(END, "<operator,%s> " % (ope))
            inputstring = inputstring[:oper.start()] + inputstring[oper.end():]
        if re.match(r'\s*[0-9]+\s*', inputstring) is not None:
            literal = re.match(r'\s*[0-9]+\s*', inputstring)
            lit = literal.group()
            lit = lit.replace(" ", "")
            outputBox.insert(END, "<literal,%s> " % (lit))
            inputstring = inputstring[:literal.start()] + inputstring[literal.end():]
        if re.match(r'\s*[():"]\s*', inputstring) is not None:
            separator = re.match(r'\s*[():"]\s*', inputstring)
            sep = separator.group()
            sep = sep.replace(" ", "")
            outputBox.insert(END, "<separator,%s> " % (sep))
            inputstring = inputstring[:separator.start()] + inputstring[separator.end():]


##close function
def close():
    window.destroy()
    exit()

##UI code
##Main window:
window = Tk()
window.title("My Window")
window.configure(background="orange")
##Label for the source code
Label(window, text="Enter the source code", bg="orange", fg="purple", font="none 12 bold").grid(row=1, column=4,
                                                                                                sticky=W)

##text box for input
textentry = Text(window, width=30, height=10, wrap=WORD, background="white")
textentry.grid(row=2, column=4, columnspan=3, sticky=W)

##the next line button
Button(window, text="next line", width=6, command=click).grid(row=3, column=4, sticky=W)

##label for the output
Label(window, text="\nThe code inputed", bg="orange", fg="purple", font="none 12 bold").grid(row=1, column=8, sticky=W)

##the output box
outputBox = Text(window, width=40, height=30, wrap=WORD, background="white")
outputBox.grid(row=2, column=8, columnspan=5, sticky=E)
##line it is on
Label(window, text="Number of the line", bg="orange", fg="purple", font="none 12 bold").grid(row=3, column=5, sticky=E)
##text box for what line we are on
line_num = Text(window, width=4, height=2, background="white")
line_num.grid(row=3, column=6, sticky=E)
##the quit button
Button(window, text="close window", command=close).grid(row=3, column=8, sticky=E)

## main loop
window.mainloop()
