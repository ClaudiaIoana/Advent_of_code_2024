if __name__ == '__main__':
    # Open the file
    with open('input_file.txt', 'r') as file:  # Replace 'data.txt' with your file name
        data1 = []
        data2 = []
        data = []
        for line in file:
            numbers = list(map(int, line.split()))
            data.append(numbers)
            data1.append(numbers[0])
            data2.append(numbers[1])

    #Part 1
    data11 = sorted(data1)
    data12 = sorted(data2)
    sum = 0

    for i in range(0, len(data1)):
        sum += abs(data11[i] - data12[i])
    print(sum)

    #Part 2
    sum2 = 0
    for i in data1:
        print(i, data2.count(i))
        sum2 += i * data2.count(i)
    print(sum2)


