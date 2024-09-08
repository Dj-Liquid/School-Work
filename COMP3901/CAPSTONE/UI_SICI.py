from customtkinter import *
from PIL import Image
import subprocess
import threading
import mysql.connector
from email_database import Emails

host = "localhost"
user = "root"
password = "jimjones2266"
database = "Capture"

#db = Emails(host, user, password, database)
#db.create_table()
#emails = db.get_emails()
#print("Emails in database:", emails)



# Global variable to store the subprocess
process = None

# Function to execute subprocess
def run_subprocess():
    global process
    process = subprocess.Popen(["python", "test.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Read output asynchronously in a separate thread
    threading.Thread(target=read_subprocess_output, args=(process.stdout,)).start()
    threading.Thread(target=read_subprocess_output, args=(process.stderr,)).start()

# Function to read subprocess output asynchronously
def read_subprocess_output(stream):
    for line in iter(stream.readline, b''):
        print(line.decode(), end='')  # Output to console (optional)
    stream.close()

# Function to handle button click events
def button_click(button_number):
    global process
    if button_number == 1:
        #db.add_email(email)
        #db.close_connection()

        run_subprocess()
        status_label.configure(text="Starting Process...", fg_color="blue")
    elif button_number == 2:
        if process is not None:
            process.kill()  # Terminate the subprocess
            status_label.configure(text="Process Terminated", fg_color="red")
        else:
            status_label.configure(text="No Process Running", fg_color="red")
    else:
        status_label.configure(text="Button {} Clicked!".format(button_number), fg_color="green")

# Function that simulates a long-running process
def long_running_process():
    for i in range(10):
        status_label.configure(text="Processing...", fg_color="orange")
        # Check if a button is clicked every 100 milliseconds
        root.after(100, check_button_click)
        # Simulate some work
        import time
        time.sleep(1)
    status_label.configure(text="App Loaded", fg_color="green")

# Function to check if a button is clicked
def check_button_click():
    global clicked_button
    if clicked_button is not None:
        status_label.configure(text="Stopping Long Running Process...", fg_color="red")
        # Stop the long running process or perform any other action
        clicked_button = None  # Reset clicked_button to None
        return True

# Create the main Tkinter window
root = CTk()
root.title("Secure Integrated Computer Infrastructure")

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the size of the window to a quarter of the screen dimensions
root.geometry("{}x{}".format(screen_width // 2, screen_height // 2))

"""background_img = CTkImage(Image.open("bg.png"), size=(screen_width // 2,screen_height // 2))

background_label2 = CTkLabel(master=root, text="", image = background_img)
background_label2.place(x=0,y=0)"""

img = CTkImage(Image.open("test.png"), size=(100,100))

background_label = CTkLabel(master=root, text="", image = img)
background_label.place(x=0,y=0)

frame = CTkFrame(master=root, bg_color="transparent", fg_color="transparent")
frame.pack(anchor="c", pady = 100,expand = True)    

# Add style

start_img = Image.open("play.png")
stop_img = img = Image.open("stop.png")
report_img = img = Image.open("report.png")

# Create and add buttons to the window
button1 = CTkButton(master = frame, text="Start", command=lambda: button_click(1),corner_radius=32, bg_color="transparent", fg_color="#9C31CB", hover_color="#A564C2", image = CTkImage(dark_image=start_img))
button1.pack(padx=20, pady=30, anchor="c")

button2 = CTkButton(master = frame, text="Stop", command=lambda: button_click(2),corner_radius=32, bg_color="transparent", fg_color="#9C31CB", hover_color="#A564C2", image = CTkImage(dark_image=stop_img))
button2.pack(anchor="n", expand=True, padx=20, pady=30)

button3 = CTkButton(master = frame, text="Generate Report", command=lambda: button_click(3),corner_radius=32, bg_color="transparent", fg_color="#36B0D3", hover_color="#5EBAD5", image = CTkImage(dark_image=report_img))
button3.pack(anchor="n", expand=True, padx=20, pady=30)

# Add a label for displaying status
status_label = CTkLabel(master = frame, text="Ready", anchor="center")

# Set up a global variable to store which button is clicked
clicked_button = None



email = ""



# Define function to handle storing email
def store_email(event):
    global email  # Define email as a global variable
    email = entry.get()  # Get the email from the entry widget
    print("Email entered:", email)

# Create entry widget
entry = CTkEntry(master=root, placeholder_text="Email", fg_color="transparent")
entry.place(relx=0.5, rely=0.8, anchor="center")

# Bind the <Return> key event to the entry widget
entry.bind("<Return>", store_email)
set_appearance_mode("dark")

# Run a long-running process
long_running_process()

# Run the Tkinter event loop
root.mainloop()
