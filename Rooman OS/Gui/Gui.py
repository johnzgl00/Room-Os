import tkinter as tk
from tkinter import ttk
import ExitWindow as ew
import MainMenu as mm
import Lights as li
import Devices as dv
import Wifi as wf
import Themes as th
import Connections as cn
import Other as ot
import Settings as st

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
btn1 = tk.Button(window, text="Main Menu", bg='white', bd=0, padx=50, pady=20, command=mm.OpenMenu)
btn1.place(relx=0.01, rely=0.07)

btn2 = tk.Button(window, text="Lights", bg='white', bd=0, padx=64, pady=20, command=li.OpenLights)
btn2.place(relx=0.01, rely=0.14)

btn3 = tk.Button(window, text="Devices", bg='white', bd=0, padx=60, pady=20, command=dv.OpenDevices)
btn3.place(relx=0.01, rely=0.21)

btn4 = tk.Button(window, text="Wifi", bg='white', bd=0, padx=69, pady=20, command=wf.OpenWifi)
btn4.place(relx=0.01, rely=0.28)

btn5 = tk.Button(window, text="Themes", bg='white', bd=0, padx=59, pady=20, command=th.OpenThemes)
btn5.place(relx=0.01, rely=0.35)

btn6 = tk.Button(window, text="Connections", bg='white', bd=0, padx=46, pady=20, command=cn.OpenConnections)
btn6.place(relx=0.01, rely=0.42)

btn7 = tk.Button(window, text="Other", bg='white', bd=0, padx=64, pady=20, command=ot.OpenOther)
btn7.place(relx=0.01, rely=0.49)

btn8 = tk.Button(window, text="Settings", bg='white', bd=0, padx=58, pady=20, command=st.OpenSettings)
btn8.place(relx=0.01, rely=0.56)

#exit-Button
btnExit = tk.Button(window, text="E X I T", font=("Arial", 30), bg='red', fg='white', bd=0, padx=6, pady=0, command=ew.exitPopUp)
btnExit.place(relx=0.01, rely=0.63)

#seperator
separator = ttk.Separator(window, orient='vertical')
separator.place(relx=0.09, rely=0.05, relwidth=0.0001, relheight=1)

window.mainloop()