from tkinter import *
from tkinter.ttk import *





class MyWidget(Frame):
    '''
    A custom widget class that inherits from the Widget class.
    '''
    def __init__(self, master: any = None, **kwargs):
        '''
        Constructor for the MyWidget class.
        '''
        super().__init__(master, **kwargs)
        self.widgets = {}        
        self.setUp()


    def setUp(self) -> None:
        '''
        Sets up the widget.
        '''
        print(f"setUp: not implemented for {self.__class__}!")
        pass
    

    def make_scrollable(self) -> None:
        '''
        Makes the widget scrollable.
        '''
        print(f"make_scrollable: not implemented for {self.__class__}!")
        pass
    

    def get_widgets(self) -> list:
        return [self.widgets[k] for k in self.widgets.keys()]
    

    def get_weights(self) -> dict:
        def add_weight(d, k, w):
            if k in d.keys():
                d[k] += w
            else:
                d[k] = w
            return d
        row_weights = {}
        col_weights = {}
        for widget in self.get_widgets():
            weights = widget["weights"]
            pos = widget["position"]
            row_weights = add_weight(row_weights, str(pos[0]), weights[0])
            col_weights = add_weight(col_weights, str(pos[1]), weights[1])
        return {'row_weights':row_weights, 'col_weights': col_weights}
    

    def set_weights(self) -> None:
        def read_and_set_weights(d, modus):
            for k in d.keys():
                idx = int(k)
                weight = d[k]
                if modus == 'row':
                    self.rowconfigure(idx, weight=weight)
                if modus == 'column':                    
                    self.columnconfigure(idx, weight=weight)
        weightdict = self.get_weights()
        read_and_set_weights(weightdict['row_weights'], 'row')
        read_and_set_weights(weightdict['col_weights'], 'column')


    def add_widget(self, widget, name: str, row:int = 0, column:int = 0, 
                        rowspan:int = 1, columnspan:int = 1, 
                        row_weight:int = 0, col_weight:int = 0, 
                        config: dict = {}, **grid_kwargs) -> None:
        '''
        Adds a widget to the MyWidget class.
        '''
        widget.master = self
        wdict = {}
        wdict["widget"] = widget
        wdict["position"] = [row, column, rowspan, columnspan]
        wdict["weights"] = [row_weight, col_weight]
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


    def add_title(self, title: str, title_config: dict = {}, **grid_kwargs) -> None:
        '''
        Adds a title to the widget.
        '''        
        lbl = Label(self, text=title, **title_config)
        self.shift_widgets()
        self.add_widget(lbl, "widget_title", **grid_kwargs)


    def add_button(self, text: str, command, button_config: dict = {}, **grid_kwargs):
        '''
        add a button to the widget
        '''
        btn = Button(self, text=text, command=command, **button_config)
        self.add_widget(btn, text + '_btn', **grid_kwargs)


    def build(self) -> None:
        '''
        Builds the widget.
        '''
        for wdict in self.get_widgets():
            grid_kwargs = wdict["grid_kwargs"]
            pos = wdict["position"]
            weights = wdict["weights"]
            widget = wdict["widget"]
            widget.grid(row=pos[0], column=pos[1], rowspan=pos[2], columnspan=pos[3], **grid_kwargs)
        self.set_weights()










class MyTxtfield(MyWidget):
    '''
    A custom text field widget class that inherits from the MyWidget class.
    '''
    def __init__(self, master = None, yscrollable: bool = True, textfield_config: dict = {}, **kwargs):
        '''
        Constructor for the MyTxtfield class.
        '''
        self.textfield_config = textfield_config
        self.yscrollable = yscrollable
        super().__init__(master, **kwargs)
        

    def setUp(self) -> None:
        '''
        Sets up the text field widget.
        '''
<<<<<<< HEAD
        self.txtfield = Text(self, **self.textfield_config)
        self.add_widget(self.txtfield, "txtfield", row=0, column=0, rowspan=1, columnspan=1, sticky="nesw")
        self.build()
=======
        self.txtfield = Text(self, **self.textfield_config)        
        self.add_widget(self.txtfield, "txtfield", row=0, column=0, row_weight=1, col_weight=1, sticky="nesw")
        if self.yscrollable:
            self.make_vert_scrollable()


    def make_vert_scrollable(self) -> None:
        scrollbar = Scrollbar(self, orient='vertical', command=self.txtfield.yview)
        self.txtfield.config(yscrollcommand=scrollbar.set)
        self.add_widget(scrollbar, 'y_scrollbar', row=0, column=1, sticky='nesw', padx=2, pady=2)
        

    def get_text(self, index1="1.0", index2="end"):
        return self.txtfield.get(index1=index1, index2=index2)


    def clear(self):
        self.txtfield.delete("0.0", "end")


    def write(self, str):
        self.txtfield.insert("end", str)
>>>>>>> 3bfb4153bb59cbd50af3b5d6ece182ab008ecfb1
