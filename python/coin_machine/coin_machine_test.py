from coin_machine import get_change

def test_can_take_a_single_coin_integer():
    result = get_change("2")
    assert result == "1 2p"

def test_can_take_a_double_coin_integer():
    result = get_change("4")
    assert result == "2 2p"

def test_can_take_integer_requiring_2_different_coins():
    result = get_change("42")
    assert result == "2 20p, 1 2p"

def test_can_take_integer_requiring_4_different_coins():
    result = get_change("342")
    assert result == "1 £2, 1 £1, 2 20p, 1 2p"

def test_can_take_decimals():
    result = get_change("3.42")
    assert result == "1 £2, 1 £1, 2 20p, 1 2p"

def test_can_take_the_pd_sign_at_the_beginning_for_integer():
    result = get_change("£342")
    assert result == "1 £2, 1 £1, 2 20p, 1 2p"

def test_can_take_the_pd_sign_at_the_beginning_for_decimal():
    result = get_change("£3.42")
    assert result == "1 £2, 1 £1, 2 20p, 1 2p"

def test_returns_an_error_if_given_too_many_decimals():
    result = get_change("£3.454")
    assert result == "Input has too many decimals"

def test_returns_an_error_if_given_not_a_number():
    result = get_change("234sdf")
    assert result == "Input is invalid"

def test_can_take_a_coin_limit():
    coins = [
        {
            "name": "£2",
            "count": 0,
            "value": 200,
            "limit": 1
        },
        {
            "name": "£1",
            "count": 0,
            "value": 100,
            "limit": 1
        },
        {
            "name": "50p",
            "count": 0,
            "value": 50,
            "limit": "none"
        },
        {
            "name": "20p",
            "count": 0,
            "value": 20,
            "limit": "none"
        },
        {
            "name": "10p",
            "count": 0,
            "value": 10,
            "limit": "none"
        },
        {
            "name": "5p",
            "count": 0,
            "value": 5,
            "limit": "none"
        },
        {
            "name": "2p",
            "count": 0,
            "value": 2,
            "limit": "none"
        },
        {
            "name": "1p",
            "count": 0,
            "value": 1,
            "limit": "none"
        }
    ]

    result = get_change("£4.42", coins)
    assert result == "1 £2, 1 £1, 2 50p, 2 20p, 1 2p"

def test_can_take_multiple_coin_limit():
    coins = [
        {
            "name": "£2",
            "count": 0,
            "value": 200,
            "limit": 1
        },
        {
            "name": "£1",
            "count": 0,
            "value": 100,
            "limit": 1
        },
        {
            "name": "50p",
            "count": 0,
            "value": 50,
            "limit": 4
        },
        {
            "name": "20p",
            "count": 0,
            "value": 20,
            "limit": "none"
        },
        {
            "name": "10p",
            "count": 0,
            "value": 10,
            "limit": "none"
        },
        {
            "name": "5p",
            "count": 0,
            "value": 5,
            "limit": "none"
        },
        {
            "name": "2p",
            "count": 0,
            "value": 2,
            "limit": "none"
        },
        {
            "name": "1p",
            "count": 0,
            "value": 1,
            "limit": "none"
        }
    ]

    result = get_change("£10.42", coins)
    assert result == "1 £2, 1 £1, 4 50p, 27 20p, 1 2p"