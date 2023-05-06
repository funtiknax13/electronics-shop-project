from src.item import Item


class MixinLang:

    __lang = "EN"

    def change_lang(self):
        if self.__lang == "EN":
            self.__lang = "RU"
        else:
            self.__lang = "EN"
        return self

    @property
    def language(self):
        return self.__lang


class Keyboard(Item, MixinLang):
    pass
