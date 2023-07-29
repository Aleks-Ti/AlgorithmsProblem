
def isPalindrome(number):
    count = -1
    number = str(number)
    for num in number:
        if num == number[count]:
            count -= 1
            continue
        return False
    return True


if __name__ == '__main__':
    print(isPalindrome(int(input())))
