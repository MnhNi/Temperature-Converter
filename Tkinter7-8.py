from tkinter import * 

ABS_ZERO_FARENHEIT = -459.67
ABS_ZERO_CELSIUS = -273.15
FONT_MAIN_TITLE = "Verdana 16 bold"
FONT_HEADING = "Verdana 12 bold"
FONT_DEFAULT = "Verdana 12"

class TemperatureConverter:

    def convert_to_c(self, temp):
        try:
            temp = float(temp)
            if temp >= ABS_ZERO_FARENHEIT:
                result = (float(temp) - 32) * 5 / 9
                return f'{result:.1f} degrees Centigrade'
            else:
                return'Temperature too low'
        except ValueError:
            return 'Please enter a number'
    
    def convert_to_f(self,temp):
        try:
            temp = float(temp)
            if temp >= ABS_ZERO_CELSIUS:
                result = float(temp) * (9 / 5) + 32
                return f'{result:.1f} degrees Fahrenheit'
            else:
                return'Temperature too low'
        except ValueError:
            return 'Please enter a number'
    
class ConverterGUI:
    
    def __init__(self, root):

        self.converter = TemperatureConverter()

        self.root = root
        self.root.title('Temperature Converter')
        # self.root.geometry('400x150')

        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky='nsew')

        self.frames = {}
        self.frames['MainFrame'] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_c_frame()
        self.frames["to_fFrame"] = self.create_to_f_frame()

        self.show_frame("MainFrame")
    
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
    

    def create_main_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0,column=0,sticky='nsew')
        frame.columnconfigure((0, 1), weight=1)
        frame.rowconfigure((0, 1), weight=1)
        
        Label(frame, font=FONT_MAIN_TITLE, text='Temperature Converter').grid(row=0,columnspan=2,padx=10,pady=10,sticky='nsew')

        Button(frame, text='To Centigrade', bg='yellow', font=FONT_HEADING, command=lambda: self.show_frame('to_cFrame')).grid(row=1,column=0, padx=10, pady=10, sticky='nsew')

        Button(frame, text='To Fahrenheit', bg='pink', font=FONT_HEADING, command=lambda: self.show_frame('to_fFrame')).grid(row=1,column=1, padx=10, pady=10, sticky='nsew')

        return frame
    
    def reset(self, entry, label):
        entry.delete(0,END)
        label.configure(text='')

    def to_c(self):
        result = self.converter.convert_to_c(self.fahrenheit_box.get())
        self.result_c_lbl.configure(text=result)

    def create_to_c_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0,column=0,sticky='nsew')
        frame.columnconfigure((0, 1, 2), weight=1)
        frame.rowconfigure((0, 1, 2), weight=1)

        Label(frame, font=FONT_MAIN_TITLE, text='Enter the Temperature in Fahrenheit').grid(row=0,columnspan=3,padx=10,pady=10,sticky='nsew')
        
        self.fahrenheit_box = Entry(frame)
        self.fahrenheit_box.grid(row=1,columnspan=3, sticky='nsew')

        Button(frame, text='Calculate',font=FONT_DEFAULT, command=self.to_c).grid(row=2,column=0,sticky='nsew')

        Button(frame, text='Back',font=FONT_DEFAULT, command=lambda: self.show_frame("MainFrame")).grid(row=2,column=1,sticky='nsew')

        Button(frame, text='Reset',font=FONT_DEFAULT, command=lambda: self.reset(self.fahrenheit_box,self.result_c_lbl)).grid(row=2,column=2,sticky='nsew')

        self.result_c_lbl = Label(frame, font=FONT_DEFAULT, text='')
        self.result_c_lbl.grid(row=3,columnspan=3,sticky='nsew',padx=10,pady=10)

        return frame
    
    def to_f(self):
        result = self.converter.convert_to_f(self.centigrade_box.get())
        self.result_f_lbl.configure(text=result)


    def create_to_f_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0,column=0,sticky='nsew')
        frame.columnconfigure((0, 1, 2), weight=1)
        frame.rowconfigure((0, 1, 2), weight=1)

        Label(frame, font=FONT_MAIN_TITLE, text='Enter the Temperature in Centigrade').grid(row=0,columnspan=3,padx=10,pady=10,sticky='nsew')
        
        self.centigrade_box = Entry(frame)
        self.centigrade_box.grid(row=1,columnspan=3, sticky='nsew')

        Button(frame, text='Calculate',font=FONT_DEFAULT, command=self.to_f).grid(row=2,column=0,sticky='nsew')

        Button(frame, text='Back',font=FONT_DEFAULT, command=lambda: self.show_frame("MainFrame")).grid(row=2,column=1,sticky='nsew')

        Button(frame, text='Reset',font=FONT_DEFAULT, command=lambda: self.reset(self.centigrade_box, self.result_f_lbl)).grid(row=2,column=2,sticky='nsew')

        self.result_f_lbl = Label(frame, font=FONT_DEFAULT, text='')
        self.result_f_lbl.grid(row=3,columnspan=3,sticky='nsew',padx=10,pady=10)

        return frame

root = Tk()
app = ConverterGUI(root)
root.mainloop()