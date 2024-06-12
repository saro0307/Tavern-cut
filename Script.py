import tkinter as tk
from tkinter import messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import datetime
import pytz
import ssl

# Turing machine states and transitions
states = {
    "q0": {  # Start state
        "r": ("q1", "r", "R"),  # If the current symbol is "r", move right to state q1 and write "r"
    },
    "q1": {
        "u": ("q2", "u", "R"),  # If the current symbol is "u", move right to state q2 and write "u"
    },
    "q2": {
        "s": ("q3", "s", "R"),  # If the current symbol is "s", move right to state q3 and write "s"
    },
    "q3": {
        "s": ("accept", "s", "S"),  # If the current symbol is "s", move to the accept state and write "s"
    },
    "q4": {
        "i": ("accept", "i", "S"),  # If the current symbol is "i", move to the accept state and write "i"
    },
    "q5": {
        "a": ("accept", "a", "S"),  # If the current symbol is "a", move to the accept state and write "a"
    },
}

# Email configuration 
# Make sure to replace XXXX YYYY ZZZZ with actual values of you own choice
email_sender = 'XXXX YYYY ZZZZ'
email_password = 'XXXX YYYY ZZZZ'
email_receiver = 'XXXX YYYY ZZZZ'

def run_turing_machine(password):
    tape = list(password)
    current_state = "q0"
    current_position = 0
    incorrect_flag = False

    while current_state != "accept":
        current_symbol = tape[current_position]
        if current_symbol in states[current_state]:
            new_state, write_symbol, move_direction = states[current_state][current_symbol]
            tape[current_position] = write_symbol
            if move_direction == "R":
                current_position += 1
            elif move_direction == "L":
                current_position -= 1
            current_state = new_state
        else:
            incorrect_flag = True
            break

    if incorrect_flag:
        return False
    else:
        return True

def send_email_alert():
    ist_timezone = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(ist_timezone).strftime('%Y-%m-%d %I:%M:%S %p')

    subject = 'Security Alert'
    body = f"""
    An unauthorized attempt has been made to access your account without proper authorization.
    Timestamp: {current_time} IST
    """

    em = MIMEMultipart()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.attach(MIMEText(body, 'plain'))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def on_submit_button_click(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    if username == "KBG":  
        if run_turing_machine(password):
            messagebox.showinfo("Login Successful", "Access Granted.")
        else:
            messagebox.showerror("Login Failed", "Incorrect password. Security breach detected.")
            send_email_alert()
    else:
        messagebox.showerror("Login Failed", "Incorrect username.")

# GUI setup
root = tk.Tk()
root.title("Login Page")

# Increase the window size
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Increase font size for better readability
font = ("Helvetica", 20)

# Username entry
username_label = tk.Label(root, text="Username:", font=font)
username_label.pack(pady=10)
username_entry = tk.Entry(root, font=font)
username_entry.pack(pady=10)

# Password entry
password_label = tk.Label(root, text="Password:", font=font)
password_label.pack(pady=10)
password_entry = tk.Entry(root, show="*", font=font)
password_entry.pack(pady=10)

# Submit button
submit_button = tk.Button(root, text="Login", command=lambda: on_submit_button_click(username_entry, password_entry), font=font)
submit_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
