import random

WORDS_LIST = \
    ['travel', 'person', 'strong', 'street', 'turtle', 'purple', 'orange',
     'potato', 'august', 'better', 'breath', 'market', 'repair', 'school',
     'colony', 'online', 'carrot', 'rabbit', 'doctor']


def get_player_name():
    print("Hello player")
    print("Please enter your name:")
    return input()


def get_random_word(words_list):
    return random.choice(words_list)


def put_letter_in_state(letter, word, state):
    for i in range(len(word)):
        if word[i] == letter:
            state[i] = letter


def list_to_str(list):
    str = ""
    for c in list:
        str = str + c
    return str


def hanging_man_round(player_name, word, state):
    print("Hello " + player_name + ". Please guess your next letter: " + list_to_str(state))
    letter = input()

    while len(letter) != 1:
        print("please enter only one letter")
        letter = input()

    if letter in word:
        put_letter_in_state(letter, word, state)
        print("The letter", letter, "is in the word:", list_to_str(state))
    else:
        print("The letter", letter, "is not in the word:", list_to_str(state))


def hanging_man(words_list):
    player_name = get_player_name()
    player_word = get_random_word(words_list)
    player_state = ['_' for c in player_word]

    while '_' in player_state:
        hanging_man_round(player_name, player_word, player_state)

    if '_' not in player_state:
        print(player_name, "you won!")
    return


hanging_man(WORDS_LIST)