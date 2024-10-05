from abstract_observer import AbstractObserver


class GermanSpeakingConcreteObserver(AbstractObserver):
    def __init__(self):
        pass

    def on_receiving_event(self):
        print("Received Event, Guten tag !!")

    def __str__(self):
        return "German Observer"


class FrenchSpeakingConcreteObserver(AbstractObserver):
    def __init__(self):
        pass

    def on_receiving_event(self):
        print("Received Event, Bonjour !!")

    def __str__(self):
        return "French Observer"
