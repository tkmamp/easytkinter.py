import unittest
from tkinter import *
from tkinter.ttk import *

from src.eztkinter.widget import *


class TestGUI(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.setup_gui()


    def setup_gui(self):
        self.root = Tk()
        self.root.title("Test GUI")
        self.root.geometry("800x600")

    
    def test_app(self):
        self.root.mainloop()




