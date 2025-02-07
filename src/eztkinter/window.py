from tkinter import *
from tkinter.ttk import *

from .widget import MyWidget





class MyWindow():
    '''
    Basic TK window 
    '''
    def __init__(self, title: str = 'MyGUI', geometry:str = "900x600", **kwargs) -> None:
        self.setup_gui(title, geometry, **kwargs)
        self.inherit_functions()

    def setup_gui(self, title, geometry, **kwargs):
        self.root = Tk(**kwargs)
        self.root.title(title)
        self.root.geometry(geometry)
        self.frame = MyWidget(self.root)
        self.frame.grid(column=0, row=0, sticky='wens')
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)


    def inherit_functions(self):
        self.mainloop = self.root.mainloop
        self.add_widget = self.frame.add_widget
        self.build = self.frame.build


    def mainloop(self):
        self.root.mainloop()