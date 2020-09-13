def tower_builder(n_floors):
    '''This function builts a tower of odd numbers'''
    return [' '*(n_floors - i - 1) + '*'*(2 * i + 1) + ' '*(n_floors - i - 1) for i in range(n_floors)]

def two_sum(numbers, target):
    '''
This function takes an array as an argument and a target number and returns the
indices of the two special numbers from the array, whose sum is equal to the
target number
    '''
    if len(numbers) == 0:
        return
    else:
        for num1 in numbers:
            for num2 in numbers:
                if num1 != num2 and num1 + num2 == target:
                    return [numbers.index(num1), numbers.index(num2)]

def count(string):
    '''
This function takes an argument string and returns the number of character in the
string as a dictionary.
    '''
    return {letter: string.count(letter) for letter in string}

def sqInRect(lng, wdth):
    '''
This function takes an argument length(lng) and width(wdth) and returns the maximum
number of squares of maximum side possible.
    '''
    if lng == wdth:
        return None

    squares = []
    while lng != wdth:
        if lng < wdth:
            squares.append(lng)
            wdth -= lng
        else:
            squares.append(wdth)
            lng -= wdth


    squares.append(1)
    return squares

def list_squared(m, n):
    def isSquaredDivisor(n):
        listOfDivisor = []
        for i in range(1, n + 1):
            if n % i == 0:
                listOfDivisor.append(i)

        return listOfDivisor


