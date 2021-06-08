def sum_of_multiples(number_upto: int, multiple_number: list) -> int:
    total = 0
    for i in range(0, number_upto):
        flag = False
        for number in multiple_number:
            if number == 0:
                continue
            if i % number == 0 and not flag:
                total += i
                flag = True
    return total


if __name__ == '__main__':
    sum_of_multiples(100, [3, 5])
