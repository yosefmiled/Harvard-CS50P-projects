from twttr import shorten
import pytest

def test_word():
     assert shorten("hello") == "hll"
     assert shorten("twitter") == "twttr"

def test_phrase():
     assert shorten("hello world") == "hll wrld"
     assert shorten("yosef miled is the best footballer in the world") == "ysf mld s th bst ftbllr n th wrld"

def test_upper():
     assert shorten("HELLO TUNISIA") == "HLL TNS"

def test_numbers():
     assert shorten("i have 3 flags") ==" hv 3 flgs"

def test_ponc():
     assert shorten("what??, ok!") == "wht??, k!"


