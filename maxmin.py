def maxmin(input):
    lowest = input[0]
    highest = input[0]

    for num in input:
        if num > highest:
            highest = num
        elif num < lowest:
            lowest = num
    print(lowest, highest)


input = [100, -100]
maxmin(input)
