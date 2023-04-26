# Import Module
from tkinter import *
from tkinter import messagebox

# create UC_main window
UC_main = Tk()

# title for main window
UC_main.title("Units Converter")
# width x height
UC_main.geometry('600x600')


def open_window1():

    length_main = Toplevel(UC_main)
    length_main.resizable(False, False)
    length_main.title("  Units Converter - Length  ")

    label = Label(length_main, text="      Units Converter - Length      ", font=("Arial", 15))
    label.grid(row=0)

    row1 = Frame(length_main)
    row1.grid(row=1)
    row1.columnconfigure(0, weight=3)
    row1.columnconfigure(1, weight=1)
    row1.columnconfigure(2, weight=2)

    label1 = Label(row1, text="From: ")
    label1.grid(column=0, row=0, sticky=W)

    label2 = Label(row1, text="To:")
    label2.grid(column=0, row=1, sticky=W)

    entry1 = Entry(row1, width=20)
    entry2 = Entry(row1, width=20)
    entry1.grid(column=1, row=0, sticky=W)
    entry2.grid(column=1, row=1, sticky=W)

    options = ["Millimeter", "Centimeter", "Decimeter", "Meter", "Kilometer", "Inch", "Foot", "Yard", "Mile"]

    selected_option = StringVar()
    selected_option.set(options[0])
    option_menu = OptionMenu(row1, selected_option, *options)
    option_menu.grid(column=2, row=0, sticky=E)

    selected_option1 = StringVar()
    selected_option1.set(options[0])
    option_menu = OptionMenu(row1, selected_option1, *options)
    option_menu.grid(column=2, row=1, sticky=E)

    def call_back():
        length_main.destroy()

    def convert():
        from_unit = selected_option.get()
        to_unit = selected_option1.get()

        # conversion formulas
        conversions = {
            "Millimeter": {"Millimeter": 1, "Centimeter": 0.1, "Decimeter": 0.01, "Meter": 0.001, "Kilometer": 0.000001,
                           "Inch": 0.03937, "Foot": 0.003281, "Yard": 0.001094, "Mile": 0.0000006214},
            "Centimeter": {"Millimeter": 10, "Centimeter": 1, "Decimeter": 0.1, "Meter": 0.01, "Kilometer": 0.00001,
                           "Inch": 0.3937, "Foot": 0.03281, "Yard": 0.01094, "Mile": 0.000006214},
            "Decimeter": {"Millimeter": 100, "Centimeter": 10, "Decimeter": 1, "Meter": 0.1, "Kilometer": 0.0001,
                          "Inch": 3.937, "Foot": 0.3281, "Yard": 0.1094, "Mile": 0.00006214},
            "Meter": {"Millimeter": 1000, "Centimeter": 100, "Decimeter": 10, "Meter": 1, "Kilometer": 0.001,
                      "Inch": 39.37, "Foot": 3.281, "Yard": 1.094, "Mile": 0.0006214},
            "Kilometer": {"Millimeter": 1000000, "Centimeter": 100000, "Decimeter": 10000, "Meter": 1000,
                          "Kilometer": 1, "Inch": 39370, "Foot": 3281, "Yard": 1094, "Mile": 0.6214},
            "Inch": {"Millimeter": 25.4, "Centimeter": 2.54, "Decimeter": 0.254, "Meter": 0.0254,
                     "Kilometer": 0.0000254, "Inch": 1, "Foot": 0.08333, "Yard": 0.02778, "Mile": 0.00001578},
            "Foot": {"Millimeter": 304.8, "Centimeter": 30.48, "Decimeter": 3.048, "Meter": 0.3048,
                     "Kilometer": 0.0003048, "Inch": 12, "Foot": 1, "Yard": 0.3333, "Mile": 0.0001894},
            "Yard": {"Millimeter": 914.4, "Centimeter": 91.44, "Decimeter": 9.144, "Meter": 0.9144,
                     "Kilometer": 0.0009144, "Inch": 36, "Foot": 3, "Yard": 1, "Mile": 0.0005682},
            "Mile": {"Millimeter": 1609344, "Centimeter": 160934.4, "Decimeter": 16093.44, "Meter": 1609.344,
                     "Kilometer": 1.609344}
        }

        try:
            from_value = float(entry1.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number in the 'From' field")
            return

            # check if the 'From' field is empty
        if not entry1.get():
            messagebox.showerror("Error", "Please enter a value in the 'From' field")
            return

        to_value = from_value * conversions[from_unit][to_unit]
        to_value = "{:.2f}".format(to_value)
        entry2.delete(0, END)
        entry2.insert(0, str(to_value))

    convert_button = Button(length_main, text="Convert", command=convert)
    convert_button.grid(row=2)

    back_button = Button(length_main, text="Back", command=call_back)
    back_button.grid(row=3, pady=2)

    length_main.mainloop()


def open_window2():
    weight_main = Toplevel(UC_main)
    weight_main.resizable(False, False)
    weight_main.title("  Units Converter - Weight  ")

    label = Label(weight_main, text="      Units Converter - Weight      ", font=("Arial", 15))
    label.grid(row=0)

    row1 = Frame(weight_main)
    row1.grid(row=1)
    row1.columnconfigure(0, weight=3)
    row1.columnconfigure(1, weight=1)
    row1.columnconfigure(2, weight=2)

    label1 = Label(row1, text="From: ")
    label1.grid(column=0, row=0, sticky=W)

    label2 = Label(row1, text="To:")
    label2.grid(column=0, row=1, sticky=W)

    entry1 = Entry(row1, width=20)
    entry2 = Entry(row1, width=20)
    entry1.grid(column=1, row=0, sticky=W)
    entry2.grid(column=1, row=1, sticky=W)

    options = ["Milligram", "Gram", "Kilogram", "Pound", "Ounce"]

    selected_option = StringVar()
    selected_option.set(options[0])
    option_menu = OptionMenu(row1, selected_option, *options)
    option_menu.grid(column=2, row=0, sticky=E)

    selected_option1 = StringVar()
    selected_option1.set(options[0])
    option_menu = OptionMenu(row1, selected_option1, *options)
    option_menu.grid(column=2, row=1, sticky=E)

    def convert():
        from_unit = selected_option.get()
        to_unit = selected_option1.get()

        conversions = {
            "Milligram": {"Milligram": 1, "Gram": 0.001, "Kilogram": 0.000001, "Pound": 0.00000220462,
                          "Ounce": 0.000035274},
            "Gram": {"Milligram": 1000, "Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274},
            "Kilogram": {"Milligram": 1000000, "Gram": 1000, "Kilogram": 1, "Pound": 2.20462, "Ounce": 35.274},
            "Pound": {"Milligram": 453592, "Gram": 453.592, "Kilogram": 0.453592, "Pound": 1, "Ounce": 16},
            "Ounce": {"Milligram": 28349.5, "Gram": 28.3495, "Kilogram": 0.0283495, "Pound": 0.0625, "Ounce": 1}
        }

        try:
            from_value = float(entry1.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number in the 'From' field")
            return

            # check if the 'From' field is empty
        if not entry1.get():
            messagebox.showerror("Error", "Please enter a value in the 'From' field")
            return

        to_value = from_value * conversions[from_unit][to_unit]
        to_value = "{:.2f}".format(to_value)
        entry2.delete(0, END)
        entry2.insert(0, str(to_value))

    def call_back():
        weight_main.destroy()

    convert_button = Button(weight_main, text="Convert", command=convert)
    convert_button.grid(row=2)

    back_button = Button(weight_main, text="Back", command=call_back)
    back_button.grid(row=3, pady=2)

    weight_main.mainloop()


def open_window3():
    area_main = Toplevel(UC_main)
    area_main.resizable(False, False)
    area_main.title("      Units Converter - Area      ")

    label = Label(area_main, text="      Units Converter - Area      ", font=("Arial", 15))
    label.grid(row=0)

    row1 = Frame(area_main)
    row1.grid(row=1)
    row1.columnconfigure(0, weight=3)
    row1.columnconfigure(1, weight=1)
    row1.columnconfigure(2, weight=2)

    label1 = Label(row1, text="From: ")
    label1.grid(column=0, row=0, sticky=W)

    label2 = Label(row1, text="To:")
    label2.grid(column=0, row=1, sticky=W)

    entry1 = Entry(row1, width=20)
    entry2 = Entry(row1, width=20)
    entry1.grid(column=1, row=0, sticky=W)
    entry2.grid(column=1, row=1, sticky=W)

    options = ["Square Kilometer", "Square Meter", "Square Centimeter", "Square Mile", "Acre", 
               "Square Feet", "Square Inch"]

    selected_option = StringVar()
    selected_option.set(options[0])
    option_menu = OptionMenu(row1, selected_option, *options)
    option_menu.grid(column=2, row=0, sticky=E)

    selected_option1 = StringVar()
    selected_option1.set(options[0])
    option_menu = OptionMenu(row1, selected_option1, *options)
    option_menu.grid(column=2, row=1, sticky=E)

    def call_back():
        area_main.destroy()

    def convert():
        from_unit = selected_option.get()
        to_unit = selected_option1.get()

        conversions = {
            "Square Kilometer": {
                "Square Meter": 1000000,
                "Square Centimeter": 10000000000,
                "Square Mile": 0.386102,
                "Acre": 247.105,
                "Square Feet": 10763910,
                "Square Inch": 1550003100,
            },
            "Square Meter": {
                "Square Kilometer": 0.000001,
                "Square Centimeter": 10000,
                "Square Mile": 0.000000386102,
                "Acre": 0.000247105,
                "Square Feet": 10.763910,
                "Square Inch": 1550.003100,
            },
            "Square Centimeter": {
                "Square Kilometer": 0.00000001,
                "Square Meter": 0.0001,
                "Square Mile": 0.000000000386102,
                "Acre": 0.000000247105,
                "Square Feet": 0.0010763910,
                "Square Inch": 0.1550003100,
            },
            "Square Mile": {
                "Square Kilometer": 2.58999,
                "Square Meter": 2589988.11,
                "Square Centimeter": 25899881103.36,
                "Acre": 640,
                "Square Feet": 27878400,
                "Square Inch": 4014489600,
            },
            "Acre": {
                "Square Kilometer": 0.00404686,
                "Square Meter": 4046.86,
                "Square Centimeter": 40468600,
                "Square Mile": 0.0015625,
                "Square Feet": 43560,
                "Square Inch": 6272640,
            },
            "Square Feet": {
                "Square Kilometer": 0.00000009290304,
                "Square Meter": 0.09290304,
                "Square Centimeter": 929.0304,
                "Square Mile": 0.00000003587006,
                "Acre": 0.00002295684,
                "Square Inch": 144,
            },
            "Square Inch": {
                "Square Kilometer": 0.00000000064516,
                "Square Meter": 0.00064516,
                "Square Centimeter": 6.4516,
                "Square Mile": 0.000000000249097,
                "Acre": 0.0000001594225,
                "Square Feet": 0.00694444,
            },
        }

        try:
            from_value = float(entry1.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number in the 'From' field")
            return

            # check if the 'From' field is empty
        if not entry1.get():
            messagebox.showerror("Error", "Please enter a value in the 'From' field")
            return

        to_value = from_value * conversions[from_unit][to_unit]
        to_value = "{:.2f}".format(to_value)
        entry2.delete(0, END)
        entry2.insert(0, str(to_value))

    convert_button = Button(area_main, text="Convert", command=convert)
    convert_button.grid(row=2)

    back_button = Button(area_main, text="Back", command=call_back)
    back_button.grid(row=3, pady=2)

    area_main.mainloop()
    
    
def open_window4():
    data_main = Toplevel(UC_main)
    data_main.resizable(False, False)
    data_main.title("      Units Converter - Data      ")

    label = Label(data_main, text="      Units Converter - Data      ", font=("Arial", 15))
    label.grid(row=0)

    row1 = Frame(data_main)
    row1.grid(row=1)
    row1.columnconfigure(0, weight=3)
    row1.columnconfigure(1, weight=1)
    row1.columnconfigure(2, weight=2)

    label1 = Label(row1, text="From: ")
    label1.grid(column=0, row=0, sticky=W)

    label2 = Label(row1, text="To:")
    label2.grid(column=0, row=1, sticky=W)

    entry1 = Entry(row1, width=20)
    entry2 = Entry(row1, width=20)
    entry1.grid(column=1, row=0, sticky=W)
    entry2.grid(column=1, row=1, sticky=W)

    options = ["Bit", "Byte", "Kilobyte", "Megabyte", "Terabyte"]

    selected_option = StringVar()
    selected_option.set(options[0])
    option_menu = OptionMenu(row1, selected_option, *options)
    option_menu.grid(column=2, row=0, sticky=E)

    selected_option1 = StringVar()
    selected_option1.set(options[0])
    option_menu = OptionMenu(row1, selected_option1, *options)
    option_menu.grid(column=2, row=1, sticky=E)

    def call_back():
        data_main.destroy()

    def convert():
        from_unit = selected_option.get()
        to_unit = selected_option1.get()

        conversions = {
            "Bit": {
                "Bit": 1,
                "Byte": 0.125,
                "Kilobyte": 0.00012207,
                "Megabyte": 1.1921e-7,
                "Terabyte": 1.1642e-10
            },
            "Byte": {
                "Bit": 8,
                "Byte": 1,
                "Kilobyte": 0.00097656,
                "Megabyte": 9.5367e-7,
                "Terabyte": 9.3132e-10
            },
            "Kilobyte": {
                "Bit": 8192,
                "Byte": 1024,
                "Kilobyte": 1,
                "Megabyte": 0.00097656,
                "Terabyte": 9.5367e-7
            },
            "Megabyte": {
                "Bit": 8.389e+6,
                "Byte": 1.049e+6,
                "Kilobyte": 1024,
                "Megabyte": 1,
                "Terabyte": 0.00097656
            },
            "Terabyte": {
                "Bit": 8.796e+9,
                "Byte": 1.1e+9,
                "Kilobyte": 1.074e+6,
                "Megabyte": 1048.576,
                "Terabyte": 1
            }
        }

        try:
            from_value = float(entry1.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number in the 'From' field")
            return

            # check if the 'From' field is empty
        if not entry1.get():
            messagebox.showerror("Error", "Please enter a value in the 'From' field")
            return

        to_value = from_value * conversions[from_unit][to_unit]
        to_value = "{:.2f}".format(to_value)
        entry2.delete(0, END)
        entry2.insert(0, str(to_value))

    convert_button = Button(data_main, text="Convert", command=convert)
    convert_button.grid(row=2)

    back_button = Button(data_main, text="Back", command=call_back)
    back_button.grid(row=3, pady=2)

    data_main.mainloop()
    
    
def open_window5():
    time_main = Toplevel(UC_main)
    time_main.resizable(False, False)
    time_main.title("      Units Converter - Time      ")

    label = Label(time_main, text="      Units Converter - Time      ", font=("Arial", 15))
    label.grid(row=0)

    row1 = Frame(time_main)
    row1.grid(row=1)
    row1.columnconfigure(0, weight=3)
    row1.columnconfigure(1, weight=1)
    row1.columnconfigure(2, weight=2)

    label1 = Label(row1, text="From: ")
    label1.grid(column=0, row=0, sticky=W)

    label2 = Label(row1, text="To:")
    label2.grid(column=0, row=1, sticky=W)

    entry1 = Entry(row1, width=20)
    entry2 = Entry(row1, width=20)
    entry1.grid(column=1, row=0, sticky=W)
    entry2.grid(column=1, row=1, sticky=W)

    options = ["Second", "Minute", "Hour", "Day", "Week", "Month", "Year"]

    selected_option = StringVar()
    selected_option.set(options[0])
    option_menu = OptionMenu(row1, selected_option, *options)
    option_menu.grid(column=2, row=0, sticky=E)

    selected_option1 = StringVar()
    selected_option1.set(options[0])
    option_menu = OptionMenu(row1, selected_option1, *options)
    option_menu.grid(column=2, row=1, sticky=E)

    def call_back():
        time_main.destroy()

    def convert():
        from_unit = selected_option.get()
        to_unit = selected_option1.get()

        # conversion formulas
        conversions = {
            "Hour": {"Hour": 1, "Minute": 60, "Second": 3600, "Day": 1 / 24, "Week": 1 / 168, 
                     "Month": 1 / 720, "Year": 1 / 8760},
            "Minute": {"Minute": 1, "Hour": 1 / 60, "Second": 60, "Day": 1 / 1440, "Week": 1 / 10080, 
                       "Month": 1 / 43200,
                       "Year": 1 / 525600},
            "Second": {"Second": 1, "Hour": 1 / 3600, "Minute": 1 / 60, "Day": 1 / 86400, "Week": 1 / 604800, 
                       "Month": 1 / 2592000,
                       "Year": 1 / 31536000},
            "Day": {"Day": 1, "Hour": 24, "Minute": 1440, "Second": 86400, "Week": 1 / 7, "Month": 1 / 30.44, 
                    "Year": 1 / 365},
            "Week": {"Week": 1, "Hour": 168, "Minute": 10080, "Second": 604800, "Day": 7, "Month": 1 / 4.345,
                     "Year": 1 / 52.143},
            "Month": {"Month": 1, "Hour": 720, "Minute": 43200, "Second": 2592000, "Day": 30.44, "Week": 4.345, 
                      "Year": 1 / 12},
            "Year": {"Year": 1, "Hour": 8760, "Minute": 525600, "Second": 31536000, "Day": 365, "Week": 52.143, 
                     "Month": 12}
        }

        try:
            from_value = float(entry1.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number in the 'From' field")
            return

            # check if the 'From' field is empty
        if not entry1.get():
            messagebox.showerror("Error", "Please enter a value in the 'From' field")
            return

        to_value = from_value * conversions[from_unit][to_unit]
        to_value = "{:.2f}".format(to_value)
        entry2.delete(0, END)
        entry2.insert(0, str(to_value))

    convert_button = Button(time_main, text="Convert", command=convert)
    convert_button.grid(row=2)

    back_button = Button(time_main, text="Back", command=call_back)
    back_button.grid(row=3, pady=2)

    time_main.mainloop()
    
    
def open_window6():
    temp_main = Toplevel(UC_main)
    temp_main.resizable(False, False)
    temp_main.title("  Units Converter - Temperature  ")

    label = Label(temp_main, text="  Units Converter - Temperature  ", font=("Arial", 15))
    label.grid(row=0)

    row1 = Frame(temp_main)
    row1.grid(row=1)
    row1.columnconfigure(0, weight=3)
    row1.columnconfigure(1, weight=1)
    row1.columnconfigure(2, weight=2)

    label1 = Label(row1, text="From: ")
    label1.grid(column=0, row=0, sticky=W)

    label2 = Label(row1, text="To:")
    label2.grid(column=0, row=1, sticky=W)

    entry1 = Entry(row1, width=20)
    entry2 = Entry(row1, width=20)
    entry1.grid(column=1, row=0, sticky=W)
    entry2.grid(column=1, row=1, sticky=W)

    options = ["Fahrenheit", "Celsius"]

    selected_option = StringVar()
    selected_option.set(options[0])
    option_menu = OptionMenu(row1, selected_option, *options)
    option_menu.grid(column=2, row=0, sticky=E)

    selected_option1 = StringVar()
    selected_option1.set(options[0])
    option_menu = OptionMenu(row1, selected_option1, *options)
    option_menu.grid(column=2, row=1, sticky=E)

    def call_back():
        temp_main.destroy()

    def convert():
        from_unit = selected_option.get()
        to_unit = selected_option1.get()

        try:
            from_value = float(entry1.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number in the 'From' field")
            return

            # check if the 'From' field is empty
        if not entry1.get():
            messagebox.showerror("Error", "Please enter a value in the 'From' field")
            return

        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            c = float(entry1.get())
            f = c * 9 / 5 + 32
            f = "{:.2f}".format(f)
            entry2.delete(0, END)
            entry2.insert(0, str(f))
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            f = float(entry1.get())
            c = (f - 32) * 5 / 9
            c = "{:.2f}".format(c)
            entry2.delete(0, END)
            entry2.insert(0, str(c))
        elif from_unit == "Celsius" and to_unit == "Celsius":
            entry2.delete(0, END)
            entry2.insert(0, str(entry1.get()))
        elif from_unit == "Fahrenheit" and to_unit == "Fahrenheit":
            entry2.delete(0, END)
            entry2.insert(0, str(entry1.get()))

    convert_button = Button(temp_main, text="Convert", command=convert)
    convert_button.grid(row=2)

    back_button = Button(temp_main, text="Back", command=call_back)
    back_button.grid(row=3, pady=2)

    temp_main.mainloop()
    

label_main = Label(UC_main, text="Units Converter", font=("Arial", 20))
label_main.pack(side="top", fill="x", padx=20, pady=20)

frame1 = Frame(UC_main)
frame2 = Frame(UC_main)


button1 = Button(frame1, text="Length", command=open_window1)
button2 = Button(frame1, text="Weight", command=open_window2)
button3 = Button(frame1, text="Area", command=open_window3)
button4 = Button(frame2, text="Data", command=open_window4)
button5 = Button(frame2, text="Time", command=open_window5)
button6 = Button(frame2, text="Temperature", command=open_window6)


button1.pack(side="left", padx=20, pady=20)
button2.pack(side="left", padx=20, pady=20)
button3.pack(side="left", padx=20, pady=20)
button4.pack(side="left", padx=20, pady=20)
button5.pack(side="left", padx=20, pady=20)
button6.pack(side="left", padx=20, pady=20)

frame1.pack(side="top", padx=20, pady=20)
frame2.pack(side="top", padx=20, pady=20)


def exit_app():
    UC_main.destroy()


exit_button = Button(UC_main, text="Exit", command=exit_app)
exit_button.pack(pady=20, side="bottom")

# execute main window
UC_main.mainloop()
