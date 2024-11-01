# ruff: noqa: N801 N802

class HTMLElement:
    value: str

class document:
    @staticmethod
    def getElementById(name: str) -> HTMLElement: ...
