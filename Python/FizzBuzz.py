"""
FizzBuzz...
Hardly dynamic programming but here for the record
"""

fizzBuzzDictionary = {3:"fizz", 5:"buzz"} # , 7:"pop"

def fizzBuzzGenerator(start = 1):
    currentNumber = start
    while True:
        answer = ""
        for special in fizzBuzzDictionary:
            if currentNumber % special == 0:
                answer += fizzBuzzDictionary[special]
        if answer == "":
            answer = currentNumber
        yield answer
        currentNumber += 1

def printFizzBuzzRange(start, end):
    gen = fizzBuzzGenerator(start = start)
    for _ in range(end - start):
        print(next(gen))

if __name__ == "__main__":
    printFizzBuzzRange(1, 101)
