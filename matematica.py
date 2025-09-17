import consts
import random

def which_level():
    """
    check which level and how much exercises
    :return: list of all the exercises every exercise:
            [the exercise[number1, the_math, number2], the result]
    """
    the_level = int(input(consts.WHICH_LEVEL))
    how_many_exercise = int(input(consts.HOW_MANY_EXERCISE))
    all_numbers = make_exercises(the_level, how_many_exercise)
    return all_numbers

def make_exercises(the_level, how_many_exercise):
    """
    make list of all the exercise and make sure every exercise appear once
    :param the_level:
    :param how_many_exercise:
    :return: the list of all exercises
    """
    all_numbers = []
    for i in range(how_many_exercise):
        the_numbers = find_numbers(the_level)
        the_math = get_calculation()
        the_result = exercise_result(the_numbers, the_math)
        exercise = [the_numbers[1], the_math, the_numbers[0]]
        while appear_in_all_numbers(all_numbers, exercise):
            the_numbers = find_numbers(the_level)
            the_math = get_calculation()
            the_result = exercise_result(the_numbers, the_math)
            exercise = [the_numbers[1], the_math, the_numbers[0]]
        all_numbers.append([make_the_list_string(exercise), the_result])
    return all_numbers

def find_numbers(the_level):
    """
    check in which level the numbers should be
    :param the_level: the level
    :return: the numbers in list in the right level
    """
    if the_level == 1:
        return easy_level()
    elif the_level == 2:
        return medium_level()
    return hard_level()

def easy_level():
    """
    the numbers between 1-9
    :return: list of the numbers in easy level
    """
    number1 = random.randint(1,9)
    number2 = random.randint(1,9)
    the_numbers = [number1, number2]
    return the_numbers
def medium_level():
    """
    the numbers between 10-99
    :return: list of the numbers in medium level
    """
    number1 = random.randint(10,99)
    number2 = random.randint(10,99)
    the_numbers = [number1, number2]
    return the_numbers
def hard_level():
    """
    the numbers between 100-999
    :return: list of the numbers in hard level
    """
    number1 = random.randint(100,999)
    number2 = random.randint(100,999)
    the_numbers = [number1, number2]
    return the_numbers

def get_calculation():
    """
    if the_math = 1 it +
    if the_math = 2 it -
    if the_math = 3 it *
    if the_math = 4 it /
    :return: the_math
    """
    the_math = random.randint(1, 4)
    if the_math == 1:
        return consts.ADDITION
    elif the_math == 2:
        return consts.SUBTRACTION
    elif the_math == 3:
        return consts.MULTIPLICATION
    return consts.DIVISION

def exercise_result(the_numbers, the_math):
    """
    find the result
    :param the_numbers: the numbers
    :param the_math: which calculation to do
    :return: the answear of the exrcise
    """
    numbers = sort_the_numbers(the_numbers)
    if the_math == consts.ADDITION:
        return numbers[1] + numbers[0]
    elif the_math == consts.SUBTRACTION:
        return  numbers[1] - numbers[0]
    elif the_math == consts.MULTIPLICATION:
        return  numbers[1] * numbers[0]
    else:
        return numbers[1] // numbers[0]
def sort_the_numbers(the_numbers):
    """
    make the list from the smallest to biggest
    :param the_numbers: the list
    :return: the list after sorted
    """
    numbers = the_numbers.copy()
    return numbers.sort()

def appear_in_all_numbers(all_numbers, exercise):
    """
    check if the exercise already appear in all numbers
    :param all_numbers:
    :param exercise:
    :return: true if it appears false if not
    """
    for i in all_numbers:
        if i[0] == exercise:
            return True
    return False

def make_the_list_string(the_list):
    """
    make the list to string
    :param the_list:
    :return: the string
    """
    st = ""
    for i in the_list:
        st += str(i)
    return st