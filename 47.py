def prime_factors_num(num):
    result = []

    while num % 2 == 0:
        result.append(2)
        num = num // 2

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num == 1:
            break

        while num % i == 0:
            result.append(i)
            num = num // i
    if num != 1:
        result.append(num)
    return len(set(result))


n = 647
save = {644: 3, 645: 3, 646: 3}
while True:
    save[n] = prime_factors_num(n)
    if save[n - 3] == 4 and save[n - 2] == 4 and save[n - 1] == 4 and save[n] == 4:
        print(n - 3)
        break
    n += 1