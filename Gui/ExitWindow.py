import tkinter as tk

def exitPopUp():
	ExitWindow = tk.Tk()
	ExitWindow.geometry('200x80')
	ExitWindow.configure(bg='grey22')
	ExitWindow.title("Exit")
	#ExitWindow.iconbitmap('Icons/CancelIcon.ico')
	#ExitWindow.eval('tk::PlaceExitWindow . center')
	#Label
	lbl = tk.Label(ExitWindow, text="Are you sure?", bg='grey22',fg='grey86', font=("Arial", 15))
	lbl.place(relx=0.19, rely=0.1)
	#Buttons
	btnCancel = tk.Button(ExitWindow, text="Cancel", bg='grey')
	btnCancel.place(relx=0.1, rely=0.5)

	btnExit = tk.Button(ExitWindow, text="E x i t", bg='red3', fg='snow', command=exit)
	btnExit.place(relx=0.55, rely=0.5)

	ExitWindow.mainloop()
