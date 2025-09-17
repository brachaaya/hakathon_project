import consts


def get_custom_dict():
    """
    a function that gets words and roots from user and creates a dictionary from them,
    words are the keys and roots are the values
    :return: dictionary of words and roots
    """
    custom_hebrew_dict = {}
    word = " "
    print("Enter words and their roots, Enter -1 at the end to stop")
    while word != "-1":
        word = input("Enter word and its root: ")
        if word != "-1":
            root = input()
            custom_hebrew_dict[word] = root

    return custom_hebrew_dict


def choose_level():
    """
    the user chooses a level and gets a dictionary based on his choice
    :return: a dictionary based on the level
    """
    level = int(input("Choose your level: \n1: Easy \n2: Hard \n3: choose your own words and level \n"))
    if level == 1:
        return consts.EASY_HEBREW_DICT
    if level == 2:
        return consts.HARD_HEBREW_DICT
    else:
        return get_custom_dict()
