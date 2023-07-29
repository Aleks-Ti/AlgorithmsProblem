def bicycle_buy(
    moneybox: list,
    bicycle_price: int,
    number_of_days: int,
    left,
    right,
    flag,
    result=['-1', '-1'],
):
    if right <= left:  # промежуток пуст
        if moneybox[right] >= bicycle_price:
            result[-1] = right + 1
            return result
        else:
            return result
    mid = (left + right) // 2

    if moneybox[mid] >= bicycle_price and flag == True:
        result[-1] = mid + 1
        return result
    if moneybox[mid] >= bicycle_price and flag == False:
        result[0] = mid + 1
        return result
    elif bicycle_price < moneybox[mid]:
        return bicycle_buy(
            moneybox, bicycle_price, number_of_days, left, mid, flag
        )
    elif bicycle_price >= moneybox[mid]:
        # left = mid + 1
        # right = -1
        return bicycle_buy(
            moneybox,
            bicycle_price,
            number_of_days,
            mid + 1,
            len(moneybox) - 1,
            flag,
        )

    else:
        return result


if __name__ == '__main__':
    number_of_days = 6
    moneybox = [int(x) for x in '1 2 4 4 4 4'.split()]
    bicycle_price = 1
    asd = bicycle_buy(
        moneybox,
        bicycle_price,
        number_of_days,
        left=0,
        right=(number_of_days - 1),
        flag=False,
    )
    dsa = bicycle_buy(
        moneybox[asd[0]:],
        bicycle_price * 2,
        number_of_days,
        left=0,
        right=(number_of_days - 1),
        result=asd,
        flag=True,
    )
    if dsa is None:
        print(' '.join([str(x) for x in asd]))
    else:
        print(' '.join([str(x) for x in dsa]))
