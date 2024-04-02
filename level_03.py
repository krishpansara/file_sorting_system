from tkinter import *
from tkinter import filedialog, messagebox
import os
import shutil

window = Tk()
window.title('File Organizer')
window.iconbitmap('E:/COADING/Python/Project/File Sorting System/File.ico')
# window.geometry('500x450')

#function for browse folder
def browseFolder():
    global path

    path = filedialog.askdirectory() + '/'
    global brwsLabel
    brwsLabel.delete(0, END)
    brwsLabel.insert(0,path)
    brwsLabel.grid(row = 0, column = 0)

#deleting default value in entry bov
def on_click(event):
    event.widget.delete(0, END)

#creating button for browsing folder
brwsBtn = Button(window, text = 'Browse Folder', command = browseFolder)
brwsBtn.grid(row = 0, column = 1)

#creating entry box for path of folder
brwsLabel = Entry(window, font = ('20'))
brwsLabel.insert(0,'Enter Path')
brwsLabel.bind('<Button-1>',on_click)
brwsLabel.grid(row = 0, column = 0, padx = (2,10), ipadx = 200, ipady = 5)

# function for doing proccess 1
def sort():
    global var1
    global path

    if var1.get() == 1:
        for file in os.listdir(path):
            name, ext = os.path.splitext(file)

            extType = ext[1:]

            if os.path.exists(path + extType):
                shutil.move(path + file, path + extType + '/' + file)

            else:
                os.makedirs(path + extType)
                shutil.move(path + file, path + extType + '/' + file)

    if var1.get() == 2:
        for file in os.listdir(path):
            name, ext = os.path.splitext(file)

            extType = ext[1:]

            if os.path.exists(path + extType):
                shutil.move(path + file, path + extType + '/' + file)

            else:
                os.makedirs(path + extType)
                shutil.move(path + file, path + extType + '/' + file)
        for folder in (os.listdir(path)):
            for file in (os.listdir(path + folder)):
                fName = file[0]

            if os.path.exists(path + folder + '/' + fName.upper()):
                shutil.move(path + folder + '/' + file, path + folder + '/' + fName.upper() + '/' + file)
            else:
                os.makedirs(path + folder + '/' + fName.upper()) 
                shutil.move(path + folder + '/' + file, path + folder + '/' + fName.upper() + '/' + file)

    response = messagebox.showinfo('File Organizer', 'Your file has been succseesfully organized')
    # Label(window, text = response).grid()

var1 = IntVar()

op1 = Radiobutton(window, text = 'Sort Selected Folder according to extensions                                                                              ', variable = var1, value = 1)

op1.grid(row = 1, column = 0 , pady = (10,0))

op2 = Radiobutton(window, text =  'Sort Selected Folder according extension and also all the subfolder according to alphabet', variable = var1, value = 2)
op2.grid(row = 2, column = 0)


#submit button
sortButton = Button(window, text = 'Sort' ,width = 10, command = sort)
sortButton.grid(row = 3, column = 1, pady = 15)

window.mainloop()