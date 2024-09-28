import random
import tkinter as tk
from tkinter import messagebox

# Generate a random number
randomNumber = random.randint(1, 100)
guesses = 0

# Function to handle guess submission
def submit_guess():
    global guesses, randomNumber
    
    guess = entry_guess.get()
    
    if guess.lower() == "e":
        root.quit()
    
    try:
        guess = int(guess)
    except ValueError:
        label_feedback.config(text="Invalid input! Enter a number.", fg="red")
        return
    
    guesses += 1
    label_progress.config(text=f"Guesses: {guesses}")
    
    if guess < randomNumber:
        label_feedback.config(text="Higher!", fg="blue")
    elif guess > randomNumber:
        label_feedback.config(text="Lower!", fg="blue")
    else:
        messagebox.showinfo("Success", f"Correct! You guessed it in {guesses} attempts.")
        guesses = 0
        randomNumber = random.randint(1, 100)  # Generate new random number
        label_feedback.config(text="New number generated! Guess again.", fg="green")
        label_progress.config(text=f"Guesses: {guesses}")

# Function to exit the game
def exit_game():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Window size and position
root.geometry("400x300")
root.resizable(False, False)

# Center the window
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Styling options
bg_color = "#f0f8ff"  # Light cyan background
button_color = "#ff7f50"  # Coral buttons
font_style = ("Arial", 14)

# Configure root window's background color
root.config(bg=bg_color)

# Create widgets
label_instructions = tk.Label(root, text="Guess the number (1-100)\nEnter 'e' to exit", bg=bg_color, font=font_style)
label_instructions.pack(pady=10)

entry_guess = tk.Entry(root, font=("Arial", 12))
entry_guess.pack(pady=10)

button_submit = tk.Button(root, text="Submit", command=submit_guess, bg=button_color, font=font_style)
button_submit.pack(pady=5)

button_exit = tk.Button(root, text="Exit", command=exit_game, bg=button_color, font=font_style)
button_exit.pack(pady=5)

label_feedback = tk.Label(root, text="", bg=bg_color, font=("Arial", 12))
label_feedback.pack(pady=10)

label_progress = tk.Label(root, text="Guesses: 0", bg=bg_color, font=("Arial", 12))
label_progress.pack(pady=10)

# Start the main loop
root.mainloop()
