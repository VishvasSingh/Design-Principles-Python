from abstract_observer import AbstractObserver
from typing import Set


class Subject:
    def __init__(self):
        self._observers: Set[AbstractObserver] = set()

    def subscribe(self, observer: AbstractObserver):
        self._observers.add(observer)

    def unsubscribe(self, observer: AbstractObserver):
        self._observers.remove(observer)
        print(f"Successfully unsubscribed -> {str(observer)}")

    def publish(self):
        for each_observer in self._observers:
            each_observer.on_receiving_event()
