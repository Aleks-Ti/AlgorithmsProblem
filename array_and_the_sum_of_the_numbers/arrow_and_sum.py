# массив с числами
nums = [2, 4, 5, 1, 8]

# сумма
target = 155


# функция, которая найдёт ответ
def twoSum(nums: int, target: int) -> int:
    # сообщение по умолчанию
    answer = 'В массиве нет такой пары числе, что составят в сумме запрошенное число!'
    # запускаем первый цикл
    for i in range(len(nums)):
        #  запускаем второй цикл
        for j in range(i + 1):
            # если получили нужный результат —
            if target == nums[i] + nums[j]:
                # меняем ответ и добавляем в него индексы элементов
                answer = 'Ответ: ' + str(i) + ' и ' + str(j)
    # выводим результат работы функции
    return answer


# запускаем код
print(twoSum(nums, target))