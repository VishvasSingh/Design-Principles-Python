from abc import ABC, abstractmethod


class AbstractObserver(ABC):
    """
    Abstract class for observers
    """

    @abstractmethod
    def on_receiving_event(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
