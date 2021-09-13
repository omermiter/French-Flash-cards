from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
good_word = []
count = 0
word_data = None
try:
    data = pandas.read_csv("./data/words.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

fr = data["French"].tolist()
eng = data["English"].tolist()
def flip(index):
    global good_word
    canvas.itemconfig(card, image=back)
    canvas.itemconfig(title, text="English", fill = "white")
    eng = data["English"].tolist()
    canvas.itemconfig(word, text= eng[index], fill = "white")
    right()


def change_word(bool):
    global timer, good_word, count,fr, eng
    window.after_cancel(timer)
    canvas.itemconfig(card, image= image)
    canvas.itemconfig(title, text="French", fill = "black")
    text = random.choice(fr)
    canvas.itemconfig(word, text = text , fill = "black")
    good_word.append(text)
    good_word.append(eng[fr.index(text)])
    index = fr.index(text)
    if bool == True:
        good_word = []
        fr.remove(text)
        print(len(fr))
    elif bool == False:
        right()
    timer = window.after(3000, flip, index)

def right():
    global good_word,count, word_data
    one = good_word[0]
    two = good_word[1]
    good_word = []
    if count != 1:
        word_dict = {"French": [one], "English": [two]}
        word_data = pandas.DataFrame(word_dict)
        count += 1
    else:
        new_line = {"French": one, "English": two}
        word_data = word_data.append(new_line, ignore_index=True)

    word_data.to_csv("./data/words.csv")








#---------------------UI---------------------#
window = Tk()
window.title("flashy")
window.config(bg = BACKGROUND_COLOR, padx=50, pady =50)
image = PhotoImage(file= "./images/card_front.png")
canvas = Canvas(width = 1000, height = 570, bg= BACKGROUND_COLOR, highlightthickness = 0)
card = canvas.create_image(500, 275, image= image)
back = PhotoImage(file= "./images/card_back.png")
title = canvas.create_text(480, 150, text= "Title", font= ("Ariel", 40, "italic"))
word = canvas.create_text(480, 263, text = "Word", font= ("Ariel", 60, "bold"))
canvas.grid(column = 0 , row = 0, columnspan = 2)
c_image = PhotoImage(file= "./images/right.png")
check_button = Button(image= c_image, highlightthickness = 0, command =lambda: change_word(True))
check_button.grid(column = 1, row = 1)
w_image = PhotoImage(file= "./images/wrong.png")
wrong_button = Button(image= w_image, highlightthickness = 0, command =lambda:change_word(False))
wrong_button.grid(column= 0, row =1)
timer = window.after(0, lambda: change_word(None))
window.mainloop()