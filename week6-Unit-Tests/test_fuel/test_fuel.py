from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("4/1")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0.5) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

