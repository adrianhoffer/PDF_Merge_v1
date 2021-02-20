from PyPDF2 import PdfFileMerger
import os
import os.path
from tkinter.filedialog import *
import tkinter as tk
from tkinter import *

pdfs = []

root = tk.Tk()
root.geometry("600x300")
def openFile():
    name = askopenfilename(defaultextension = ".pdf", filetypes=[('pdf file', '*.pdf')], title = "Choose files")
    if name is not None:
        pdfs.append(name)
        
        

def mergeFiles():
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    fout=asksaveasfile(mode='wb', defaultextension=".pdf",filetypes=[('pdf file', '*.pdf')])
    merger.write(fout)
    merger.close
   
    
    
root.iconbitmap('icon.ico')
Title = root.title("PDF merger")
label0 = tk.Label(root, text = "Welcome to PDF merger!", font='Helvetica, 24')
label0.pack()
label1 = tk.Label(root, text = "Step 1: Choose files to merge", font='Helvetica, 18')
label1.pack()
chooseButton = tk.Button(text="Choose files",font='Helvetica, 12', command = openFile)
chooseButton.pack()
label1 = tk.Label(root, text = "Step 2: Convert and save your merged PDF", font='Helvetica, 18')
label1.pack()
merButton = tk.Button(text="Merge files", font='Helvetica, 12', command = mergeFiles)
merButton.pack()
root.mainloop()





