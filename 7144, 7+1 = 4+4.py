def luck_check(num : str):
    num_sum_first = 0
    num_sum_second = 0
    for i in num[0:len(num) // 2]:
        num_sum_first += int(i)
    for i in num[len(num) // 2: len(num)]:
        num_sum_second += int(i)

    if num_sum_second == num_sum_first:
        return True
    return False


with open('luck_check.txt', 'w') as check:

    for i in range(0, 10000):
        if len(str(i)) % 2 != 0:
            if luck_check(f'0{i}') == True:
                check.write(f'0{i} \n')
        else:
            if luck_check(f'{i}') == True:
                check.write(f'{i} \n')