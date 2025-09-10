n = int(input())

if n < 0:
    error = 1 / 0 # перевірка для e-olimp, чи можуть бути подані на вхід відʼємні числа

od = n % 10
de = n // 10



print(od + de)