import pytest


from src.phone import Phone


phone1 = Phone("iPhone", 75000, 5, 2)


def test_repr():
    assert repr(phone1) == "Phone('iPhone', 75000, 5, 2)"


def test_number_of_sim_setter():
    with pytest.raises(ValueError) as ex:
        phone1.number_of_sim = 0
    assert "Количество физических SIM-карт должно быть целым числом больше нуля." in str(ex.value)