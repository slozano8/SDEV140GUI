####################  IMPORT LIBRARIES  #####################################

import tkinter as tk




### trivial change to show github branch


places = []
State = ["AL", "AK", "AZ", "AR","CA", "CO", "CT", "AL", "AK", "AZ", "AR","CA", "CO", "CT","DE", "FL", "GA", "HI","ID", "IL", "IN","IA", "KS", "KY", "LA", "ME","MD", "MA", "MI","MN", "MS", "MO", "MT","NE", "NV", "NH","NJ", "NM", "NY", "NC","ND", "OH", "OK","OR", "PA","RI", "SC","SD", "TN", "TX", "UT","VT", "VA", "WA","WV", "WI","WY"]


###################  GUI METHODS ########################################################

def DisplayStatus(status):
    lblStatus["text"] = "STATUS: " + str(status)
## end DisplayStatus()


def AddPlace(event):
    
    if txtName.get() == "":
        parkName = "<<Park>>"
    else:
        parkName = txtName.get()

    if txtCampground.get() == "":
        Campground = "<<Campground>>"
    else:
        Campground = txtCampground.get()

    try:
        siteNumber = int(txtsiteNumber.get())
    except:
        siteNumber = -1
        
    if txtTown.get() == "":
        city = "<<City>>"
    else:
        city = txtTown.get()

    if txtElectric.get() == "":
        Electric = "<<Electric>>"
    else:
        Electric = txtElectric.get()
  
    if txtWater.get() == "":
        Water = "<<Water>>"
    else:
        Water = txtWater.get()
        
    if txtAmenities.get() == "":
        Amenities = "<<Amenities>>"
    else:
        Amenities = txtAmenities.get()

    if omChosen.get() == "":
        State = "<<State>>"
    else:
        State = omChosen.get()

   
        
        
    places.append([parkName, str(siteNumber), city, State, Campground, Electric, Amenities])
    
    lstDisplay.delete(0, tk.END)
    for person in places:
        lstDisplay.insert(tk.END, person)
 
    txtName.delete(0, tk.END)
    txtCampground.delete(0, tk.END)
    txtsiteNumber.delete(0, tk.END)
    txtTown.delete(0, tk.END)
    txtElectric.delete(0, tk.END)
    txtWater.delete(0, tk.END)
    txtAmenities.delete(0, tk.END)
    omChosen.set("")
    txtName.focus_set()

    DisplayStatus("Place added successfully...")
## end AddPerson()


def EditPlace(event):
    DisplayStatus("Do you wish to make changes?...")
## end EditPerson()


def DeletePlace(event):
    DisplayStatus("Place deleted Successfully...")
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
gui.title("Personal Campground Organizer")
#gui.iconbitmap("multisizeIcon.ico")
gui.geometry("500x500")


mnMain = tk.Menu(gui)

mnFile = tk.Menu(mnMain, tearoff = 0)
mnFile.add_command(label = "Add Place", command = lambda: AddPlace(None))
mnMain.add_cascade(label = "File", menu = mnFile)

mnEdit = tk.Menu(mnMain, tearoff = 0)
mnEdit.add_command(label = "Edit Place", command = lambda: EditPlace(None))
mnMain.add_cascade(label = "Edit", menu = mnEdit)

mnView = tk.Menu(mnMain, tearoff = 0)
mnView.add_command(label = "Delete Place", command = lambda: DeletePlace(None))
mnMain.add_cascade(label = "Delete", menu = mnView)


mnContext = tk.Menu(gui, tearoff = 0)
mnContext.add_command(label = "Add Person", command = lambda: AddPlace(None))
gui.bind("<Button-3>", ShowContextMenu)


tbMain = tk.Frame(gui, bd = 1, relief = "ridge")
picAdd = tk.PhotoImage(file = "checkin.png")
picAdd = picAdd.subsample(16)
tbbAddPlace = tk.Button(tbMain, image = picAdd)
tbbAddPlace.bind("<Button-1>", lambda event: AddPlace(event))

picDelete = tk.PhotoImage(file = "checkout.png")
picDelete = picDelete.subsample(16)
tbbDeletePlace = tk.Button(tbMain, image = picDelete)
tbbDeletePlace.bind("<Button-1>", lambda event: DeletePlace(event))


picEdit = tk.PhotoImage(file = "edit_place.png")
picEdit = picEdit.subsample(16)
tbbEditPlace = tk.Button(tbMain, image = picEdit)
tbbEditPlace.bind("<Button-1>", lambda event: EditPlace(event))


    ## main content
pnContent = tk.PanedWindow(gui, orient=tk.HORIZONTAL, sashrelief="raised")
frmInput = tk.Frame(pnContent, bd=3, relief="groove")
frmDisplay = tk.Frame(pnContent, bd=3, relief="groove")
pnContent.add(frmInput)
pnContent.add(frmDisplay)


    ## prompt for userinput
lblName = tk.Label(frmInput, text="Park Name:")
txtName = tk.Entry(frmInput)

lblCampground = tk.Label(frmInput, text="Campground Name:")
txtCampground = tk.Entry(frmInput)

lblsiteNumber = tk.Label(frmInput, text="Site Number:")
txtsiteNumber = tk.Entry(frmInput)

lblTown = tk.Label(frmInput, text="City:")
txtTown = tk.Entry(frmInput)

lblElectric = tk.Label(frmInput, text="Electric Service:")
txtElectric = tk.Entry(frmInput)

lblWater = tk.Label(frmInput, text="Water Service:")
txtWater = tk.Entry(frmInput)

lblAmenities = tk.Label(frmInput, text="Amenities:")
txtAmenities = tk.Entry(frmInput)

lblState = tk.Label(frmInput, text="State")
omChosen = tk.StringVar("")
omState = tk.OptionMenu(frmInput, omChosen, *State)






    ## display in a listbox
lblDisplay = tk.Label(frmDisplay, text="Favorite Rv Parks")
lstDisplay = tk.Listbox(frmDisplay)


    ## output a greeting
lblGreet = tk.Label(frmInput)
btnAddPlace = tk.Button(frmInput, text="Add Place")
btnAddPlace.bind("<Button-1>", lambda event: AddPlace(event))


    ## create a status bar
frmStatus = tk.Frame(gui, bd = 1, relief = "sunken")
lblStatus = tk.Label(frmStatus, text="STATUS: Ready...")


    ## load the widgets on the gui
gui.config(menu = mnMain)
tbMain.pack(fill = "both", padx = 2, pady = 5)
pnContent.pack(fill = "both", pady = 5, expand=1)
frmStatus.pack(side = "bottom", fill = "both")


tbbAddPlace.grid(row = 0, column = 0, padx = 3, pady = 5)
tbbDeletePlace.grid(row = 0, column = 1, padx = 3, pady = 5)
tbbEditPlace.grid(row = 0, column = 2, padx = 3, pady = 5)

lblName.grid(row = 0, column = 0)
txtName.grid(row = 0, column = 1)
lblCampground.grid(row = 2, column = 0)
txtCampground.grid(row = 2, column = 1)
lblsiteNumber.grid(row = 3, column = 0)
txtsiteNumber.grid(row = 3, column = 1)
lblElectric.grid(row = 4, column = 0)
txtElectric.grid(row = 4, column = 1)
lblWater.grid(row = 5, column = 0)
txtWater.grid(row = 5, column = 1)
lblAmenities.grid(row = 6, column = 0)
txtAmenities.grid(row = 6, column = 1)
lblTown.grid(row = 7, column = 0)
txtTown.grid(row = 7, column = 1)
lblState.grid(row=8, column=0)
omState.grid(row=8, column=1)


lblDisplay.pack()
lstDisplay.pack(fill="both", padx=7, pady=7, expand=1)


btnAddPlace.grid(row = 9, column = 0, columnspan=2, sticky="NSEW")


lblStatus.pack(side = "left", fill = "both")

    ### this sets up the key press: ctrl+shift+H to run the method
        ### for a simple keypress event: "Keypress-H"
gui.bind("<Control-Shift-KeyPress-A>", lambda event: AddPlace(event))


### trivial change to show github branch
x = 3


    ## start the gui
if __name__ == "__main__":
    gui.mainloop()


