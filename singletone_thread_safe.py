from threading import Lock, Thread
from typing import Dict


class ThreadSafeSingletonMeta(type):
    """Thread-safe implementation of Singleton."""

    _instances: Dict = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        # locking thread first
        with cls._lock:
            # checking class instances
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


# our class which will be a singletone
class DataBase(metaclass=ThreadSafeSingletonMeta):

    def __init__(self, url: str) -> None:
        self.url = url

    def connect_to_db(self) -> None:
        print(f"Connected to database by this url: {self.url}")


# tests
def test_class(url: str) -> None:
    singleton_class = DataBase(url)
    print(id(singleton_class))
    print(singleton_class.url)


process1 = Thread(target=test_class, args=("this is a connection URL",))
process2 = Thread(target=test_class, args=("some dummy string",))

process1.start()
process2.start()
