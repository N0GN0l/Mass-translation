import googletrans
from googletrans import Translator
from tkinter import *

languages = []
root = Tk()
translator = Translator()

# Creating a label widget
label = Label(root, text="Hello world")
language = Label(root, text="Chinese")
# Shoving it onto the screen
label.grid(row=0, column=0)
language.grid(row=1, column=5)


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


def outputEmail():
    for i in languages:
        if i == 1:
            chineseOutput = Label(root, text=translator.translate(email.get(), src="en", dest="chinese (simplified)"))
            chineseOutput.grid(row=30, column=30)


# creating a button for output
output = Button(root, text="Output email", padx=20, pady=10, bg="grey", command=outputEmail)
output.grid(row=35, column=20)

# Creating input widget
email = Entry(root)
email.grid(row=0, column=0)

root.mainloop()