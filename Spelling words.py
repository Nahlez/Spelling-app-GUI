import tkinter as tk
import pyttsx3

def get_text_of_box():
    word = textbox.get()
    spelled_word = word+" . "," . ".join(word)+" . ",word+"."
    engine = pyttsx3.init()
    engine.say(spelled_word)
    engine.runAndWait()
        

root = tk.Tk()
root.geometry("300x150")
textbox = tk.Entry(root)
textbox.pack()
 
button = tk.Button(root, text='Spell', command=get_text_of_box).pack()




root.mainloop()