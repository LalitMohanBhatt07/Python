def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    sorted_numbers=sorted(numbers)
    length=len(sorted_numbers)
    middle_index=len/2;
    
    if length%2==0:
        median=(sorted_numbers(middle_index))