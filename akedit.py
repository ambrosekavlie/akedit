#!/usr/bin/python3
from sys import argv
import tkinter as tk

# initialize tkinter window
root = tk.Tk()
root.title("Text Editor")

# write to the file
def writeToFile(entry_contents):
    with open(file_name, 'w') as file:
        # write the contents and remove the last character
        # since text widget adds trailing newline
        file.write(entry_contents[:-1])

# create the entry that the user uses to edit a file
def createEntry(file_contents: str):
    # add text entry
    file_entry = tk.Text(root, borderwidth=5)
    # add file contents to entry
    file_entry.insert("1.0", file_contents)
    file_entry.pack(padx=20, pady=10)


    write = tk.Button(root, text="Write to File",
                      command=lambda: writeToFile(
                      file_entry.get(index1="1.0", index2=tk.END)))
    write.pack()

    root.mainloop()


try:
    # get the file to write to
    file_name = argv[1]
    with open(file_name, 'r') as file:
        # create the text entry with the read file as contents
        createEntry(file.read())
except IndexError:  # no file supplied
    print("Usage: akedit [file]")
except FileNotFoundError:  # create new file
    createEntry("[Creating new file]")

