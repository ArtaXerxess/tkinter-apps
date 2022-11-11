from roman_to_integer import translate_rom_to_int
from integer_to_Roman import translate_int_To_Roman
import  tkinter  as  tk
from  tkinter  import  ttk

class  ArtaXerxes(tk.Tk):
        def  __init__(self):
            super().__init__()

            #  configure  the  root  window
            self.title('Romulus And Remus')
            # self.geometry('370x90')
            self.minsize(300,300)

            # rom to int label
            self.label_rom_to_int  =  ttk.Label(self,  text='Enter Roman Integer:')
            self.label_rom_to_int.pack(pady=5)

            # entry
            self.roman_entry = ttk.Entry(master=self)
            self.roman_entry.pack(pady=5)

            # Button
            self.button  =  ttk.Button(self,  text='convert',command=self.rom_int_conv)
            self.button.pack(pady=5)

            # answer label
            self.answer = ttk.Label(master=self,text='Answer will be displayed here...')
            self.answer.pack()

            # int to roman label
            self.int_to_rom_label = ttk.Label(master=self,text='Enter Integer: ')
            self.int_to_rom_label.pack(pady=5)

            # int to roman entry
            self.int_to_rom_entry = ttk.Entry(master=self)
            self.int_to_rom_entry.pack(pady=5)

            # int to roman button
            self.int_to_roman_button = ttk.Button(master=self,text='Convert',command=self.int_to_Roman)
            self.int_to_roman_button.pack(pady=5)

            # int to roman result
            self.int_to_rom_answer_label = ttk.Label(master=self,text="Answer will be displayed here...")
            self.int_to_rom_answer_label.pack(pady=5)

        def rom_int_conv(self):
            self.answer['text']=translate_rom_to_int(roman=self.roman_entry.get())
        
        def int_to_Roman(self):
            self.int_to_rom_answer_label['text']=translate_int_To_Roman(num=int(self.int_to_rom_entry.get()))


if __name__=="__main__":
    app =  ArtaXerxes()
    app.mainloop()