def mode(L):
    # your code here
    numbers = {}
    max_times = 0
    mode_number = 0
    for i in L:
        if i not in numbers:
            numbers[i] = 0
        numbers[i] +=1
        if numbers[i] > max_times:
            max_times = numbers[i]
            mode_number = i
 
    return mode_number

print mode([1,3,4,5,5,5,5,6])