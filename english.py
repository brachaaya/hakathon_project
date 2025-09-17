def get_custom_dict():
    """
    the user creates its own dictionary
    :return: a dictionary. The keys are words in english, and the values are its meaning in hebrew
    """
    own_dict = {}
    word = " "
    print("Now you will create a dictionary of your own words.\n Please enter words and its meaning. \nEnter -1 at the end")
    while word != "-1" :
        word = input("Enter a word and its meaning: ")
        if word != "-1":
            meaning = input()
            own_dict[word] = meaning
    return own_dict

def choose_level():
    """
    the user chooses a level and gets a dictionary based on his choice
    :return: a dictionary
    """
    level = int(input("Choose your level :\n 1: Easy \n 2: Hard \n 3: choose your own words and level"))
    if level == 1 :
        return EASY_ENGLISH_DICT
    elif level == 2 :
        return HARD_ENGLISH_DICT
    else:
        return get_custom_dict()

dict = get_custom_dict()
print(dict)

