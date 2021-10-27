import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
word = 'Hello'
spelled_word = word+" . "," . ".join(word)+" . ",word+"."

print (spelled_word)

root.mainloop()