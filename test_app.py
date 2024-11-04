import pytest
from app import hello

def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hola Mundo\n"