import pygame
pygame.init()

screen_width = 700
screen_height = 500

# bucket img
bucket_img = pygame.image.load("imgs/bucket.png")


# fruit imgs
apple = pygame.image.load("imgs/apple.png")
banana = pygame.image.load("imgs/banana.png")
watermelon = pygame.image.load("imgs/watermelon.png")
strawberry = pygame.image.load("imgs/strawberry.png")
# fruit list
fruit_list = [apple, banana, strawberry, watermelon]

# bomb img
bomb_img = pygame.image.load("imgs/bomb.png")

# heart img
heart_img = pygame.image.load("imgs/heart.png")
