def sum_of_multiples(number_upto: int, multiple_number: list) -> int:
    # COACHES' NOTE: I feel like the functionality could be divided into two functions to avoid such deep indentation.
    total = 0
    # COACHES' NOTE: i? 
    for i in range(0, number_upto):
        # COACHES' NOTE: You don't a flag for this. Break statements would be better.
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

# COACHES' NOTE: decent code, but could use more functions to help organize.
