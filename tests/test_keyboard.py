import pytest


from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_str():
    assert str(kb) == "Dark Project KD87A"


def test_change_lang():
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

    with pytest.raises(AttributeError) as ex:
        kb.language = 'CH'
    assert "property 'language' of 'Keyboard' object has no setter" in str(ex.value)
