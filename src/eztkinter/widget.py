from tkinter import *
from tkinter import Misc
from tkinter.ttk import *


class MyWidget(Frame):
    '''
    A custom widget class that inherits from the Widget class.
    '''
    def __init__(self, master: any = None, title:str = None, **kwargs):
        '''
        Constructor for the MyWidget class.
        '''
        super().__init__(master, **kwargs)
        self.widgets = {}
        self.title = title
        self.setUp()


    def setUp(self) -> None:
        '''
        Sets up the widget.
        '''
        print(f"setUP: not implemented for {self.__class__}!")
        pass
    

    def make_scrollable(self) -> None:
        '''
        Makes the widget scrollable.
        '''
        print(f"make_scrollable: not implemented for {self.__class__}!")
        pass


    def add_widget(self, widget, name: str, row:int = 0, column:int = 0, rowspan:int = 1, columnspan:int = 1, config: dict = {}, **grid_kwargs) -> None:
        '''
        Adds a widget to the MyWidget class.
        '''
        widget.master = self
        wdict = {}
        wdict["widget"] = widget
        wdict["position"] = [row, column, rowspan, columnspan]
        wdict["config"] = config
        wdict["grid_kwargs"] = grid_kwargs
        self.widgets[name] = wdict


    def shift_widgets(self, shift_by: int = 1, direction="horizontal") -> None:
        '''
        Shifts the widgets by shift_by steps in "horizontal" or "vertical" direction.
        '''
        shift_index = 0 if direction == "horizontal" else 1
        for wname in self.widgets.keys():
            wdict = self.widgets[wname]
            wdict["position"][shift_index] += shift_by


    def add_title(self, title_config: dict = {}, **grid_kwargs) -> None:
        '''
        Adds a title to the widget.
        '''
        if self.title:
            title = Label(self, text=self.title, **title_config)
            self.shift_widgets()
            self.add_widget(title, "auto_title", **grid_kwargs)


    def build(self) -> None:
        '''
        Builds the widget.
        '''
        self.add_title()
        for wname in self.widgets.keys():
            wdict = self.widgets[wname]
            widget = wdict["widget"]
            grid_kwargs = wdict["grid_kwargs"]
            pos = wdict["position"]
            widget.grid(row=pos[0], column=pos[1], rowspan=pos[2], columnspan=pos[3], **grid_kwargs)










class MyTxtfield(MyWidget):
    '''
    A custom text field widget class that inherits from the MyWidget class.
    '''
    def __init__(self, master = None, title: str = None, textfield_config: dict = {}, **kwargs):
        '''
        Constructor for the MyTxtfield class.
        '''
        self.textfield_config = textfield_config
        super().__init__(master, title, **kwargs)
        
        

    def setUp(self) -> None:
        '''
        Sets up the text field widget.
        '''
        self.txtfield = Text(self, **self.textfield_config)
        self.add_widget(self.txtfield, "txtfield", row=0, column=0, rowspan=1, columnspan=1, sticky="nesw")
