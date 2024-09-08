import tkinter as tk
from tkinter import messagebox

# Simulate a database with a dictionary
users_db = {}

# Question Class
class Question:
    def __init__(self, question_text, answer_1, answer_2, answer_3, answer_4, correct_answer, question_score):
        self.question_text = question_text
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.answer_4 = answer_4
        self.correct_answer = correct_answer
        self.question_score = question_score

    def ask_question(self, window, question_label, buttons, score_var):
        question_label.config(text=self.question_text)
        buttons[0].config(text=self.answer_1, command=lambda: self.check_answer(1, window, score_var))
        buttons[1].config(text=self.answer_2, command=lambda: self.check_answer(2, window, score_var))
        buttons[2].config(text=self.answer_3, command=lambda: self.check_answer(3, window, score_var))
        buttons[3].config(text=self.answer_4, command=lambda: self.check_answer(4, window, score_var))

    def check_answer(self, guess, window, score_var):
        global total_score
        if guess == self.correct_answer:
            messagebox.showinfo("Result", "Correct!")
            total_score += self.question_score
        else:
            messagebox.showinfo("Result", f"Wrong! Correct answer was {self.correct_answer}")
        score_var.set(f"Score: {total_score} / 100")
        next_question()

# Initialize quiz data
questions = [
    Question("How many times has India won the Cricket World Cup?", "1", "2", "0", "3", 4, 10),
    Question("When was the first Football World Cup held?", "1904", "1906", "1912", "1930", 4, 10),
    Question("In badminton, the winner is the first to reach how many points?", "12", "15", "18", "21", 4, 10),
    Question("How many players are on the pitch in a hockey match?", "16", "22", "18", "20", 2, 10),
    Question("Who is regarded as the best player in the history of hockey?", "Dhyan Chand", "Roop Singh", "Niraj Singh", "Dhanraj Pillay", 1, 10),
    Question("What is the international governing body of Cricket?", "ICC", "CCI", "GCI", "LIC", 1, 10),
    Question("Which team has won the most IPL trophies?", "CSK", "MI", "RCB", "KKR", 2, 10),
    Question("Which team made the lowest score in IPL history?", "CSK", "MI", "RCB", "RR", 3, 10),
    Question("In which year did India win its first Cricket World Cup?", "1982", "1983", "1984", "1985", 2, 10),
    Question("In which year did India win its first T20 World Cup?", "2006", "2007", "2009", "2011", 2, 10)
]

# Start quiz logic
current_question = 0
total_score = 0

def next_question():
    global current_question
    if current_question < len(questions):
        questions[current_question].ask_question(window, question_label, answer_buttons, score_var)
        current_question += 1
    else:
        messagebox.showinfo("Quiz Completed", f"Your total score is {total_score} / 100")
        window.quit()

def start_quiz():
    login_frame.pack_forget()  # Hide the login frame
    sign_up_frame.pack_forget()  # Hide the sign-up frame
    quiz_frame.pack()  # Show the quiz frame
    next_question()  # Start the quiz by showing the first question

def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in users_db:
        messagebox.showerror("Error", "Username already exists!")
    elif username == "" or password == "":
        messagebox.showerror("Error", "Username and Password cannot be empty!")
    else:
        users_db[username] = password
        messagebox.showinfo("Success", "Sign up successful! You can now log in.")
        sign_up_frame.pack_forget()
        login_frame.pack()

def sign_in():
    username = login_username_entry.get()
    password = login_password_entry.get()
    
    if users_db.get(username) == password:
        messagebox.showinfo("Success", "Login successful!")
        start_quiz()  # Start the quiz after successful login
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# GUI Setup
window = tk.Tk()
window.title("The Daily Quiz")

# Sign-up Frame
sign_up_frame = tk.Frame(window)
tk.Label(sign_up_frame, text="Sign Up", font=("Arial", 16)).pack(pady=20)

tk.Label(sign_up_frame, text="Username:", font=("Arial", 14)).pack(pady=5)
username_entry = tk.Entry(sign_up_frame, font=("Arial", 14))
username_entry.pack(pady=5)

tk.Label(sign_up_frame, text="Password:", font=("Arial", 14)).pack(pady=5)
password_entry = tk.Entry(sign_up_frame, font=("Arial", 14), show="*")
password_entry.pack(pady=5)

sign_up_button = tk.Button(sign_up_frame, text="Sign Up", font=("Arial", 14), command=sign_up)
sign_up_button.pack(pady=20)

# Login Frame
login_frame = tk.Frame(window)
tk.Label(login_frame, text="Sign In", font=("Arial", 16)).pack(pady=20)

tk.Label(login_frame, text="Username:", font=("Arial", 14)).pack(pady=5)
login_username_entry = tk.Entry(login_frame, font=("Arial", 14))
login_username_entry.pack(pady=5)

tk.Label(login_frame, text="Password:", font=("Arial", 14)).pack(pady=5)
login_password_entry = tk.Entry(login_frame, font=("Arial", 14), show="*")
login_password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Sign In", font=("Arial", 14), command=sign_in)
login_button.pack(pady=20)

# Quiz Frame
quiz_frame = tk.Frame(window)
question_label = tk.Label(quiz_frame, text="Welcome to the Quiz!", font=("Arial", 16))
question_label.pack(pady=20)

answer_buttons = [
    tk.Button(quiz_frame, text="", font=("Arial", 14)),
    tk.Button(quiz_frame, text="", font=("Arial", 14)),
    tk.Button(quiz_frame, text="", font=("Arial", 14)),
    tk.Button(quiz_frame, text="", font=("Arial", 14))
]

for btn in answer_buttons:
    btn.pack(pady=10)

score_var = tk.StringVar()
score_var.set(f"Score: 0 / 100")
score_label = tk.Label(quiz_frame, textvariable=score_var, font=("Arial", 14))
score_label.pack(pady=20)

# Start with sign-up screen
sign_up_frame.pack()

# Start the GUI loop
window.mainloop()
