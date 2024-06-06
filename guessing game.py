import tkinter as tk
import random

# Initialize the Tkinter root window
win = tk.Tk()
win.geometry('500x500')
win.title('Joffre Guessing Game')

# Generate a random number for the guessing game
num = random.randint(1, 50)

# Initialize Tkinter variables
hint = tk.StringVar()
guess = tk.IntVar()
score = tk.IntVar()
final_score = tk.IntVar()

# Define the main function for the game logic
def fun():
    x = guess.get()
    final_score.set(score.get())
    if score.get() > 0:
        if x > 50 or x < 1:
            hint.set('Please guess a number between 1 and 50')
        elif num == x:
            hint.set('Congratulations, you won!')
        elif num > x:
            hint.set('Your guess was too low, guess again')
        elif num < x:
            hint.set('Your guess was too high, guess again')
        score.set(score.get() - 1)
        final_score.set(score.get())
    else:
        hint.set('Game over, you lost')

# Create the entry boxes
tk.Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=tk.GROOVE).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
tk.Entry(win, textvariable=hint, width=50, font=('Courier', 15), relief=tk.GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=tk.CENTER)
tk.Entry(win, textvariable=final_score, width=2, font=('Ubuntu', 24), relief=tk.GROOVE).place(relx=0.61, rely=0.85, anchor=tk.CENTER)

# Create the labels
tk.Label(win, text='I challenge you to guess the number', font=('Courier', 24)).place(relx=0.5, rely=0.9, anchor=tk.CENTER)
tk.Label(win, text='Score out of 5', font=('Courier', 25)).place(relx=0.3, rely=0.85, anchor=tk.CENTER)

# Create the button
tk.Button(win, width=8, text='CHECK', font=('Courier', 25), command=fun, relief=tk.GROOVE, bg='light blue').place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Set initial values for the game
hint.set('Guess a number between 1 to 50')
score.set(5)
final_score.set(score.get())

# Run the Tkinter event loop
win.mainloop()
