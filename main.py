from tkinter import *
from datetime import date , datetime
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import tkinter.messagebox as tmsg

''' About Notepad'''     
# Making About GUI
def AboutUs():

    AboutUs_root =  Toplevel()
    # width x height
    AboutUs_root.geometry("300x300")
    # width , height
    AboutUs_root.maxsize(300,300)
    # width , height
    AboutUs_root.minsize(300,300)

    AboutUs_root.wm_iconbitmap("notepad.ico")
    AboutUs_root.title("About NotePad")

    # making canvas 
    can_widget = Canvas(AboutUs_root, width=380, height=300)
    can_widget.pack()

    # Adding win10 logo
    logoname = PhotoImage(file = "Windows_10_logo.png")
    image = can_widget.create_image(70, 15, anchor=NE, image=logoname)

    # Write win10 LOGO
    can_widget.create_text(160,40,text="Windows 10",font="Rowdies 26 bold", fill ="#00BFFF")
    

    # Adding Lines
    can_widget.create_line(20, 70, 280, 70, fill="grey")

    # Addiing images
    filename = PhotoImage(file = "Notepad.png")
    image = can_widget.create_image(50, 80, anchor=NE, image=filename)

    # Adding Texts
    can_widget.create_text(150, 115, text=" Creater - Masoom Zaid \n Computer Science - B.Tech \n Modified Year - 2020 \n Language - Python(Tkinter) ",font="PoiretOne 10 italic")
    
    AboutUs_root.mainloop()

''' Fonts  All  Functions   '''
# Function for handling Fonts
def font():
    # initialize Global Variables 
    global font_lbx,size_lbx, style_lbx, font_root, label,lookOfFont , widthOfFont , styleOfFont

    font_root =  Tk()
    # width x height
    font_root.geometry("400x380")
    # width , height
    font_root.maxsize(400,380)
    # width , height
    font_root.minsize(400,380)

    font_root.wm_iconbitmap("notepad.ico")
    font_root.title("Font - NoTePad")


    # create a canvas for handle listboxes
    can_widget = Canvas(font_root, width=400, height=200)
    can_widget.pack()

    # Headings
    can_widget.create_text(17, 12, text="Font:",font = "Rowdies 8")
    can_widget.create_text(176, 12, text="Style:",font = "Rowdies 8")
    can_widget.create_text(308, 12, text="Size:",font = "Rowdies 8")



    # listbox for Fonts
    font_lbx = Listbox(can_widget,width = 23, height = 8)
    font_lbx.pack(side = LEFT,anchor  = "nw",pady = 20,padx = 5)
    font_lbx.insert(1, "Ariel")
    font_lbx.insert(2, "timesandroman")
    font_lbx.insert(3, "cambria")
    font_lbx.insert(4, "broadway")
    font_lbx.insert(5, "algerian")
    font_lbx.insert(6, "calibri")
    font_lbx.insert(7, "comicsansMS")
    font_lbx.insert(8, "Latin")


    # Listbox for styles
    style_lbx = Listbox(can_widget,width = 18, height = 8)
    style_lbx.pack(side = LEFT,anchor  = "nw",pady = 20,padx = 10)
    style_lbx.insert(1, "normal")
    style_lbx.insert(2, "italic")
    style_lbx.insert(3, "bold")
    style_lbx.insert(4, "bold italic")
    style_lbx.insert(5, "roman")
    style_lbx.insert(6, "overstrike")
    style_lbx.insert(7, "underline")


    # Listbox for sizes
    size_lbx = Listbox(can_widget,width = 10, height = 8)
    size_lbx.pack(side = LEFT,anchor  = "nw",pady = 20,padx = 10)

    # Adding all font sizes
    size_lbx.insert(0, "11")
    size_lbx.insert(1, "12")
    size_lbx.insert(2, "14")
    size_lbx.insert(3, "16")
    size_lbx.insert(4, "18")
    size_lbx.insert(5, "20")
    size_lbx.insert(6, "22")
    size_lbx.insert(7, "24")
    size_lbx.insert(8, "26")
    size_lbx.insert(9, "28")
    size_lbx.insert(10, "30")
    size_lbx.insert(11, "32")
    size_lbx.insert(12, "34")
    size_lbx.insert(13, "36")
    size_lbx.insert(14, "38")
    size_lbx.insert(15, "40")
    size_lbx.insert(16, "42")
    size_lbx.insert(17, "44")
    size_lbx.insert(18, "46")
    size_lbx.insert(19, "48")
    size_lbx.insert(20, "50")
    size_lbx.insert(21, "52")
    size_lbx.insert(22, "54")
    size_lbx.insert(23, "56")
    size_lbx.insert(24, "58")
    size_lbx.insert(25, "60")
    size_lbx.insert(26, "62")
    size_lbx.insert(27, "64")
    size_lbx.insert(28, "66")
    size_lbx.insert(29, "68")
    size_lbx.insert(30, "70")
    size_lbx.insert(31, "72")
    

    # Create Second Canvas for Tesing Fonts and Butoons etc
    can_widget1 = Canvas(font_root, width=400, height=200)
    can_widget1.pack()

    # adding rectangle
    can_widget1.create_rectangle(180, 30, 370, 130)

    # write some usefull variables
    lookOfFont = 'ariel'
    widthOfFont = '16'
    styleOfFont = 'bold'

    
    # adding Some Texts
    can_widget1.create_text(220, 16, text="Preview",font = "Rowdies 16")
   
    label = Label(font_root,text = "AaBbYyZz",font=(lookOfFont,widthOfFont,styleOfFont))
    label.pack()
    label.place(relx  = 0.56,rely = 0.6) 

    # Adding A Buttons
    frame = Frame(font_root)
    frame.pack(side=RIGHT, anchor="nw")

    b1 = Button(frame, text="Cancel", command=close,bd = 5,bg='black',fg='white')
    b1.pack(side=RIGHT,padx = 4,pady=3)

    b2 = Button(frame, text="OK", command=add,bd = 5,bg='black',fg='white')
    b2.pack(side=RIGHT,padx = 4,pady=3)
    frame.place(relx = 0.7, rely = 0.9)

    # handling events 
    font_lbx.bind('<Button-1>', test)
    style_lbx.bind('<Button-1>', test)
    size_lbx.bind('<Button-1>', test)

    font_root.mainloop()

# Add func for Adding Fonts in Notepad
def add():
    global fonts,font_style,fontSize

    # Get all attributes from listbxes 
    fonts = str((font_lbx.get(ACTIVE)))
    font_style = str((style_lbx.get(ACTIVE)))
    fontSize = str((size_lbx.get(ACTIVE)))
    fontSize = int(fontSize)
    # Add them in Textarea
    TextArea.config(font=(fonts,fontSize,font_style))
    close()

# function for testing
def test(event):
    #initilize Global Variables
    global fonts,font_style,fontSize

    # take avtive items from listbox
    fonts = str((font_lbx.get(ACTIVE)))
    font_style = str((style_lbx.get(ACTIVE)))
    fontSize = str((size_lbx.get(ACTIVE)))

    label.config(font = (fonts,fontSize,font_style))

# Close function for FontsBox
def close():
    font_root.destroy()


''' File handling Functions For Notepad'''
# open file function
def openFile():
    check = TextArea.get(1.0, END)

    if check == '\n':
        # open new file
        global file
        # this is taken from documentation
        file = askopenfilename(defaultextension=".txt",
                            filetypes=[("All Files", "*.*"),
                                        ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            # use this for getiing only file name from file path
            root.title(os.path.basename(file) + " - Notepad")
            TextArea.delete(1.0, END)
            # file open as read mode 
            f = open(file, "r")
            #insert word from 1.0 to end where read function reached at the end
            TextArea.insert(1.0, f.read())
            f.close()

    else:
        # ask want to save or not
        msg = tmsg.askyesnocancel("Want to save this File", "click on save to save the file.")
        
        if msg == True:
            saveAsFile()

        elif msg  == False: 
            # open new file
            # this is taken from documentation
            file = askopenfilename(defaultextension=".txt",
                                filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
            if file == "":
                file = None
            else:
                # use this for getiing only file name from file path
                root.title(os.path.basename(file) + " - Notepad")
                TextArea.delete(1.0, END)
                # file open as read mode 
                f = open(file, "r")
                #insert word from 1.0 to end where read function reached at the end
                TextArea.insert(1.0, f.read())
                f.close()

        else:
            None

# Save function
def saveFile():
    global file
    if file == None:
        # this is taken from documentation
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None
            
        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            # use this for getiing only file name from file path
            root.title(os.path.basename(file) + " - Notepad")
            
    else:
        # Save the file
        f = open(file, "w")
        # open as write mode and get all data in file for saving
        f.write(TextArea.get(1.0, END))
        f.close()


# save As a new file fucntion
def saveAsFile():
    global file
    file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])

    if file =="":
            file = None

    else:
        #Save as a new file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        # use this for getiing only file name from file path
        root.title(os.path.basename(file) + " - Notepad")

# New File function
def newFile():

    global file
    check = TextArea.get(1.0, END)

    # check textarea is empty or not
    if check == '\n':
        # making new file
        root.title("Untitled - Notepad")
        file = None
        TextArea.delete(1.0, END)

    else:
        # ask want to save or not
        msg = tmsg.askyesnocancel("Want to save this File", "click on save to save the file.")
        
        if msg == True:
            saveAsFile()

        elif msg  == False:   
            # making new file
            root.title("Untitled - Notepad")
            file = None
            TextArea.delete(1.0, END)

        else:
            None 

 
''' Functionalities  for  notepad  '''
# Cut
def cut():
    TextArea.event_generate("<<Cut>>")

# Copy
def copy():
    TextArea.event_generate(("<<Copy>>"))

# Paste
def paste():
    TextArea.event_generate(("<<Paste>>"))

# Delete
def delete():
    TextArea.event_generate(("<Delete>"))

# Select All
def selectAll():
    TextArea.event_generate(("<<SelectAll>>"))

# function for exiting Notepad
def Exit():
    check = TextArea.get(1.0, END)
    # check textarea is empty or not
    if check == '\n':
        quit()

    else:
        # ask want to save or not
        msg = tmsg.askyesnocancel("Want to save this File", "click on save to save the file.")
        
        if msg == True:
            saveAsFile()

        elif msg  == False: 
            # exit Notepad
            quit()

        else:
            None 


# Date Time Display Function
def DateTime():
    hour = int(datetime.now().hour)
    strTime = datetime.now().strftime("%H:%M %p  %Y-%m-%d")
    
    if hour >= 0 and hour < 12:
        D_time = Label(TextArea,font="Rowdies 20 ",text = strTime)
        D_time.pack()

    else:
        
        D_time = Label(TextArea,font="Rowdies 20 ",text = strTime)
        D_time.pack(side = TOP, anchor = "sw")

#making and Handling Status Bar
def handleStatusBar():
    global sbar
    value = statusBarValue.get()
    if value == 1:
        # visible status bar
        statusvar = StringVar()
        statusvar.set("Ready")
        
        sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
        sbar.pack(side=BOTTOM, fill=X)
    else:
        # unvisible status bar
        sbar.destroy()

# function for handle scrollbar using mouse wheel
def scrollbarHandle(event):
    global count

    def delta(event):
        if event.num == 5 or event.delta < 0:
            return -1 
        return 1 

    count += delta(event)
    
# Handling Zoom functionality
def ZoomIn():
    global fontSize
    fontSize = fontSize + int(2)
    TextArea.config(font=(fonts, fontSize,font_style ))

def ZoomOut():
    global fontSize
    fontSize -= int(2)
    TextArea.config(font=(fonts,fontSize, font_style))

''' main  Functon  of  the  Project  '''
# main function 
def main():
    #  initialze Global variables
    global statusBarValue,TextArea,root,file,fontSize,fonts,font_style,count
    
    root = Tk()

    root.geometry('800x300')
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    
    # variables for Texts
    count = 0
    fontSize = 18
    fonts = 'ariel'
    font_style = 'normal'

    # Add TEXT Area
    TextArea = Text(root,font=(fonts,fontSize,font_style))
    file = None
    TextArea.pack(fill=BOTH, expand=True)
    
    # variable for assign statusbar
    statusBarValue = IntVar()

    # Adding ScrollBar in Right in NotePad
    scrollbar = Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollbar.set)


    # Main menu  start from Here
    mainmenu = Menu(root)

    #creating file Menu
    m1 = Menu(mainmenu, tearoff=0)
    m1.add_command(label="New", command=newFile)
    m1.add_command(label="Open", command=openFile)
    m1.add_command(label="Save", command=saveFile)
    m1.add_command(label="Save As", command=saveAsFile)
    m1.add_separator()
    m1.add_command(label="Exit", command=Exit)

    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="File", menu=m1)

    # Creating EDit Menu

    m2 = Menu(mainmenu, tearoff=0)
    m2.add_command(label="Cut", command=cut)
    m2.add_command(label="Copy", command=copy)
    m2.add_command(label="Paste", command=paste)
    m2.add_command(label="Delete", command=delete)
    m2.add_separator()
    m2.add_command(label="Select All", command=selectAll)
    m2.add_command(label="Time/Date", command=DateTime)

    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="Edit", menu=m2)

    # Creating Format Menu

    m3 = Menu(mainmenu, tearoff=0)
    m3.add_command(label="Font", command=font)

    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="Format", menu=m3)

    # Creating View Menu
    m4 = Menu(mainmenu, tearoff=0)
    m4.add_checkbutton(label="Status bar",variable= statusBarValue, command=handleStatusBar)
    
    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="View", menu=m4)

    # Creating a zoom Menu by  Creating submenus - submenu
    viewMenu = Menu(m4, tearoff=0)
    viewMenu.add_command(label = "zoom in", command = ZoomIn)
    viewMenu.add_command(label = "Zoom out", command = ZoomOut)

    root.config(menu = m4)
    m4.add_cascade(label = "Zoom" , menu = viewMenu)

    # Creating About Menu

    m5 = Menu(mainmenu, tearoff=0)
    m5.add_command(label="About NotePad", command=AboutUs)

    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="About", menu=m5)

    TextArea.bind("<MouseWheel>", scrollbarHandle)
    # TextArea.bind("<Control_L><MouseWheel>", zoom)
    root.mainloop()

if __name__ == "__main__":
    main() 

