import time
import matematica
import pygame

dict = matematica.which_level()


def one_min_competition():
    start_time = time.time()
    current = 0
    count_true = 0
    count_false = 0
    while time.time() - start_time < 60 :
        for item in dict:
            print(f"Solve: {item} : ")
            answer = int(input())
            if answer == dict[item] :
                count_true += 1
                print("CORRECT!")
            else :
                count_false += 1
        current += 1
#
#
#     print(f"In one minute you solved : {count_false+count_true} \n You solved {count_true} correctly.")
# pygame.font.init() # you have to call this at the start,
#                    # if you want to use this module.
#
#
# def one_min_competition():
#     start_time = time.time()
#     current = 0
#     count_true = 0
#     count_false = 0
#     my_font = pygame.font.SysFont('Comic Sans MS', 30)
#     user_text = ''
#     pygame.init()
#     size = (700, 500)
#     screen = pygame.display.set_mode(size)
#     while time.time() - start_time < 60 :
#         text_surface = my_font.render(f"Solve: {list1[current][0]} : ", False, (0, 0, 0))
#         screen.blit(text_surface, (0, 0))
#         # answer = int(input())
#         user_text = user_text[:-1]
#
#         if user_text == list1[current][1] :
#             count_true += 1
#             text_surface = my_font.render("Correct! ", False, (0, 0, 0))
#             screen.blit(text_surface, (0, 0))
#
#         else :
#             count_false += 1
#         current += 1
#
#     text_surface = my_font.render(f"In one minute you solved : {count_false+count_true} \n You solved {count_true} correctly.", False, (0, 0, 0))
#     screen.blit(text_surface, (0, 0))
#
# one_min_competition()