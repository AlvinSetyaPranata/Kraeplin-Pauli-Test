from .writer import Writer
from tkinter.ttk import Notebook
import tkinter

# --------- Program Starts ------------- #



class App():
    def __init__(self):
        self._window = tkinter.Tk()
        self._window.title("Kraeplin and Pauli Test")
        self._window.geometry("500x500")
        
        self._main_frame = Notebook(self._window)
        self._main_frame.pack(fill=tkinter.BOTH, expand=True)


    def kraeplin(self):
        self._k_frame = tkinter.Frame(self._main_frame)
        self._k_frame.pack(fill=tkinter.BOTH, expand=True)
        self._main_frame.add(self._k_frame, text="Kraeplin")


    def pauli(self):
        self._p_frame = tkinter.Frame(self._main_frame)
        self._p_frame.pack(fill=tkinter.BOTH, expand=True)
        self._main_frame.add(self._p_frame, text="Pauli")

    def configuration(self):
        self._c_frame = tkinter.Frame(self._main_frame)
        self._c_frame.pack(fill=tkinter.BOTH, expand=True)
        self._main_frame.add(self._c_frame, text="Settings")


    @property
    def run(self):
        self.kraeplin()
        self.pauli()
        self.configuration()

        self._window.mainloop()





