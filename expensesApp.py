import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from Users import login
from Gui import frames, entryBox, loginLayout
from config import store

class ExpensesApp(tk.Frame):

    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.parent = parent
        
        self.loginGUI()

    #Login GUI
    def loginGUI(self):
        self.parent.unbind('<+>')
        self.loginLayout = loginLayout.LoginLayout(self.parent, 1,"solid")

def placeholder():
    pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Expenses Application")

    style = ThemedStyle(root)
    style.set_theme("arc")
    style.theme_use("arc")
    
    application = ExpensesApp(root)
    store["root"] = root
    store["application"] = application
    
    root.state('zoomed') # Maximise window.
    root.update_idletasks()
    root.update()
    
    root.minsize(width=root.winfo_width(), height=root.winfo_height())
    root.maxsize(width=root.winfo_width(), height=root.winfo_height())

#    menubar = tk.Menu(root) # Menu on top
#    filemenu = tk.Menu(menubar, tearoff=0)
#    filemenu.add_command(label="New", command=placeholder)
#    filemenu.add_separator()
#    filemenu.add_command(label="Load")
#    filemenu.add_command(label="Save")
#    menubar.add_cascade(label="File", menu=filemenu)
    
#    root.config(menu=menubar)

    root.mainloop()
    
def logoutClear():

    for i in store.get("root").winfo_children():
        if not isinstance(i, (ExpensesApp, tk.Menu)):
            i.destroy()

    store.get("application").loginGUI()
        
