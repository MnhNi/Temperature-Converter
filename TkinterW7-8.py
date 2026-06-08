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
    
