from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self, text: str) -> None:
        pass


class Scannable(ABC):
    @abstractmethod
    def scan(self) -> str:
        pass


class Faxable(ABC):
    @abstractmethod
    def fax(self, number: str) -> None:
        pass


class Copiable(ABC):
    @abstractmethod
    def copy(self) -> None:
        pass


class SimplePrinter(Printable):
    def print(self, text: str) -> None:
        print(text)


class MultiFunctionDevice(Printable, Scannable, Faxable, Copiable):
    def print(self, text: str) -> None:
        print(f"[PRINT] {text}")

    def scan(self) -> str:
        return "scanned_content"

    def fax(self, number: str) -> None:
        print(f"[FAX] {number}")

    def copy(self) -> None:
        print("[COPY]")