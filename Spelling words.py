import tkinter as tk
from tkinter import Label
import pyttsx3


def spell_word():
    word = textbox.get()
    spelled_word = word+" . "," . ".join(word)+" . ",word+"."
    return spelled_word


def spell_text_of_box():
    spelled_word = spell_word()
    engine = pyttsx3.init()
    engine.say(spelled_word)
    engine.runAndWait()
        
def save_to_file():
    word = textbox.get()
    spelled_word = spell_word()
    engine = pyttsx3.init()
    engine.save_to_file(spelled_word, word+'.mp3')
    engine.runAndWait()

root = tk.Tk()
root.geometry("300x150")
root.title('Python Script')
label_title = Label(root,text="Spelling App!").pack()
textbox = tk.Entry(root)
textbox.place(x=90,y=20)
 
button_spell = tk.Button(root, text='Play', command=spell_text_of_box)
button_spell.place(x=100,y=50)

button_save = tk.Button(root, text='Save as mp3', command=save_to_file)
button_save.place(x=135,y=50)





root.mainloop()