from typing import Dict


class SingletonMeta(type):
    """Regular Singleton implementation"""

    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        # checking class instances
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# our class which will be a singletone
class DataBase(metaclass=SingletonMeta):

    def __init__(self, url: str) -> None:
        self.url = url

    def connect_to_db(self) -> str:
        return f"Connected to db by this url: {self.url}"


# tests
a = DataBase("A database connection")
b = DataBase("Some dummy str rewrite a db connection")

print(id(a), a, a.connect_to_db())
print(id(b), b, b.connect_to_db())
