from tkinter import *
#from tkinter import messagebox

OVERWEIGHT = 200
MIN_UNITS = 1
MAX_UNITS = 200


class Pet:
    def __init__(self, name=None, weight=0):
        self.name = name.title()
        self.weight = weight

    # def get_name(self, pet_name):
    #     while True:
    #         if len(pet_name) > 10:
    #             messagebox('Please enter a shorter name')
    #         elif len(pet_name) < 1:
    #             messagebox('Gang, enter somethin')
    #         else: 
    #             break

    def feed(self, units):
        if self.weight > 0:
            self.weight += units
        return self.weight

    def exercise(self, units):
        if self.weight > 0:
            self.weight -= units
        return self.weight

    def __str__(self):
        if self.weight <= 0:
            return f"RIP {self.name}"
        elif self.weight > OVERWEIGHT:
            return f"{self.name} :-("
        else:
            return f"{self.name} now weighs {self.weight}"


class PetGUI:
    def __init__(self, root):
        self.root = root 
        self.root.title('Virtual Pet')
        self.root.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.root.columnconfigure((0, 1), weight=1)
        # self.pet_class = Pet()
        self.pet = None
        
        Label(root, text='Pet Name').grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
        Label(root, text='Starting Weight').grid(row=1,column=0,padx=10,pady=10,sticky='nsew')

        self.pet_name_entry = Entry(root)
        self.pet_name_entry.grid(row=0, column=1, sticky='w')

        self.starting_weight_entry = Entry(root)
        self.starting_weight_entry.grid(row=1, column=1, sticky='w')

        Button(root, text='Create Pet', command=None).grid(row=2,columnspan=2)

        Label(root, text='Units').grid(row=3,column=0,padx=10,pady=10,sticky='nsew')

        self.unit_entry = Entry(root)
        self.unit_entry.grid(row=3, column=1, sticky='w')

        Button(root, text='Feed', command=None).grid(row=4,column=0)
        Button(root, text='Exercise', command=None).grid(row=4,column=1)

        self.result_lbl = Label(root, text='Something(placeholder)').grid(row=5,columnspan=2,padx=10,pady=10,sticky='nsew')

root = Tk()
app = PetGUI(root)
root.mainloop()