import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Touch Counter Game")

# Set up the colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set up the circles
outer_circle_radius = 100
inner_circle_radius = 50
outer_circle_position = (screen_width // 2, screen_height // 2)
inner_circle_position = (screen_width // 2, screen_height // 2)
outer_circle_points = 2
inner_circle_points = 5

# Set up the counters
total_touch_counter = 0
outer_circle_touch_counter = 0
inner_circle_touch_counter = 0

# Set up the game mode
game_mode = "total_touch"  # or "time"

# Set up the game parameters
target_total_touch_count = 100
target_time = 5 * 60  # 5 minutes
start_time = pygame.time.get_ticks()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if outer_circle_radius >= inner_circle_radius:
                if pygame.mouse.get_pos() in pygame.draw.circle(screen, WHITE, outer_circle_position, outer_circle_radius):
                    total_touch_counter += 1
                    outer_circle_touch_counter += 1
                elif pygame.mouse.get_pos() in pygame.draw.circle(screen, WHITE, inner_circle_position, inner_circle_radius):
                    total_touch_counter += 1
                    inner_circle_touch_counter += 1
            else:
                if pygame.mouse.get_pos() in pygame.draw.circle(screen, WHITE, inner_circle_position, inner_circle_radius):
                    total_touch_counter += 1
                    inner_circle_touch_counter += 1
                elif pygame.mouse.get_pos() in pygame.draw.circle(screen, WHITE, outer_circle_position, outer_circle_radius):
                    total_touch_counter += 1
                    outer_circle_touch_counter += 1

    # Clear the screen
    screen.fill(BLACK)

    # Draw the circles
    pygame.draw.circle(screen, RED, outer_circle_position, outer_circle_radius)
    pygame.draw.circle(screen, GREEN, inner_circle_position, inner_circle_radius)

    # Update the counters
    font = pygame.font.Font(None, 36)
    total_touch_text = font.render("Total Touches: " + str(total_touch_counter), True, WHITE)
    outer_circle_text = font.render("Outer Circle: " + str(outer_circle_touch_counter * outer_circle_points), True, WHITE)
    inner_circle_text = font.render("Inner Circle: " + str(inner_circle_touch_counter * inner_circle_points), True, WHITE)
    screen.blit(total_touch_text, (10, 10))
    screen.blit(outer_circle_text, (10, 50))
    screen.blit(inner_circle_text, (10, 90))

    # Update the display
    pygame.display.update()

    # Check game over conditions
    if game_mode == "total_touch" and total_touch_counter >= target_total_touch_count:
        break
    elif game_mode == "time" and (pygame.time.get_ticks() - start_time) >= target_time * 1000:
        break

# Show the final score
final_score = total_touch_counter + (outer_circle_touch_counter * outer_circle_points) + (
        inner_circle_touch_counter * inner_circle_points)
font = pygame.font.Font(None, 48)
final_score_text = font.render("Final Score: " + str(final_score), True, WHITE)
screen.blit(final_score_text, (screen_width // 2 - final_score_text.get_width() // 2,
                               screen_height // 2 - final_score_text.get_height() // 2))
pygame.display.update()

# Wait for a while before quitting
pygame.time.wait(3000)

# Clean up the game
pygame.quit()