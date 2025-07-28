
### 📄 `rps_gui.py`:
```python
import tkinter as tk
import random
from tkinter import messagebox

user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score
    choices = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(choices)

    result = ""
    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        comp_score += 1

    result_label.config(text=f"Computer chose {comp_choice}\n{result}")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {comp_score}")

def reset():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_label.config(text="Choose your move:")
    score_label.config(text="Your Score: 0 | Computer Score: 0")

# GUI
root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16)).pack(pady=10)

result_label = tk.Label(root, text="Choose your move:", font=("Arial", 14))
result_label.pack()

score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", font=("Arial", 12))
score_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

tk.Button(root, text="Reset", command=reset).pack(pady=10)

root.mainloop()

