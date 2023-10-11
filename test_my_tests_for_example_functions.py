import pytest

from example_functions import my_adder, my_thermo_stat, have_digits

@pytest.mark.parametrize("a,b,c,out", [(1, 2, 3, 6), (4, 5, 6, 15), (-1, -2, 0, -3)])
def test_adder(a, b, c, out):
    output = my_adder(a, b, c)
    assert output == out

@pytest.mark.parametrize("temp, desired_temp, status", [(10, 26, 'Heat'), (32, 26, 'AC'), (26, 26, 'off')])
def test_thermo_stat(temp, desired_temp, status):
    output = my_thermo_stat(temp, desired_temp)
    assert output == status

@pytest.mark.parametrize("s, out", [('abc4e', 1), ('abcde', 0)])
def test_have_digits(s, out):
    output = have_digits(s)
    assert output == out
