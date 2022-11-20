while True:
    short_steak_hor, long_steak_min = map(int, input('введите текущее время: ').split(':'))
    if short_steak_hor <= 12 and long_steak_min <= 59:
        if short_steak_hor == 12:
            short_steak_hor = 0
        break
    print('\nколичество часаов не должно превышать 12 \nтакже количество минут не должно превышать 59\n')


sum_steak = long_steak_min * 6 - (long_steak_min * 0.5 + short_steak_hor * 30)
if sum_steak < 0:
    sum_steak *= -1
if sum_steak > 180:
    sum_steak = 360 - sum_steak
print(sum_steak, 'degree')
# short = 10 * 6, long = 10 * 0.5


