import pygame, sys, random
from timeit import default_timer as timer
import consts

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman!")
clock = pygame.time.Clock()
fps = 30
black, white = (0, 0, 0), (255, 255, 255)
lightred, darkred = (255, 165, 145), (200, 50, 50)
lightgrey, darkgrey = (200, 200, 200), (120, 120, 120)
darklightblue, lightblue = (42, 129, 255), (126, 178, 255)

def quitGame():
    pygame.quit()
    sys.exit()

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

def draw_hangman(chances):
    max_chances = 20
    parts = [
        lambda: pygame.draw.rect(screen, black, [450, 550, 100, 10]),
        lambda: pygame.draw.rect(screen, black, [550, 550, 100, 10]),
        lambda: pygame.draw.rect(screen, black, [650, 550, 100, 10]),
        lambda: pygame.draw.rect(screen, black, [500, 450, 10, 100]),
        lambda: pygame.draw.rect(screen, black, [500, 350, 10, 100]),
        lambda: pygame.draw.rect(screen, black, [500, 250, 10, 100]),
        lambda: pygame.draw.rect(screen, black, [500, 250, 150, 10]),
        lambda: pygame.draw.rect(screen, black, [600, 250, 100, 10]),
        lambda: pygame.draw.rect(screen, black, [600, 250, 10, 50]),
        lambda: pygame.draw.line(screen, black, [505, 505], [550, 550], 10),
        lambda: pygame.draw.line(screen, black, [550, 250], [505, 295], 10),
        lambda: pygame.draw.line(screen, black, [505, 505], [460, 550], 10),
        lambda: pygame.draw.circle(screen, black, [605, 325], 30),
        lambda: pygame.draw.rect(screen, black, [600, 350, 10, 60]),
        lambda: pygame.draw.rect(screen, black, [600, 410, 10, 60]),
        lambda: pygame.draw.line(screen, black, [605, 375], [550, 395], 10),
        lambda: pygame.draw.line(screen, black, [605, 375], [650, 395], 10),
        lambda: pygame.draw.line(screen, black, [605, 465], [550, 485], 10),
        lambda: pygame.draw.line(screen, black, [605, 465], [650, 485], 10),
    ]
    parts_to_draw = max(0, min(len(parts), max_chances - chances))
    for i in range(parts_to_draw):
        parts[i]()

def endGame(win, start_time):
    end_time = timer()
    message = "You won!" if win else "You lost!"
    message += f"  Time: {round(end_time - start_time)}s"
    done = False
    def back_to_menu():
        nonlocal done
        done = True
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        screen.fill(white)
        draw_text(message, 40, black, (width // 2, height // 2 - 100))
        button("Play Again", width // 2 - 75, 350, 150, 50, darkred, lightred, back_to_menu)
        button("Quit", width // 2 - 75, 420, 150, 50, darkred, lightred, quitGame)
        pygame.display.update()
        clock.tick(fps)
    return

def hangmanGame(words, title):
    word = random.choice(list(words)).lower()
    guessed = []
    wrong = []
    chances = 20
    start_time = timer()
    running = True
    def back():
        nonlocal running
        running = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                if pygame.K_a <= event.key <= pygame.K_z:
                    letter = chr(event.key)
                    if letter in guessed or letter in wrong:
                        pass
                    elif letter in word:
                        guessed.append(letter)
                    else:
                        wrong.append(letter)
                        chances -= 1
        screen.fill(white)
        draw_text(title, 40, black, (width // 2, 50))
        display_word = " ".join([c if c in guessed else "_" for c in word])
        draw_text(display_word, 50, black, (width // 2, 200))
        draw_text("Wrong: " + " ".join(wrong), 25, darkred, (width // 2, 300))
        draw_text(f"Chances left: {chances}", 25, black, (width // 2, 400))
        draw_hangman(chances)
        button("Back", 50, 50, 100, 50, darkgrey, lightgrey, back)
        if all(c in guessed for c in word):
            endGame(True, start_time)
            return
        if chances <= 0:
            endGame(False, start_time)
            return
        pygame.display.update()
        clock.tick(fps)


def hangman():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        screen.fill(white)
        draw_text("Choose a category", 40, black, (width // 2, height // 2 - 150))
        button("Easy", 150, 400, 150, 100, darkgrey, lightgrey,
               lambda: hangmanGame(consts.EASY_ENGLISH_DICT.keys(), "Easy"))
        button("Hard", 500, 400, 150, 100, darkgrey, lightgrey,
               lambda: hangmanGame(consts.HARD_ENGLISH_DICT.keys(), "Hard"))
        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    hangman()
