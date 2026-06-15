import json
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Order:
    id: str
    price: float
    qty: int
    customer_email: str


class OrderLoader:
    @staticmethod
    def load(json_path: str) -> List[dict]:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)


class OrderValidator:
    @staticmethod
    def parse_and_validate(raw_data: List[dict]) -> List[Order]:
        orders = []
        for item in raw_data:
            if "id" not in item or "price" not in item or "qty" not in item or "email" not in item:
                raise ValueError("Invalid order payload")
            if item["qty"] <= 0:
                raise ValueError("qty must be positive")
            orders.append(Order(item["id"], float(item["price"]), int(item["qty"]), item["email"]))
        return orders


class OrderCalculator:
    @staticmethod
    def calculate_total(orders: List[Order]) -> float:
        return sum(o.price * o.qty for o in orders)


class OrderReportFormatter:
    @staticmethod
    def format(orders: List[Order], total: float) -> str:
        return f"Orders count: {len(orders)}\nTotal: {total:.2f}\n"


class EmailSender:
    @staticmethod
    def send(to: str, subject: str, body: str) -> None:
        print(f"[EMAIL to={to}] {subject}\n{body}")


class OrderReportService:
    def __init__(self,
                 loader: OrderLoader,
                 validator: OrderValidator,
                 calculator: OrderCalculator,
                 formatter: OrderReportFormatter,
                 sender: Optional[EmailSender] = None):
        self.loader = loader
        self.validator = validator
        self.calculator = calculator
        self.formatter = formatter
        self.sender = sender

    def make_and_send_report(self, json_path: str) -> str:
        raw = self.loader.load(json_path)
        orders = self.validator.parse_and_validate(raw)
        total = self.calculator.calculate_total(orders)
        report = self.formatter.format(orders, total)

        if self.sender:
            for o in orders:
                self.sender.send(o.customer_email, "Your order report", report)

        return report