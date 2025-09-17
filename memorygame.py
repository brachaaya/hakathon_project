import random
import time

BOARD_WORDS = 16

EMPTY = "null"

BOARD_SIZE = 4
DELAY = 2
# board = []
#
# LIST_FOR_GAME =  ['travel', 'person', 'strong', 'street', 'turtle', 'purple', 'orange',
#      'potato', 'august', 'better', 'breath', 'market', 'repair', 'school',
#      'colony', 'online', 'carrot', 'rabbit', 'doctor']
#
# for i in range(BOARD_SIZE):
#     board.append([0] * BOARD_SIZE)

def the_list_for_game(the_list):
    list1 = random_list(the_list)
    list2 = make_another_list(the_list, list1)
    the_board = create_board(list1, list2)
    return the_board

def random_list(the_list):
    list_1 = the_list.keys()
    board_list = []
    for i in range(len(the_list)):
        board_list.append(random.choice(list_1))
    for i in range(len(the_list), BOARD_WORDS//2):
        board_list.append(EMPTY)
    return board_list

def make_another_list(board_list, the_list):
    another_list = []
    for i in range(the_list):
        another_list.append(board_list.get(i))
    return another_list

def create_board(list1, list2):
    all_list = list2 + list1
    random.shuffle(all_list)
    the_board = []
    counter = 0
    for y in range(len(list1)//2):
        the_line = []
        for x in range(len(list2)//2):
            the_line.append(all_list[counter])
            counter += 1
        the_board.append(the_line)
    return the_board

def check_place(place1, place2, the_dictionary):
    if place1 in the_dictionary.keys():
        if place2 == the_dictionary.get(place1):
            return True
    if place2 in the_dictionary.keys():
        if place1 == the_dictionary.get(place2):
            return True
    return False

# def clear():
#     print("\n"*10)
#
#
# def print_mat(mat):
#     for row in mat:
#         for cell in row:
#             print(cell, end="\t")
#         print()
#
#
# def fill_board(mat):
#     half = BOARD_SIZE * BOARD_SIZE // 2
#     places = []
#     for i in range(half):
#         places.append(LIST_FOR_GAME[i])
#
#     places = places * 2
#     random.shuffle(places)
#
#     i = 0
#     for y in range(len(mat)):
#         for x in range(len(mat[y])):
#             mat[y][x] = places[i]
#             i+=1
#
#
# def show_board(mat, matches, place1=None, place2=None):
#     for y in range(len(mat)):
#         for x in range(len(mat[y])):
#             word = mat[y][x]
#             if (x, y) in matches:
#                 print(word, end="\t")
#             else:
#                 if place1 is None and place2 is None:
#                     print('█████', end="\t")
#                 elif place1 is not None and place2 is None:
#                     if place1 == (x, y):
#                         print(word, end="\t")
#                     else:
#                         print('█████', end="\t")
#                 else:
#                     if place1 == (x, y):
#                         print(word, end="\t")
#                     elif place2 == (x, y):
#                         print(word, end="\t")
#                     else:
#                         print('█████', end="\t")
#         print()
#     print("-"*15)
#
#
# def get_cords(matches, point=(-2, -2)):
#     x = int(input("Enter x value: ")) - 1
#     y = int(input("Enter y value: ")) - 1
#     while not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE) and [x, y] not in matches and (x, y) != point:
#         x = int(input("Enter x value: ")) - 1
#         y = int(input("Enter y value: ")) - 1
#     return x, y
#
#
# # Setup
# fill_board(board)
# running = True
# places = []
# start_time = time.time()
#
# while running:
#     show_board(board, places)
#     point1 = get_cords(places)
#     show_board(board, places, point1)
#     point2 = get_cords(places, point1)
#     show_board(board, places, point1, point2)
#     num1 = board[point1[1]][point1[0]]
#     num2 = board[point2[1]][point2[0]]
#     time.sleep(DELAY)
#     if num1 != num2:
#         clear()
#         continue
#     places.append(point1)
#     places.append(point2)
#     clear()
#     if len(places) == BOARD_SIZE * BOARD_SIZE:
#         running = False
#
# secs = time.time() - start_time
# print(f"Well done! it took you {secs} seconds.")