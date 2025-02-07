import unittest
from tkinter import *
from tkinter.ttk import *

from src.eztkinter.widget import *
from src.eztkinter.window import *





class TestGUI(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.setup_gui()


    def setup_gui(self):
        self.window = MyWindow('Test GUI')
        textfield = MyTxtfield(self.window.frame, textfield_config={"padx":10, "pady":10})    
        textfield.add_title('Test Textfield', sticky='nesw')
        textfield.add_button(text='clear', command=textfield.clear, row=2, sticky='ne') 
        textfield.build()
        self.window.add_widget(textfield, 'textfield', row_weight=1, col_weight=1)
        self.window.build()
        
    def test_app(self):
        self.window.mainloop()




