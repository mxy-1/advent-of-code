import pytest
import solution

@pytest.mark.parametrize('test_input,expected', [("1122", 3), ("1111", 4), ("1234", 0), ("91212129", 9)])
def test_inverse_captcha(test_input, expected):
    assert solution.inverse_captcha(test_input) == expected