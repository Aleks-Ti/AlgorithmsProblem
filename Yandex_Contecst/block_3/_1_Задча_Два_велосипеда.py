def bicycle_buy(
    moneybox: list,
    bicycle_price: int,
    number_of_days: int,
    count=0,
    result=['-1', '-1'],
    x1_bicycle=True,
):
    if count >= number_of_days:
        return ' '.join(result)

    for day in range(count, number_of_days):
        count += 1
        if moneybox[day] >= bicycle_price and x1_bicycle is True:
            x1_bicycle = False
            result[0] = str(day + 1)
            return bicycle_buy(
                moneybox,
                bicycle_price,
                number_of_days,
                count,
                result,
                x1_bicycle,
            )
        if moneybox[day] >= bicycle_price * 2 and x1_bicycle is False:
            result[-1] = str(day + 1)
            return ' '.join(result)

    return ' '.join(result)


if __name__ == '__main__':
    number_of_days = int(input())
    moneybox = [int(x) for x in input().split()]
    bicycle_price = int(input())
    print(bicycle_buy(moneybox, bicycle_price, number_of_days))
