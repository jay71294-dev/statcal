from Calculator.Division import division
from Calculator.Square import square
from Calculator.Square_rot import squar_rot
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean


def popstand(numbers):
    num_values = len(numbers)

    result = mean(numbers)
    total = 0
    for numb in numbers:
        result2 = subtraction(numb, result)
        sq = square(result2)
        total = addition(total, sq)
    return squar_rot(division(num_values, total))
