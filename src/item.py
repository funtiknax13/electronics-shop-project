import csv
import os
from src.errors import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Name экземпляра класса item.
        """
        return self.__name

    def __add__(self, other):
        """
        Складывает товары по количеству
        """
        if not isinstance(other, self.__class__):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) <= 10:
            self.__name = name
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, file_name: str):
        """
        Формирует экземпляры класса из CSV файла
        """
        # file_name = "items.csv"
        path = os.path.join(os.getcwd(), "..", "src", file_name)
        try:
            with open(path, encoding="utf-8", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if "name" in row and "price" in row and "quantity" in row:
                        cls(row["name"], cls.string_to_number(row["price"]), cls.string_to_number(row["quantity"]))
                    else:
                        raise InstantiateCSVError(file_name)
        except FileNotFoundError:
            print(f"FileNotFoundError: Отсутствует файл {file_name}")
            return f"FileNotFoundError: Отсутствует файл {file_name}"


    @staticmethod
    def string_to_number(data: str):
        """
        Преобразование строки в число
        """
        if data.replace(".", "", 1).isdigit():
            return int(float(data))
        else:
            return data
