def count_digits(number):
    count = 0
    remaining_value = number
    while remaining_value > 0:
        remaining_value = remaining_value // 10
        count += 1
    return count

def find_proper_divisors(number):
    divisors = [1]
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def sieve_of_eratosthenes(number):
    numbers = [i for i in range(1, number + 1)]
    i = 0
    while len(numbers) >= i:
        for num in numbers[i + 2:]:
            possible_prime = numbers[i + 1]
            if num % possible_prime == 0:
                numbers.remove(num)
        print(numbers)
        i += 1
    return numbers
        

if __name__=='__main__':
    print(sieve_of_eratosthenes(10))