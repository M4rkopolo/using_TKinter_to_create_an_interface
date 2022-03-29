from tkinter import *
window = Tk()                                   #create window instance of Tk() class
window.title("Miles to Kilometers converter")   
window.config(padx=10, pady=10)                 #size of the window
result = 0
def convert():
    result = round(int(kilometers_input.get())*1.609)   #complicated mathematical calculations
    label_result.config(text=result)                

button = Button(width=10, text="convert", command=convert)
button.grid(column=1, row=2)                            #grid method to locate the object

kilometers_input = Entry(width=10)
kilometers_input.insert(END, string="0")
kilometers_input.grid(column=1, row=0)

label_Km = Label(text="Km")
label_Km.grid(column=2, row=1)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_miles = Label(text="miles")
label_miles.grid(column=2, row=0)

label_result = Label(text="0")
label_result.grid(column=1, row=1)

window.mainloop()