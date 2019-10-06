default_coins = [
    {
        "name": "£2",
        "count": 0,
        "value": 200,
        "limit": "none"
    },
    {
        "name": "£1",
        "count": 0,
        "value": 100,
        "limit": "none"
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

def get_change(amount, coins = default_coins):
    # only required when running script multiple times (ie in tests) or if counts not set
    coins = reset_counts(coins)

    remaining_amount = parse_input(amount)

    if isinstance(remaining_amount, str):
        return remaining_amount

    for coin in coins:
        while (remaining_amount >= coin["value"]) and (getLimit(coin) > 0):
            coin["count"] += 1
            remaining_amount -= coin["value"]
            if isinstance(coin["limit"], int):
                coin["limit"] -=1

    if remaining_amount > 0:
        return "Not enough coins"

    return stringify_coins(coins)

def stringify_coins(coins):
    string = ""
    for coin in coins:
        if coin["count"] > 0:
            string += f'{str(coin["count"])} {coin["name"]}, '

    return string[:-2]

def parse_input(string_to_parse):
    amount = string_to_parse
    if(string_to_parse[0] == "£"):
        amount = string_to_parse[1:]
    try:
        return int(amount)
    except ValueError:
        try:
            undecimaled_amount = float(amount) * 100
            if undecimaled_amount.is_integer():
                return int(undecimaled_amount)
            return("Input has too many decimals")
        except ValueError:
            return("Input is invalid")

def reset_counts(coins):
    for coin in coins:
        coin["count"] = 0
    return coins

def getLimit(coin):
    if isinstance(coin["limit"], int):
        return coin["limit"]
    # Always return 1 if there's no limit
    return 1