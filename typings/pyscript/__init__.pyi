# pylint: disable-all

class Element:

    def __init__(self, id: str) -> None:
        self.value: str


    def write(self, text: str) -> None: ...
