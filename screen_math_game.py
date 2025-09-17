import pygame
import random
import time
import requests
from io import BytesIO
from PIL import Image

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
CARD_SIZE = 175
GRID_SIZE = 4
WHITE = (255, 255, 255)
FLIP_DELAY = 0.5
BUTTON_WIDTH = 140
BLACK = (0, 0, 0)
BUTTON_HEIGHT = 40
TIMER_LIMIT = 15

# URLs for images
image_urls = [
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120810/f.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311121011/d.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120802/a.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120802/b.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120801/c.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311122347/z.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311122913/y.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311122913/x.webp"
]

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Puzzle Game")

# Load card back image from URL and convert to PNG format
response = requests.get(
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311145552/geeksforgeeks.png")
image = Image.open(BytesIO(response.content))
image = image.convert("RGB")
with BytesIO() as img_bytes:
    image.save(img_bytes, "PNG")
    img_bytes.seek(0)
    card_back = pygame.image.load(img_bytes)

# Load card images from URLs and convert to PNG format
card_images = []
for url in image_urls:
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = image.convert("RGB")
    with BytesIO() as img_bytes:
        image.save(img_bytes, "PNG")
        img_bytes.seek(0)
        card_images.append(pygame.image.load(img_bytes))

# Duplicate card images to create pairs
card_images *= 2

# Shuffle the cards
random.shuffle(card_images)

# Create a list to store the state of each card (True: face-up, False: face-down)
card_state = [False] * (GRID_SIZE ** 2)

# Variables to keep track of flipped cards, matched pairs, moves, and timer
flipped_cards = []
matched_pairs = 0
moves = 0
timer_start_time = time.time()

# Font for displaying text
font = pygame.font.Font(None, 36)

# Function to check if a point is within a rectangle


def point_in_rect(point, rect):
    x, y = point
    rx, ry, rw, rh = rect
    return rx < x < rx + rw and ry < y < ry + rh

# Function to draw restart game button


def draw_restart_button():
    restart_button_rect = (SCREEN_WIDTH - BUTTON_WIDTH -
                           20, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, WHITE, restart_button_rect)
    # Specify text color (black)
    restart_text = font.render("Restart Game", True, (0, 0, 0))
    text_rect = restart_text.get_rect(center=(
        restart_button_rect[0] + BUTTON_WIDTH / 2, restart_button_rect[1] + BUTTON_HEIGHT / 2))
    screen.blit(restart_text, text_rect)

# Function to draw timer


def draw_timer():
    elapsed_time = max(0, int(time.time() - timer_start_time))
    remaining_time = max(0, TIMER_LIMIT - elapsed_time)
    timer_text = font.render(f"Time: {remaining_time}s", True, BLACK)
    screen.blit(timer_text, (SCREEN_WIDTH - 150, 10))

# Function to display message on the window


def display_message(message):
    message_text = font.render(message, True, BLACK)
    text_rect = message_text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(message_text, text_rect)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            restart_button_rect = (
                SCREEN_WIDTH - BUTTON_WIDTH - 20, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
            if point_in_rect((mouse_x, mouse_y), restart_button_rect):
                random.shuffle(card_images)
                card_state = [False] * (GRID_SIZE ** 2)
                flipped_cards = []
                matched_pairs = 0
                moves = 0
                timer_start_time = time.time()  # Restart the timer
            else:
                col = mouse_x // CARD_SIZE
                row = mouse_y // CARD_SIZE
                index = row * GRID_SIZE + col
                if not card_state[index] and len(flipped_cards) < 2:
                    card_state[index] = True
                    flipped_cards.append(index)
                    moves += 1

    screen.fill(WHITE)

    # Draw grid of cards
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            index = i * GRID_SIZE + j
            pygame.draw.rect(screen, WHITE, (j * CARD_SIZE,
                                             i * CARD_SIZE, CARD_SIZE, CARD_SIZE))
            if card_state[index] or index in flipped_cards:
                card = card_images[index]
            else:
                card = card_back
            card = pygame.transform.scale(card, (CARD_SIZE - 8, CARD_SIZE - 8))
            screen.blit(card, (j * CARD_SIZE + 4, i * CARD_SIZE + 4))

    # Render moves counter
    moves_text = font.render(f"Moves: {moves}", True, WHITE)
    screen.blit(moves_text, (10, 10))

    # Draw restart game button
    draw_restart_button()

    # Draw timer
    draw_timer()

    # Check for matched pairs
    if len(flipped_cards) == 2:
        time.sleep(FLIP_DELAY)
        if card_images[flipped_cards[0]] == card_images[flipped_cards[1]]:
            matched_pairs += 1
            flipped_cards = []
        else:
            card_state[flipped_cards[0]] = False
            card_state[flipped_cards[1]] = False
            flipped_cards = []

    # Check for game over
    if matched_pairs == GRID_SIZE ** 2 // 2:
        display_message("Congratulations! You found all the pairs!")
        pygame.display.flip()
        time.sleep(2)  # Display the message for 2 seconds
        running = False

    # Check for time limit reached
    elapsed_time = time.time() - timer_start_time
    if elapsed_time >= TIMER_LIMIT:
        display_message("Time's up! You lost the game.")
        pygame.display.flip()
        time.sleep(2)  # Display the message for 2 seconds
        running = False

    pygame.display.flip()

pygame.quit()

