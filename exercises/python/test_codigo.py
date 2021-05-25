from codigo import is_even
from codigo import divide

def test_is_even_number_is_even_return_true():
    assert is_even(2) is True


def test_divide_thrown_exception_when_dividing_by_zero():
    assert divide(2, 0) is False
