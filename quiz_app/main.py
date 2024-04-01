import tkinter as tk
from tkinter import messagebox,ttk
from ttkbootstrap import Style
from quiz import quiz_data

def show_question():
    question=quiz_data[current_qsn]
    qs_label.config(text=question["question"])
    
    #display the choice on the buttons
    choice=question["choice"]
    for i in range(4):
        choice_btns[i].config(text=choice[i],state="normal")

    #clear feedback label and disable next button
        feedback_label.config(text=" ")
        next_button.config(state="disabled")

def check_answer(choice):
    question=quiz_data[current_qsn]
    selected_choice=choice_btns[choice].cget("text")

    if selected_choice==question["answer"]:
        global score
        score=score+1
        score_label.config(text="Score:{}/{}".format(score,len(quiz_data)))
        feedback_label.config(text="Correct",foreground="green")
    else:
        feedback_label.config(text="Incorrect",foreground="red")
    for button in choice_btns:
        button.config(state="disabled")
    next_button.config(state="normal")

def next_question():
    global current_qsn
    current_qsn=current_qsn+1
    if current_qsn<len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed","Quiz completed!Final Score:{}/{}".format(score,len(quiz_data)))
        root.destroy()

#create the main window
root=tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style=Style(theme="sandstone")

#create question label
qs_label=ttk.Label(root,
                   anchor="center",
                   wraplength=500,
                   padding=10
                   )
qs_label.pack(pady=10)

#create the choice button
choice_btns=[]
for i in range(4):
    button=ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
        )
    button.pack(pady=5)
    choice_btns.append(button)

#create feedback label
feedback_label=ttk.Label(root,
                   anchor="center",
                   padding=10
                   )
feedback_label.pack(pady=10)
    
#Initialize score
score_label=ttk.Label(root,
                      text="Score:0/{}".format(len(quiz_data)),
                      anchor="center",
                      padding=10)
score_label.pack(pady=10)

#create next button
next_button=ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_button.pack(pady=10)

#initialize score
score=0
#Initialize current question index
current_qsn=0

#show first question
show_question()

#start main event loop
root.mainloop()