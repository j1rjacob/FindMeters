from cgitb import text
import tkinter as tk
from tkinter import messagebox 
import core.GetMetersCoordinates as main
from tkinter import filedialog as fd

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(1, minsize=25, weight=1)
# window.eval('tk::PlaceWindow . center')
window.title("GTW XY")

fr_buttons = tk.Frame(window)

#CONFIRMATION
def show_msg():
   gtwFilePath = "C:\\Users\\Ivar\\Desktop\\gtw3"
   destinationPath =  "C:\\Users\\Ivar\\Desktop\\gtwXY\\"
   db = "C:\\Users\\Ivar\\Desktop\\RCBU_20211206_DB_.csv"
   #x = main.GetCoordinates(txt_folderpath.get(),txt_filepath.get())
   x = main.GetCoordinates(txt_folderpath.get(),txt_filepath.get())
   x.get_result()
   messagebox.showinfo("GTW XY",x.get_result())
#CONFIRMATION

#LABEL
l1 = tk.Label(fr_buttons, text = "Folder Path:")
l2 = tk.Label(fr_buttons, text = "File Path:")
#LABEL

#INPUT
txt_folderpath = tk.Entry(fr_buttons, width=100)
txt_filepath = tk.Entry(fr_buttons, width=100)
#INPUT

#GET FILEPATH
def open_file():
    txt_filepath.configure(state="normal")
    """Get DB File Path"""
    filepath = fd.askopenfilename( 
      initialdir='/',
      filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if not filepath:
      return

    txt_filepath.insert(0,filepath) 
    txt_filepath.configure(state="readonly")
#GET FILEPATH

#GET FOLDERPATH
def open_folder():
    txt_filepath.configure(state="normal")
    """Get DB Folder Path"""
    folderpath = fd.askdirectory( 
      initialdir='/'
    )
    if not folderpath:
      return   
    txt_folderpath.insert(0,folderpath) 
    txt_folderpath.configure(state="readonly")
#GET FOLDERPATH

#BUTTONS
btn_folderpath = tk.Button(fr_buttons, text="Folder Path", command=open_folder)
btn_filepath = tk.Button(fr_buttons, text="File Path", command=open_file)
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

window.mainloop()