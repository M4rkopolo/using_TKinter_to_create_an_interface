BACKGROUND_COLOR = "#B1DDC6"
import pandas
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
import math

known_list = []
unknown_list = []
timer = None

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#create a new flash card 
def new_card():
    global known_list, unknown_list

    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
    data_list_words = [[value["French"],value["English"]] for value in data_dict[1:5:]]             #create a list from data in csv file
    unknown_list = [strange_word for strange_word in data_list_words if strange_word not in known_list] #prepare list of unknown words,
    try:
        random_word = choice(unknown_list)                                                          #shuffle the words
        canvas.itemconfig(word, text = random_word[1])
        return random_word
    except IndexError:
        canvas.itemconfig(word, text = "You know every word")
    except UnboundLocalError:
        canvas.itemconfig(word, text = "You know every word")

def flip_card():                                                #change image, bg color, word from the list
    canvas.itemconfig(language, text= "English", fill="black")
    canvas.itemconfig(word, text= random_word[1], fill="black")
    canvas.itemconfig(card_image , image = card_back_img)
    
def known():                                                    #add word to knowing list after click green btn
    global known_list
    known_list.append(new_card())
    print(known_list)
    
def unknown():                                                  #add word to unknowe list after click red btn  
    new_card()
    print(unknown_list)
    
                                    #user interface
window.after(1000, func=flip_card)
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")

card_image = canvas.create_image(400, 263, image=card_back_img)
language = canvas.create_text(400,150, text= "Language", font=("arial", 40, "italic"))
word = canvas.create_text(400,263, text= "word", font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
right_img = PhotoImage(file="./images/right.png")

known_button = Button(image=right_img, command=known)
known_button.grid(column=0, row=1)
wrong = PhotoImage(file="./images/wrong.png")

unknown_button = Button(image = wrong, command=unknown)
unknown_button .grid(column=1, row=1)

window.mainloop()
