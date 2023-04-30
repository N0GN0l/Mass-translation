import googletrans
import tkinter
from googletrans import Translator
from tkinter import *

languages = []
root = Tk()
translater = Translator()


# Creating a label widget
# label = Label(root, text="Hello world")
# language = Label(root, text="Chinese")
# Shoving it onto the screen
# label.grid(row=0, column=0)
# language.grid(row=1, column=5)


# Create Chinese button function
def chinese():
    languages.append(1)
    print(languages)
    chineseChoose['state'] = DISABLED


# creating a button for chinese
chineseChoose = Button(root, text="Chinese?", padx=20, command=chinese, bg="grey",
                       fg="Red")  # bg = background color, fg = text color
chineseChoose.grid(row=15, column=15)


# Create Spanish button function
def spanish():
    languages.append(2)
    print(languages)
    spanishChoose['state'] = DISABLED


# creating a button for spanish
spanishChoose = Button(root, text="Spanish?", padx=20, command=spanish, bg="grey",
                       fg="Red")  # bg = background color, fg = text color
spanishChoose.grid(row=15, column=20)


def french():
    languages.append(3)
    print(languages)
    frenchChoose['state'] = DISABLED


# creating a button for french
frenchChoose = Button(root, text="French?", padx=20, command=french, bg="grey",
                      fg="Red")  # bg = background color, fg = text color
frenchChoose.grid(row=15, column=30)


def italian():
    languages.append(4)
    print(languages)
    italianChoose['state'] = DISABLED


# creating a button for italian
italianChoose = Button(root, text="Italian?", padx=20, command=italian, bg="grey",
                       fg="Red")  # bg = background color, fg = text color
italianChoose.grid(row=15, column=35)


def japanese():
    languages.append(5)
    print(languages)
    japaneseChoose['state'] = DISABLED


japaneseChoose = Button(root, text="japanese?", padx=20, command=japanese, bg="grey", fg="red")

japaneseChoose.grid(row=15, column=40)


def outputEmail():
    for i in languages:
        if i == 1:
            china = Toplevel()
            china.title("Chinese email")
            china.geometry("1000x100")

            def focusText(event):
                chineseOutput.config(state='normal')
                chineseOutput.focus()
                chineseOutput.config(state='disabled')

            chineseOutput = Text(china, borderwidth=0)
            chineseOutput.insert(1.0, translater.translate(email.get(), src="en", dest="zh-cn").text)
            chineseOutput.pack()

            chineseOutput.configure(state="disabled")

            chineseOutput.bind('<Button-1>', focusText)
        if i == 2:
            spain = Toplevel()
            spain.title("Spanish email")
            spain.geometry("1000x100")

            def focusText(event):
                spanishOutput.config(state='normal')
                spanishOutput.focus()
                spanishOutput.config(state='disabled')

            spanishOutput = Text(spain, borderwidth=0)
            spanishOutput.insert(1.0, translater.translate(email.get(), src="en", dest="es").text)
            spanishOutput.pack()

            spanishOutput.configure(state="disabled")

            spanishOutput.bind('<Button-1>', focusText)
        if i == 3:
            def focusText(event):
                frenchOutput.config(state='normal')
                frenchOutput.focus()
                frenchOutput.config(state='disabled')

            france = Toplevel()
            france.title("French Email")
            france.geometry("1000x100")
            frenchOutput = Text(france, borderwidth=0)
            frenchOutput.insert(1.0, translater.translate(email.get(), src="en", dest="fr").text)
            frenchOutput.pack()

            frenchOutput.configure(state="disabled")

            frenchOutput.bind('<Button-1>', focusText)

        if i == 4:
            italy = Toplevel()
            italy.title("Italian email")
            italy.geometry("1000x100")

            def focusText(event):
                italianOutput.config(state='normal')
                italianOutput.focus()
                italianOutput.config(state='disabled')

            italianOutput = Text(italy, borderwidth=0)
            italianOutput.insert(1.0, translater.translate(email.get(), src="en", dest="it").text)
            italianOutput.pack()

            italianOutput.configure(state="disabled")

            italianOutput.bind('<Button-1>', focusText)

        if i == 5:
            japan = Toplevel()
            japan.title("japanese email")
            japan.geometry("1000x100")

            def focusText(event):
                japaneseOutput.config(state='normal')
                japaneseOutput.focus()
                japaneseOutput.config(state='disabled')

            japaneseOutput = Text(japan, borderwidth=0)
            japaneseOutput.insert(1.0, translater.translate(email.get(), src="en", dest="ja").text)
            japaneseOutput.pack()
            japaneseOutput.configure(state="disabled")
            japaneseOutput.bind('<Button-1>', focusText)


# creating a button for output
output = Button(root, text="Output email", padx=20, pady=10, bg="grey", command=outputEmail)
output.grid(row=35, column=20)

# Creating input widget
email = Entry(root, width=50, borderwidth=10)
email.grid(row=0, column=20)

root.mainloop()