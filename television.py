class Television:
    """
    A class representing a simple television.

    Attributes:
        MIN_VOLUME (int): The minimum volume level.
        MAX_VOLUME (int): The maximum volume level.
        MIN_CHANNEL (int): The minimum channel number.
        MAX_CHANNEL (int): The maximum channel number.

    Methods:
        __init__: Initializes a new Television instance.
        mute: Mutes or unmutes the television.
        power: Turns the television on or off.
        channel_up: Increases the channel by one.
        channel_down: Decreases the channel by one.
        volume_up: Increases the volume by one.
        volume_down: Decreases the volume by one.
        __str__: Returns a string representation of the television.

    """

    # Class variables
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 15
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 10

    def __init__(self) -> None:
        """
        Initializes a new Television instance.

        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def mute(self) -> None:
        """
        Mutes or unmutes the television.

        """
        if self.__status is True:
            self.__muted = not self.__muted

    def power(self) -> None:
        """
        Turns the television on or off.

        """
        self.__status = not self.__status

    def channel_up(self) -> None:
        """
        Increases the channel by one.

        """
        if self.__status is True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the channel by one.

        """
        if self.__status is True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by one.

        """
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by one.

        """
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a string representation of the television.

        """
        if self.__muted is True:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

