__title__ = "Simple GUI that generates SHA-1 and MD-5 hash code from the plaintext entered by the user"
__author__ = "Harshvardhan Singh"

from tkinter import Tk,ttk
from hashlib import sha1,md5

class crypto:

    def __init__(self) -> None:
        self.plaintext = None
        self.sha_1_hash_string = None
        self.md_5_hash_string = None
    
    def hash(self,plaintext):
        self.plaintext = plaintext
        self.sha_1_hash_string = sha1(str(self.plaintext).encode()).hexdigest()
        self.md_5_hash_string = md5(str(self.plaintext).encode()).hexdigest()
        self.results = self.sha_1_hash_string , self.md_5_hash_string
        return self.results
    
class GUI:
    def __init__(self) -> None:
        # Creating the GUI

        #initializing
        self.window = Tk()
        self.widget = ttk

        #basic configuration of the window
        self.window.geometry('450x200')
        self.window.resizable(height=False,width=False)
        self.window.title("HASHING")

        # Putting up widgets

        # input request label
        self.request_input_label = self.widget.Label(text="Enter the Plaintext")
        self.request_input_label.pack(pady=5)

        #getting input from Entry
        self.input_entry = self.widget.Entry()
        self.input_entry.pack(pady=5)

        # OK button
        self.ok_button = self.widget.Button(text='OK',command=self.button_clicked)
        self.ok_button.pack(pady=5)

        # Result label
        self.results_label = self.widget.Label(text='')
        self.results_label.pack()

        # Copy to clipboard Buttons
        self.copy_sha_hash_button = self.widget.Button(text='Copy sha-1 hash string to clipboard',command=self.copy_sha_hash_button_Clicked)
        self.copy_sha_hash_button.pack(side='left',padx=10)
        self.copy_md5_hash_button = self.widget.Button(text='Copy md-5 hash string to clipboard',command=self.copy_md5_hash_button_Clicked)
        self.copy_md5_hash_button.pack(side='right',padx=10)

        # OK button command
    def button_clicked(self):
        self.get_input = str(self.input_entry.get())
        self.hashira = crypto()
        self.results=self.hashira.hash(plaintext=self.get_input)
        self.result_string = f"""\
SHA-1 Hash string :\t{self.results[0]}
MD-5  Hash string :\t{self.results[1]}"""
        self.results_label['text'] =  self.result_string

    
    # sha_1 copy Button Command
    def copy_sha_hash_button_Clicked(self):
        print(f"{self.results[0]}")
        self.window.clipboard_append(f"{self.results[0]}")
    
    # md-5 copy Button Command
    def copy_md5_hash_button_Clicked(self):
        print(f"{self.results[1]}")
        self.window.clipboard_append(f"{self.results[1]}")
        
    # the magic is activated here
    def do_the_magic(self)->None:
        self.window.mainloop()


if __name__ == "__main__":
    testing = GUI()
    testing.do_the_magic()

# Have fun :)