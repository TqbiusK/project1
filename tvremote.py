import tkinter as tk
from tkinter import ttk
from television import Television


class TelevisionController:
    """
    Controller class for the Television Remote GUI.

    Attributes:
        model (Television): The television model.
        view (TelevisionRemoteView): The associated view.
    """

    def __init__(self, model, view):
        """
        Initialize the controller with a television model and associated view.

        Parameters:
            model (Television): The television model.
            view (TelevisionRemoteView): The associated view.
        """
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def power_button_clicked(self):
        """
        Callback method for the Power button click event.
        Powers on/off the television and updates the view.
        """
        self.model.power()
        self.view.update()

    def mute_button_clicked(self):
        """
        Callback method for the Mute button click event.
        Toggles mute status of the television and updates the view.
        """
        self.model.mute()
        self.view.update()

    def channel_up_button_clicked(self):
        """
        Callback method for the Channel Up button click event.
        Increases the channel of the television and updates the view.
        """
        self.model.channel_up()
        self.view.update()

    def channel_down_button_clicked(self):
        """
        Callback method for the Channel Down button click event.
        Decreases the channel of the television and updates the view.
        """
        self.model.channel_down()
        self.view.update()

    def volume_up_button_clicked(self):
        """
        Callback method for the Volume Up button click event.
        Increases the volume of the television and updates the view.
        """
        self.model.volume_up()
        self.view.update()

    def volume_down_button_clicked(self):
        """
        Callback method for the Volume Down button click event.
        Decreases the volume of the television and updates the view.
        """
        self.model.volume_down()
        self.view.update()


class TelevisionRemoteView(tk.Tk):
    """
    View class for the Television Remote GUI.

    Attributes:
        controller (TelevisionController): The associated controller.
    """

    def __init__(self, master=None):
        """
        Initialize the view with a master window.

        Parameters:
            master: The master window.
        """
        super().__init__(master)
        self.controller = None

        self.title("TV Remote")
        self.geometry("300x400")  # Set the initial size of the window

        # Create a style for buttons
        button_style = ttk.Style()
        button_style.configure("TButton", font=("Arial", 12))

        # Create buttons
        self.power_button = ttk.Button(self, text="Power", command=self.power_button_clicked, style="TButton")
        self.mute_button = ttk.Button(self, text="Mute", command=self.mute_button_clicked, style="TButton")
        self.channel_up_button = ttk.Button(self, text="Ch+", command=self.channel_up_button_clicked, style="TButton")
        self.channel_down_button = ttk.Button(self, text="Ch-", command=self.channel_down_button_clicked, style="TButton")
        self.volume_up_button = ttk.Button(self, text="Vol+", command=self.volume_up_button_clicked, style="TButton")
        self.volume_down_button = ttk.Button(self, text="Vol-", command=self.volume_down_button_clicked, style="TButton")

        # Layout buttons
        button_width = 10
        button_height = 3

        self.power_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", rowspan=2, columnspan=2)
        self.mute_button.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", rowspan=2, columnspan=2)
        self.channel_up_button.grid(row=2, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
        self.channel_down_button.grid(row=2, column=2, padx=5, pady=5, sticky="nsew", columnspan=2)
        self.volume_up_button.grid(row=3, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
        self.volume_down_button.grid(row=3, column=2, padx=5, pady=5, sticky="nsew", columnspan=2)

        # Create label for displaying TV status
        self.status_label = ttk.Label(self, text="")
        self.status_label.grid(row=4, column=0, columnspan=4, pady=10, sticky="nsew")

        # Configure row and column weights for resizing
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def set_controller(self, controller):
        """
        Set the controller for the view.

        Parameters:
            controller (TelevisionController): The associated controller.
        """
        self.controller = controller

    def update(self):
        """Update the view with the current TV status."""
        tv_status = str(self.controller.model)
        self.status_label.config(text=tv_status)

    def power_button_clicked(self):
        """Callback method for the Power button click event."""
        self.controller.power_button_clicked()

    def mute_button_clicked(self):
        """Callback method for the Mute button click event."""
        self.controller.mute_button_clicked()

    def channel_up_button_clicked(self):
        """Callback method for the Channel Up button click event."""
        self.controller.channel_up_button_clicked()

    def channel_down_button_clicked(self):
        """Callback method for the Channel Down button click event."""
        self.controller.channel_down_button_clicked()

    def volume_up_button_clicked(self):
        """Callback method for the Volume Up button click event."""
        self.controller.volume_up_button_clicked()

    def volume_down_button_clicked(self):
        """Callback method for the Volume Down button click event."""
        self.controller.volume_down_button_clicked()