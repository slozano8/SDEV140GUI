####################  IMPORT LIBRARIES  #####################################

import tkinter as tk




### trivial change to show github branch


places = []
State = ["AL", "AK", "AZ", "AR","CA", "CO", "CT", "AL", "AK", "AZ", "AR","CA", "CO", "CT","DE", "FL", "GA", "HI","ID", "IL", "IN","IA", "KS", "KY", "LA", "ME","MD", "MA", "MI","MN", "MS", "MO", "MT","NE", "NV", "NH","NJ", "NM", "NY", "NC","ND", "OH", "OK","OR", "PA","RI", "SC","SD", "TN", "TX", "UT","VT", "VA", "WA","WV", "WI","WY"]


###################  GUI METHODS ########################################################

def DisplayStatus(status):
    lblStatus["text"] = "STATUS: " + str(status)
## end DisplayStatus()


def AddPerson(event):
    
    if txtName.get() == "":
        parkName = "<<Park>>"
    else:
        parkName = txtName.get()
        
    try:
        age = int(txtAge.get())
    except:
        age = -1
        
    if txtTown.get() == "":
        city = "<<City>>"
    else:
        city = txtTown.get()
  
        
    if omChosen.get() == "":
        State = "<<State>>"
    else:
        State = omChosen.get()
        
        
    places.append([parkName, str(age), city, State])
    
    lstDisplay.delete(0, tk.END)
    for person in places:
        lstDisplay.insert(tk.END, person)
 
    txtName.delete(0, tk.END)
    txtAge.delete(0, tk.END)
    txtTown.delete(0, tk.END)
    omChosen.set("")
    txtName.focus_set()

    DisplayStatus("Data added successfully...")
## end AddPerson()


def EditPerson(event):
    DisplayStatus("editing data coming soon...")
## end EditPerson()


def DeletePerson(event):
    DisplayStatus("deleting data coming soon...")
## end DeletePerson()




def ShowContextMenu(event):
    try:
            ## most everything here is stuff built into tkinter
            ## library and events (not sure what the zero is)
        mnContext.tk_popup(event.x_root, event.y_root, 0)
    finally:
            ## only needed in tkinter 8.0.x
        mnContext.grab_release()




#######################  THE GUI  ####################################


gui = tk.Tk()
gui.title("GUI Starter Template")
#gui.iconbitmap("multisizeIcon.ico")
gui.geometry("500x500")


mnMain = tk.Menu(gui)

mnFile = tk.Menu(mnMain, tearoff = 0)
mnFile.add_command(label = "Add Person", command = lambda: AddPerson(None))
mnMain.add_cascade(label = "File", menu = mnFile)

mnEdit = tk.Menu(mnMain, tearoff = 0)
mnEdit.add_command(label = "Edit Person", command = lambda: EditPerson(None))
mnMain.add_cascade(label = "Edit", menu = mnEdit)

mnView = tk.Menu(mnMain, tearoff = 0)
mnView.add_command(label = "Delete Person", command = lambda: DeletePerson(None))
mnMain.add_cascade(label = "View", menu = mnView)


mnContext = tk.Menu(gui, tearoff = 0)
mnContext.add_command(label = "Add Person", command = lambda: AddPerson(None))
gui.bind("<Button-3>", ShowContextMenu)


tbMain = tk.Frame(gui, bd = 1, relief = "ridge")
picAdd = tk.PhotoImage(file = "add_person.png")
picAdd = picAdd.subsample(16)
tbbAddPerson = tk.Button(tbMain, image = picAdd)
tbbAddPerson.bind("<Button-1>", lambda event: AddPerson(event))

picDelete = tk.PhotoImage(file = "remove_person.png")
picDelete = picDelete.subsample(16)
tbbDeletePerson = tk.Button(tbMain, image = picDelete)
tbbDeletePerson.bind("<Button-1>", lambda event: DeletePerson(event))


picEdit = tk.PhotoImage(file = "edit_person.png")
picEdit = picEdit.subsample(16)
tbbEditPerson = tk.Button(tbMain, image = picEdit)
tbbEditPerson.bind("<Button-1>", lambda event: EditPerson(event))


    ## main content
pnContent = tk.PanedWindow(gui, orient=tk.HORIZONTAL, sashrelief="raised")
frmInput = tk.Frame(pnContent, bd=3, relief="groove")
frmDisplay = tk.Frame(pnContent, bd=3, relief="groove")
pnContent.add(frmInput)
pnContent.add(frmDisplay)


    ## prompt for userinput
lblName = tk.Label(frmInput, text="Park Name:")
txtName = tk.Entry(frmInput)

lblAge = tk.Label(frmInput, text="Site Number:")
txtAge = tk.Entry(frmInput)

lblTown = tk.Label(frmInput, text="City:")
txtTown = tk.Entry(frmInput)

lblFavFood = tk.Label(frmInput, text="State")
omChosen = tk.StringVar("")
omFavFood = tk.OptionMenu(frmInput, omChosen, *State)


    ## display in a listbox
lblDisplay = tk.Label(frmDisplay, text="Favorite Rv Parks")
lstDisplay = tk.Listbox(frmDisplay)


    ## output a greeting
lblGreet = tk.Label(frmInput)
btnAddPlace = tk.Button(frmInput, text="Add Place")
btnAddPlace.bind("<Button-1>", lambda event: AddPerson(event))


    ## create a status bar
frmStatus = tk.Frame(gui, bd = 1, relief = "sunken")
lblStatus = tk.Label(frmStatus, text="STATUS: Ready...")


    ## load the widgets on the gui
gui.config(menu = mnMain)
tbMain.pack(fill = "both", padx = 2, pady = 5)
pnContent.pack(fill = "both", pady = 5, expand=1)
frmStatus.pack(side = "bottom", fill = "both")


tbbAddPerson.grid(row = 0, column = 0, padx = 3, pady = 5)
tbbDeletePerson.grid(row = 0, column = 1, padx = 3, pady = 5)
tbbEditPerson.grid(row = 0, column = 2, padx = 3, pady = 5)

lblName.grid(row = 0, column = 0)
txtName.grid(row = 0, column = 1)
lblAge.grid(row = 1, column = 0)
txtAge.grid(row = 1, column = 1)
lblTown.grid(row = 2, column = 0)
txtTown.grid(row = 2, column = 1)
lblFavFood.grid(row=3, column=0)
omFavFood.grid(row=3, column=1)

lblDisplay.pack()
lstDisplay.pack(fill="both", padx=7, pady=7, expand=1)


btnAddPlace.grid(row = 4, column = 0, columnspan=2, sticky="NSEW")


lblStatus.pack(side = "left", fill = "both")

    ### this sets up the key press: ctrl+shift+H to run the method
        ### for a simple keypress event: "Keypress-H"
gui.bind("<Control-Shift-KeyPress-A>", lambda event: AddPerson(event))


### trivial change to show github branch
x = 3


    ## start the gui
if __name__ == "__main__":
    gui.mainloop()


