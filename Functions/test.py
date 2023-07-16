def solution(N):
    enable_print = 0
    reversed_digits = []

    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
        elif enable_print == 1:
            reversed_digits.append(str(N % 10))
        N = N // 10

    reversed_number = int(''.join(reversed_digits))
    print(reversed_number)
