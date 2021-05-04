import tkinter as tk
from tkinter import ttk
import ExitWindow as ew

def OpenMenu():
	window = tk.Tk()
	window.attributes("-fullscreen", True)
	window.title("Room Os")
	window.iconbitmap('Icons/RoomOsIcon.ico')

	#title
	title = tk.Label(window, text="Room Control Panel", font=('Arial', 25))
	title.place(relx=0.44, rely=0)

	#seperator
	separator = ttk.Separator(window, orient='horizontal')
	separator.place(relx=00, rely=0.05, relwidth=1, relheight=1)

	#buttons
	btn1 = tk.Button(window, text="Main Menu", bg='grey56', bd=0, padx=50, pady=20, )
	btn1.place(relx=0.01, rely=0.07)

	#exit-Button
	btnExit = tk.Button(window, text="Go Back", font=("Arial", 20), bg='red4', fg='white', bd=0, padx=19, pady=0, command=exit)
	btnExit.place(relx=0.01, rely=0.63)

	#seperator
	separator = ttk.Separator(window, orient='vertical')
	separator.place(relx=0.09, rely=0.05, relwidth=0.001, relheight=1)

	#Admin Num
	adminNum = tk.Label(window, text="Admins: 1", font=("Arial", 20))
	adminNum.place(relx=0.1 ,rely=0.1)

	#User Num
	UserNum = tk.Label(window, text="Users: 1", font=("Arial", 20))
	UserNum.place(relx=0.1 ,rely=0.15)

	#Devices Num
	devicesNum = tk.Label(window, text="Devices: 4", font=("Arial", 20))
	devicesNum.place(relx=0.1 ,rely=0.2)

	#Cameras Num
	camerasNum = tk.Label(window, text="Cameras: 1", font=("Arial", 20))
	camerasNum.place(relx=0.1 ,rely=0.25)

	#pc Num
	pcNum = tk.Label(window, text="Computers: 1", font=("Arial", 20))
	pcNum.place(relx=0.1 ,rely=0.3)

	#pi Num
	piNum = tk.Label(window, text="Raspberries: 2", font=("Arial", 20))
	piNum.place(relx=0.1 ,rely=0.35)
	
	#HandTracking
	htrack = tk.Button(window, text="HandTracking", font=("Arial", 15), bg='grey88')
	htrack.place(relx=0.3, rely=0.1)
	#FaceTracking
	ftrack = tk.Button(window, text="HandTracking", font=("Arial", 15), bg='grey88')
	ftrack.place(relx=0.5, rely=0.1)
	window.mainloop()