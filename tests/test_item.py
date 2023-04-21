"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


item1 = Item("Веб-камера", 5000, 15)
item2 = Item("Флешка", 500, 100)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 75000
    assert item2.calculate_total_price() == 50000


def test_apply_discount():
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 2500
    item2.apply_discount()
    assert item2.price == 250

