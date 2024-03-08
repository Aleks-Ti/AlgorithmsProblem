class Solution(object):
    numpad = {
        1: None,
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz',
    }

    def letterCombinations(self, digits):
        result = []

        def other(digits, prefix=''):
            if not digits:  # Если digits становится пустой строкой
                result.append(prefix)  # Добавляем текущий prefix к результату
            else:
                first_digit = digits[0]  # Берем первую цифру
                letters = self.numpad[int(first_digit)]  # Получаем соответствующие буквы
                for letter in letters:
                    other(digits[1:], prefix + letter)  # Рекурсивно вызываем для остальных цифр

        if digits:
            other(digits)
        
        return result


if __name__ == '__main__':
    data_keyboard = '23'
    a = Solution()
    print(a.letterCombinations(data_keyboard))
