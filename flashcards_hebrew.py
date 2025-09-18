import pygame
import sys
import consts
import random
# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("flashcards!")
clock = pygame.time.Clock()
fps = 30

# Colors
black, white = (0, 0, 0), (255, 255, 255)
lightred, darkred = (255, 165, 145), (200, 50, 50)
lightgrey, darkgrey = (200, 200, 200), (120, 120, 120)
darklightblue, lightblue = (42, 129, 255), (126, 178, 255)

PINK = (255, 105, 180)
CARD_COLOR = (255, 192, 203)

# Fonts
font = pygame.font.Font("ARIAL.TTF", 48)

def revese_words(values_string):
    new_words = []
    for i in values_string:
        i = i[::-1]
        new_words.append(i)
    return new_words

# Flashcard data builder
def flash_card(new_dict):
    flash_cards = []
    keys_list = list(new_dict.keys())
    new_keys= revese_words(keys_list)
    values_list = list(new_dict.values())
    new_values = revese_words(values_list)
    for i in range(len(new_dict)):
        flash_cards.append({"question": new_keys[i], "answer": new_values[i]})
    return flash_cards

def draw_card(question_text, answer_text, show_answer_side):
    screen.fill(PINK)  # Background color

    # Card rectangle
    card_rect = pygame.Rect(100, 100, width - 200, height - 200)
    pygame.draw.rect(screen, CARD_COLOR, card_rect)
    pygame.draw.rect(screen, black, card_rect, 2)  # Border

    # Text rendering
    text_to_display = answer_text if show_answer_side else question_text
    text_surface = font.render(text_to_display, True, black)
    text_rect = text_surface.get_rect(center=card_rect.center)
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

def draw_text(text, size, color, center):
    font2 = pygame.font.Font("freesansbold.ttf", size)
    surf = font2.render(text, True, color)
    rect = surf.get_rect(center=center)
    screen.blit(surf, rect)
    return rect

def button(text, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    color = ac if (x < mouse[0] < x + w and y < mouse[1] < y + h) else ic
    pygame.draw.rect(screen, color, (x, y, w, h))
    draw_text(text, 25, white, (x + w // 2, y + h // 2))
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        if click[0] and action:
            action()

def main_menu():
    menu_running = True

    easy_flashcard = flash_card(consts.EASY_HEBREW_DICT)
    hard_flashcard = flash_card(consts.HARD_HEBREW_DICT)
    random.shuffle(easy_flashcard)
    random.shuffle(hard_flashcard)

    while menu_running:
        screen.fill(white)
        draw_text("Choose a level", 40, black, (width // 2, height // 2 - 150))

        button("Easy", 150, 400, 150, 100, darkgrey, lightgrey,
               lambda: start_flashcards(easy_flashcard))
        button("Hard", 500, 400, 150, 100, darkgrey, lightgrey,
               lambda: start_flashcards(hard_flashcard))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(fps)

# ----------------- FLASHCARDS -----------------
def start_flashcards(flashcards):
    current_card_index = 0
    show_answer = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_answer = not show_answer
                elif event.key == pygame.K_RIGHT:
                    current_card_index = (current_card_index + 1) % len(flashcards)
                    show_answer = False
                elif event.key == pygame.K_LEFT:
                    current_card_index = (current_card_index - 1 + len(flashcards)) % len(flashcards)
                    show_answer = False
                elif event.key == pygame.K_ESCAPE:
                    running = False  # חזרה לתפריט

        current_card = flashcards[current_card_index]
        draw_card(current_card["question"], current_card["answer"], show_answer)
    main_menu()

if __name__ == "__main__":
    main_menu()
