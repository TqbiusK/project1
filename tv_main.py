import tkinter as tk
from tkinter import ttk
from television import Television
from tvremote import *
def main():
    tv_model = Television()
    tv_view = TelevisionRemoteView()
    tv_controller = TelevisionController(tv_model, tv_view)
    tv_view.mainloop()

if __name__ == "__main__":
    main()