from jar import Jar
import pytest

def test_init():
    jar=Jar()
    assert jar.capacity==12
    assert jar.size==0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar()
    with pytest.raises (ValueError):
        assert jar.deposit(15)==ValueError
    jar.deposit(5)
    assert jar.size==5


def test_withdraw():
    jar=Jar()
    with pytest.raises (ValueError):
        assert jar.withdraw(5)==ValueError
    jar.deposit(5)
    jar.withdraw(4)
    assert jar.size==1

