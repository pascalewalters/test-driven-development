from chapter_1 import Dollar


def test_multiplication():
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount

