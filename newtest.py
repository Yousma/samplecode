import random

def generate_random_numbers(n):
    numbers = []
    for _ in range(n):
        numbers.append(random.randint(1, 100))
    return numbers

def mean(numbers):
    total = sum(numbers)
    return total / len(numbers)

def median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        return numbers[n // 2]

def mode(numbers):
    freq_dict = {}
    for num in numbers:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    max_freq = max(freq_dict.values())
    modes = [num for num, freq in freq_dict.items() if freq == max_freq]
    return modes

def main():
    numbers = generate_random_numbers(100)
    mean_value = mean(numbers)
    median_value = median(numbers)
    mode_value = mode(numbers)
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Mode: {mode_value}")

if __name__ == "__main__":
    main()
