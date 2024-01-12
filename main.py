from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()

    if len(website.strip()) == 0 or len(password.strip()) == 0:
        messagebox.showinfo(title="Ooopsss", message="Sorry But you missed a blank field")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nLogin: {login}\n password: {password}\n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"\n{website} | {login} | {password}")
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:", font=("Arial", 10, "bold"))
website_label.grid(column=0, row=1)

website_entry = Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2, sticky='EW')
website_entry.focus()


# Login
login_label = Label(text='Login:', font=("Arial", 10, "bold"))
login_label.grid(column=0, row=2)

login_entry = Entry(width=45)
login_entry.grid(column=1, row=2, columnspan=2, sticky='EW')
login_entry.insert(0, "user@email.com")


# Password
password_label = Label(text="Password:", font=("Arial", 10, "bold"))
password_label.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3, sticky='EW')


# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, command=save_data)
add_button.grid(column=1, row=4,  columnspan=2, sticky='EW')


window.mainloop()
