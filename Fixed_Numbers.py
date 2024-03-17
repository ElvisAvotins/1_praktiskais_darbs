def can_reduce_to_10_or_less(n):
#Check if the number n can be reduced to 10 or less through divisions by 2, 3, or 4.
#Any division resulting in a non-whole number is considered a stopping point.
    if n <= 10:
        return True
# If division by any of 2, 3, or 4 results in a non-whole number, stop that branch
    if n% 2 == 0 and can_reduce_to_10_or_less(n // 2):
        return True
    if n% 3 == 0 and can_reduce_to_10_or_less(n // 3) :
        return True
    if n% 4 == 0 and can_reduce_to_10_or_less(n // 4):
        return True
    return False
# Numbers between 20,000 and 30,000 divisible by 12
numbers = [i for i in range(20000, 30001) if i % 12 == 0]
# Filter numbers that can be reduced to 10 or less through the defined divisions
numbers_that_can_reduce = [n for n in numbers if can_reduce_to_10_or_less(n)]
print ("Numbers that can be reduced to 10 or less: ", numbers_that_can_reduce)
