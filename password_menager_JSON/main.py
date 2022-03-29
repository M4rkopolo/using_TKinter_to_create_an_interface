from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip        #copy text from selected field
import json

                                                                #password generator from old project
def password_generator():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(7, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def add():                                                      #saving password
    website = website_entry.get()                               #.get() used to read text from UI fiels
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,                                #new password is saved in dict
        }
    }
    if len(website) == 0 or len(password) == 0 or len(email) == 0:              #checking if fiels are filled
        messagebox.showinfo(title="info", message="Please, fill all info")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are detail entered:\n- Email:    {email}\n"
                                                              f"- Password:     {password}\nIs it ok to save?") #asking user if provided informations are correct
        if is_ok:
            try:                                                    #USING TRY:
                with open("emails.json", mode="r") as file:         #opening json are same as openin txt or CSV files
                    data = json.load(file)
            except FileNotFoundError:
                with open("emails.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                                                                     # updating old data witch new data
                data.update(new_data)
                with open("emails.json", mode="w") as file:
                                                                     # saving updated date
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def search():                                                       #searching password by the entered website
    website = website_entry.get()   
    try:                                                            #USING TRY:
        with open("emails.json", mode="r") as file:
            search_data = json.load(file)
            try:
                messagebox.showinfo(title=website,
                                    message=f"Email: {search_data[website]['email']}\nPassword: {search_data[website]['password']}")
                pyperclip.copy(search_data[website]['password'])
            except KeyError as error:                               
                messagebox.showinfo(title=website,
                                    message=f"Website {website} doesnt exist in database\n KeyError: {error}")
            finally:
                pass
    except FileNotFoundError:
        messagebox.showinfo(title=website,
                            message="The data file is missing")

window = Tk()                                                       #user interface
window.title("Password")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
email_label = Label(text="E-mail/User Name: ")
email_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entriess
website_entry = Entry(width=31)
website_entry.grid(column=1, row=1, )
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=5)
email_entry.insert(0, "szczygiel.mariusz@gmail.com")
password_entry = Entry(width=31)
password_entry.grid(column=1, row=3)

# Buttons
add_button = Button(text="Add", width=45, command=add)
add_button.grid(column=1, row=4, columnspan=2)
generate_password_button = Button(text="Generate Password", width=16, command=password_generator)
generate_password_button.grid(column=2, row=3)
search_button = Button(text="Search", width=16, command=search)
search_button.grid(column=2, row=1)

window.mainloop()
