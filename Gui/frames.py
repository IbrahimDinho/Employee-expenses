import tkinter as tk

class Frames(tk.Frame):

    def __init__(self,parent,bw,rlf,**kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.frame = tk.Frame(master = parent, background = "grey",bd = bw, relief = rlf)
    
    def selfdelete(self):
        self.frame.grid_forget()
