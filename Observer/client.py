from concrete_observer import GermanSpeakingConcreteObserver, FrenchSpeakingConcreteObserver
from subject import Subject


if __name__ == '__main__':
    subject = Subject()
    german_observer = GermanSpeakingConcreteObserver()
    french_observer = FrenchSpeakingConcreteObserver()

    subject.subscribe(observer=german_observer)
    subject.subscribe(observer=french_observer)

    subject.publish()

    subject.unsubscribe(observer=german_observer)

    subject.publish()
