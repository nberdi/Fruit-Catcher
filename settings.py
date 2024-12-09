import pygame
pygame.init()

screen_width = 700
screen_height = 500
screen_bg_color = (172, 209, 175)   # light green

game_caption = "Fruit Catcher"

# fruit imgs
apple = pygame.image.load("imgs/apple.png")
banana = pygame.image.load("imgs/banana.png")
watermelon = pygame.image.load("imgs/watermelon.png")
strawberry = pygame.image.load("imgs/strawberry.png")
fruit_list = [apple, banana, strawberry, watermelon]

# bomb, heart, bomb, return to menu imgs
bomb_img = pygame.image.load("imgs/bomb.png")
heart_img = pygame.image.load("imgs/heart.png")
bucket_img = pygame.image.load("imgs/bucket.png")
return_to_menu = pygame.image.load("imgs/return_to_menu.png")

# game song control imgs
volume = pygame.image.load("imgs/volume.png")
mute = pygame.image.load("imgs/mute.png")

# sounds
game_song = "sounds/game_song.mp3"
bomb_sound = "sounds/bomb.mp3"
score_sound = "sounds/coin.mp3"
lost_life_sound = "sounds/lost_life.mp3"

rules_text = [
    "1. Move the bucket using LEFT and RIGHT arrow keys.",
    "2. Catch fruits to gain points.",
    "3. Avoid bombs! You lose a life if you hit one.",
    "4. Missing a fruit also costs you a life.",
    "5. The game ends when you lose all lives.",
]