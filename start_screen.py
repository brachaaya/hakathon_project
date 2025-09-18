import pygame
import hangman_try
import flashcards
# import memorygame
# import math_competition

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game Menu Demo')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

color2 = (50, 120, 200)
color3 = (30, 90, 160)
color4 = (255, 255, 255)



class TextButton:
    def __init__(self, x, y, width, height, text, font, bg, fg, hover_bg, border_color, border_width=2):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.bg = bg
        self.fg = fg
        self.hover_bg = hover_bg
        self.border_color = border_color
        self.border_width = border_width
        self.clicked = False

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_bg, self.rect, border_radius=8)
            if mouse_pressed and not self.clicked:
                self.clicked = True
                return True
        else:
            pygame.draw.rect(surface, self.bg, self.rect, border_radius=8)

        if not mouse_pressed:
            self.clicked = False

        pygame.draw.rect(surface, self.border_color, self.rect, self.border_width, border_radius=8)

        text_surf = self.font.render(self.text, True, self.fg)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

        return False


def create_game_buttons(subject, font):
    buttons = []
    if subject == "English":
        games = ["hangman", "flashcards", "memory game", "connections"]
    elif subject == "Hebrew":
        games = ["flashcards", "memory game", "connections"]
    else:
        games = ["math competiton", "memory game", "connections"]
    start_y = 220
    for i, game in enumerate(games):
        btn = TextButton(SCREEN_WIDTH//2 - 100, start_y + i*80, 200, 60, game, font,
                         bg=color2, fg=color4, hover_bg=color3, border_color=color2)
        buttons.append(btn)
    return buttons


font = pygame.font.SysFont("Arial", 20, bold=True)

english_button = TextButton(SCREEN_WIDTH//2 - 250, 200, 160, 60, "English", font,
                            bg=color2, fg=color4, hover_bg=color3, border_color=color2)

hebrew_button = TextButton(SCREEN_WIDTH//2 - 80, 200, 160, 60, "Hebrew", font,
                           bg=color2, fg=color4, hover_bg=color3, border_color=color2)

math_button = TextButton(SCREEN_WIDTH//2 + 90, 200, 160, 60, "Math", font,
                         bg=color2, fg=color4, hover_bg=color3, border_color=color2)

game_state = "main_menu"
selected_subject = None
selected_level = None
game_buttons = []

run = True
while run:
    screen.fill(WHITE)

    if game_state == "main_menu":
        if english_button.draw(screen):
            selected_subject = "English"
            game_buttons = create_game_buttons(selected_subject, font)
            game_state = "game_menu"
        if hebrew_button.draw(screen):
            selected_subject = "Hebrew"
            game_buttons = create_game_buttons(selected_subject, font)
            game_state = "game_menu"
        if math_button.draw(screen):
            selected_subject = "Math"
            game_buttons = create_game_buttons(selected_subject, font)
            game_state = "game_menu"

    elif game_state == "game_menu":
        title_font = pygame.font.SysFont("Arial", 28, bold=True)
        text = title_font.render(f"{selected_subject} - {selected_level} | choose game", True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH//2, 150))
        screen.blit(text, text_rect)

        for btn in game_buttons:
            if btn.draw(screen):
                selected_game= btn.text
                if selected_game=="memory game":
                    game_state="memory_game"
                elif selected_game == "hangman":
                    game_state = "hangman"
                elif selected_game == "flashcards":
                    game_state = "flashcards"
                else:
                    game_state = "game_menu"

    elif game_state == "memory_game":
        title_font = pygame.font.SysFont("Arial", 28, bold=True)
        text = title_font.render("Memory game", True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH//2, 150))
        screen.blit(text, text_rect)
    elif game_state == "hangman":
        hangman_try.hangman()
    elif game_state == "flashcards":
        flashcards.main_menu()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
