import pygame
import sys
import consts



# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("flashcards!")
clock = pygame.time.Clock()
fps = 30
black, white = (0, 0, 0), (255, 255, 255)
lightred, darkred = (255, 165, 145), (200, 50, 50)
lightgrey, darkgrey = (200, 200, 200), (120, 120, 120)
darklightblue, lightblue = (42, 129, 255), (126, 178, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flashcard App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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

# Flashcard data
def flash_card(new_dict):
    flash_cards = []
    keys_list = list(new_dict.keys())
    values_list = list(new_dict.values())
    new_values = revese_words(values_list)
    for i in range(len(new_dict)):
        flash_cards.append({"question": keys_list[i], "answer": new_values[i]})
    return flash_cards






def draw_card(question_text, answer_text, show_answer_side):
    screen.fill(PINK) # Background color

    # Card rectangle
    card_rect = pygame.Rect(100, 100, SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200)
    pygame.draw.rect(screen, CARD_COLOR, card_rect)
    pygame.draw.rect(screen, BLACK, card_rect, 2) # Border

    # Text rendering
    text_to_display = answer_text if show_answer_side else question_text
    text_surface = font.render(text_to_display, True, BLACK)
    text_rect = text_surface.get_rect(center=card_rect.center)
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

def draw_text(text, size, color, center):
    font = pygame.font.Font("freesansbold.ttf", size)
    surf = font.render(text, True, color)
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


def flashcard():
    while True:
        for event in pygame.event.get():
            screen.fill(white)
            draw_text("Choose a category", 40, BLACK, (width // 2, height // 2 - 150))
            button("Easy", 150, 400, 150, 100, darkgrey, lightgrey,
                lambda: (consts.EASY_ENGLISH_DICT.keys(), "Easy"))
            button("Hard", 500, 400, 150, 100, darkgrey, lightgrey,
               lambda: flashCards(consts.HARD_ENGLISH_DICT.keys(), "Hard"))
            pygame.display.update()
            clock.tick(fps)


def flashCards(flashcards):
    current_card_index = 0
    show_answer = False
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_answer = not show_answer
                elif event.key == pygame.K_RIGHT:
                    current_card_index = (current_card_index + 1) % len(flashcards)
                    show_answer = False # Reset to question side
                elif event.key == pygame.K_LEFT:
                    current_card_index = (current_card_index - 1 + len(flashcards)) % len(flashcards)
                    show_answer = False # Reset to question side

        current_card = flashcards[current_card_index]
        draw_card(current_card["question"], current_card["answer"], show_answer)

    pygame.quit()
    sys.exit()