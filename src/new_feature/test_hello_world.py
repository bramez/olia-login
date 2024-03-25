from hamcrest import assert_that, calling, raises

from src.new_feature.calculator import Calculator, NotANumberException


def test_successful_sum():
    calculator = Calculator()
    result = calculator.sum(2, 5)

    assert result == 7


def test_unsuccessful_sum():
    calculator = Calculator()

    assert_that(calling(calculator.sum).with_args(2, "patata"), raises(NotANumberException))

