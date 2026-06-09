from tkinter import * 
from tkinter import ttk

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
                return f'{result:.lf} degrees Centigrade'
            else:
                return'Temperature too low'
        except ValueError:
            return 'Please enter a number'
    
    def convert_to_f(self,temp):
        try:
            temp = float(temp)
            if temp >= ABS_ZERO_CELSIUS:
                result = float(temp) * (9 / 5) + 32
                return f'{result:.lf} degrees Fahrenheit'
            else:
                return'Temperature too low'
        except ValueError:
            return 'Please enter a number'
    
class ConverterGUI:
    
    def __init__(self, root):

        self.converter = TemperatureConverter()

        self.root = root
        self.root.title('Temperature Converter')
        self.root.geometry('400x150')

        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky='nsew')

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
        
        Label(frame, font=FONT_MAIN_TITLE, text='Temperature Converter').grid(row=0,columnspan=2,padx=10,pady=10,sticky='nsew')

        Button(frame, text='To Centigrade', bg='yellow', font=FONT_HEADING, command=lambda: self.show_frame('to_cFrame')).grid(row=1,column=0, padx=10, pady=10, sticky='nsew')

        Button(frame, text='To Fahrenheit', bg='pink', font=FONT_HEADING, command=lambda: self.show_frame('to_fFrame')).grid(row=1,column=1, padx=10, pady=10, sticky='nsew')

        return frame
    
    def create_to_c_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0,column=0,sticky='nsew')

        Label(frame, font=FONT_MAIN_TITLE, text='Enter the Temperature in Fahrenheit').grid(row=0,columnspan=3,padx=10,pady=10,sticky='nsew')
        fahrenheit_box = Entry(frame).grid(row=1,columnspan=3)

        Button(frame, text='To Centigrade', bg='yellow', font=FONT_HEADING, command=lambda: self.show_frame('to_cFrame')).grid(row=2,column=0,sticky='nsew')
        
    def create_to_f_frame(self):

    