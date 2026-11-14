import pytest

from src.cinema_price import ticket_price


@pytest.mark.parametrize(
    "ticket_count, expected_price",
    [
        (0, 0),  # zero tickets costs zero (FAILS: bug, code returns 1200)
        (1, 1200),  # one ticket
        (3, 3600),  # three tickets
    ],
)
def test_valid_ticket_count_returns_count_times_1200(ticket_count, expected_price):
    # Act
    result = ticket_price(ticket_count)
    # Assert
    assert result == expected_price


@pytest.mark.parametrize(
    "ticket_count",
    [
        -1,  # just below zero
        -50,  # negative number
    ],
)
def test_negative_ticket_count_raises_value_error(ticket_count):
    # Act and Assert
    with pytest.raises(ValueError):
        ticket_price(ticket_count)


@pytest.mark.parametrize(
    "ticket_count",
    [
        "3",  # string
        2.0,  # float
        None,  # no value
        True,  # bool is not a valid int
    ],
)
def test_non_integer_ticket_count_raises_type_error(ticket_count):
    # Act and Assert
    with pytest.raises(TypeError):
        ticket_price(ticket_count)


# Demo: push to a feature branch triggers the workflow