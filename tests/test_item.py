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


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 7  # в файл
    item3 = Item.all[2]
    assert item3.name == 'Смартфон'
    assert item3.quantity == 1
    item4 = Item.all[6]
    assert item4.price == 75


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('a') == 'a'


def test_repr_str():
    assert repr(item1) == "Item('Веб-камера', 2500.0, 15)"
    assert str(item2) == 'Флешка'
