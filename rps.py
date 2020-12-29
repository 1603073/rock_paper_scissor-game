from tkinter import *
from random import randint
from tkinter import ttk

root = Tk()
root.title('Rock, Paper, Scissors')
root.iconbitmap('images/rps_logo.ico')
root.geometry('300x300')

rock = PhotoImage(file="images/rock.png")
paper = PhotoImage(file="images/paper.png")
scissors = PhotoImage(file="images/scissors.png")

image_list = [rock, paper, scissors]
pick_number = randint(0,2)
image_label = Label(root, image=image_list[pick_number])
image_label.pack(pady=20)

def spin():
    pick_number = randint(0,2)
    image_label.config(image=image_list[pick_number])
    if user.get() == 'Rock':
        user_value = 0
    elif user.get() == 'Paper':
        user_value = 1
    elif user.get() == 'Scissors':
        user_value = 2
    #compare between user and computer
    if user_value == pick_number:
        win_lose.config(text = "It's a tie")
    #rock    
    elif user_value == 0:
        if pick_number == 2:
            win_lose.config(text = "Rock smashes Scissors!U win!!!")
        elif image_list[pick_number] == 1:
            win_lose.config(text = "Sad!!! Paper covers rock!!! U lose!!!")
    # paper
    elif user_value == 1:
        if pick_number == 2:
            win_lose.config(text = "Scissors cuts the paper! U lose !!!")
        elif pick_number == 0:
            win_lose.config(text = "Yeahh!!! Paper covers rock!!! U win!!!")
    #scissors
    elif user_value == 2:
        if pick_number == 1:
            win_lose.config(text = "Scissors cuts the paper! U win !!!")
        elif pick_number == 0:
            win_lose.config(text = "Sad!!! Rock smashes scissors !!! U lose!!!")                          

user = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
user.current(0)
user.pack(pady=20)
spin_button = Button(root, text="Click", command=spin)
spin_button.pack(pady=20)

win_lose = Label(root, text="", font=("Times",24))
win_lose.pack(pady=20)
root.mainloop()


