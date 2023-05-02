"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone


item1 = Item("Веб-камера", 5000, 15)
item2 = Item("Флешка", 500, 100)
phone1 = Phone("iPhone", 75000, 5, 2)


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
    assert len(Item.all) == 9  # в файл
    item3 = Item.all[4]
    assert item3.name == 'Смартфон'
    assert item3.quantity == 1
    item4 = Item.all[7]
    assert item4.price == 50


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('a') == 'a'


def test_repr_str():
    assert repr(item1) == "Item('Веб-камера', 2500.0, 15)"
    assert str(item2) == 'Флешка'


def test_add():
    assert item1 + phone1 == 20
    assert phone1 + phone1 == 10
    with pytest.raises(ValueError) as ex:
        phone1 + 3
    assert "Складывать можно только объекты Item и дочерние от них." in str(ex.value)

