import pytest

from src.cinema_entry import can_watch


@pytest.mark.parametrize(
    "age",
    [
        16,  # exactly 16 may watch (FAILS: bug, code uses > instead of >=)
        17,  # just above 16
        40,  # adult
    ],
)
def test_age_16_or_older_returns_true(age):
    # Act
    result = can_watch(age)
    # Assert
    assert result is True


@pytest.mark.parametrize(
    "age",
    [
        0,  # youngest valid age
        10,  # child
        15,  # just below 16
    ],
)
def test_age_below_16_returns_false(age):
    # Act
    result = can_watch(age)
    # Assert
    assert result is False


@pytest.mark.parametrize(
    "age",
    [
        -1,  # just below zero
        -20,  # negative number
    ],
)
def test_negative_age_raises_value_error(age):
    # Act and Assert
    with pytest.raises(ValueError):
        can_watch(age)


@pytest.mark.parametrize(
    "age",
    [
        "16",  # string
        16.0,  # float
        None,  # no value
        True,  # bool is not a valid int
    ],
)
def test_non_integer_age_raises_type_error(age):
    # Act and Assert
    with pytest.raises(TypeError):
        can_watch(age)