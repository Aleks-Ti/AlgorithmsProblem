def buble_sort(list_n, n):
    for i in range(1, n):
        # if list_n == sorted(list_n):
        # break

        flag = False
        for j in range(0, n - 1):
            if list_n[j] > list_n[j + 1]:
                list_n[j], list_n[j + 1] = list_n[j + 1], list_n[j]
                flag = True
        if flag:
            print(*list_n)
    return None


if __name__ == '__main__':
    n = int(input())
    list_n = list(map(int, input().split()))
    buble_sort(list_n, n)
