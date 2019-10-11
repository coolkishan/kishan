def calculate_length(n):
    length = 0
    while n != 0:
        length = length + 1
        n = n // 10
    return length
def sum_of_digits(num):
    remainder = result = 0
    length = calculate_length(num)
    while num > 0:
        rem = num % 10
        result = result + (rem ** length)
        num = num // 10
    return result
def print_dissarium():
    result = 0
    print(" Dissarium no.between 1 and 100 are:")
    for i in range(1, 100):
        result = sum_of_digits(i)
                if result == i:
                     print(result)
print_dissarium()


