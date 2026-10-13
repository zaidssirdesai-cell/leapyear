from lyear import leapyear

def test_is():
    assert leapyear(2016) == "is a leap year"

def test_isnot():
    assert leapyear(2017) == "is not aleap year"