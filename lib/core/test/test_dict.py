from core.dict import Dict
import pytest


def test_add():
    # Добавим элемент. Посмотрим есть ли он!
    dict =Dict()
    dict.add("key", "value")
    if dict.get("key")=="value":
        assert True
