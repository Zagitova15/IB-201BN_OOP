from abc import ABC, abstractmethod
from typing import List


class Notifier(ABC):
    @abstractmethod
    def send(self, to: str, text: str) -> None:
        pass


class EmailNotifier(Notifier):
    def send(self, to: str, text: str) -> None:
        print(f"[EMAIL to={to}] {text}")


class SmsNotifier(Notifier):
    def send(self, to: str, text: str) -> None:
        print(f"[SMS to={to}] {text}")


class PushNotifier(Notifier):
    def send(self, to: str, text: str) -> None:
        print(f"[PUSH to={to}] {text}")


class FakeNotifier(Notifier):
    def __init__(self):
        self.sent_messages = []

    def send(self, to: str, text: str) -> None:
        self.sent_messages.append((to, text))


class NotificationService:
    def __init__(self, notifiers: List[Notifier]):
        self.notifiers = notifiers

    def notify(self, to: str, text: str) -> None:
        for notifier in self.notifiers:
            notifier.send(to, text)