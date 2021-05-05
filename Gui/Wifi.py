import tkinter as tk
from tkinter import ttk
import ExitWindow as ew

def OpenWifi():
	window = tk.Tk()
	window.attributes("-fullscreen", True)
	window.title("Room Os")
	#window.iconbitmap('Icons/RoomOsIcon.ico')

	#title
	title = tk.Label(window, text="Room Control Panel", font=('Arial', 25))
	title.place(relx=0.44, rely=0)

	#seperator
	separator = ttk.Separator(window, orient='horizontal')
	separator.place(relx=00, rely=0.05, relwidth=1, relheight=1)

	#buttons
	btn1 = tk.Button(window, text="Wifi", bg='grey56', bd=0, padx=69, pady=20, )
	btn1.place(relx=0.01, rely=0.28)

	#exit-Button
	btnExit = tk.Button(window, text="Go Back", font=("Arial", 20), bg='red4', fg='white', bd=0, padx=19, pady=0, command=exit)
	btnExit.place(relx=0.01, rely=0.63)

	#seperator
	separator = ttk.Separator(window, orient='vertical')
	separator.place(relx=0.09, rely=0.05, relwidth=0.0001, relheight=1)

	window.mainloop()
