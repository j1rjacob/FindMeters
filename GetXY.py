import tkinter as tk
from tkinter import messagebox 
import core.TestPassValues as f

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(1, minsize=25, weight=1)
# window.eval('tk::PlaceWindow . center')
window.title("GTW XY")

fr_buttons = tk.Frame(window)

#CONFIRMATION
def show_msg():
   x = f.ConcatString("txt1"," txt2")
   x.get_result()

   messagebox.showinfo("GTW XY",x.get_result())
#CONFIRMATION

#LABEL
l1 = tk.Label(fr_buttons, text = "Folder Path:")
l2 = tk.Label(fr_buttons, text = "File Path:")
#LABEL

#INPUT
txt_folderpath = tk.Entry(fr_buttons, state="disabled", width=100)
txt_filepath = tk.Entry(fr_buttons, state="disabled", width=100)
#INPUT

#BUTTONS
btn_folderpath = tk.Button(fr_buttons, text="Folder Path")
btn_filepath = tk.Button(fr_buttons, text="File Path")
btn_getxy = tk.Button(fr_buttons, text="Get XY", command=show_msg)
#BUTTONS

#ALIGNING
l1.grid(row = 0, column = 0, sticky ="w", pady = 2)
l2.grid(row = 1, column = 0, sticky ="w", pady = 2)

txt_folderpath.grid(row=0, column=1, sticky="e", pady = 2)
txt_filepath.grid(row=1, column=1, sticky="e", pady = 2)

btn_folderpath.grid(row=0, column=2, sticky="we", padx=5, pady=5)
btn_filepath.grid(row=1, column=2, sticky="we", padx=5)
btn_getxy.grid(row=3, column=1, sticky="we", padx=5, pady=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
#ALIGNING



#EVENT

#EVENT

window.mainloop()