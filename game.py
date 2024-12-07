from settings import *
import random

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        
        # imgs
        self.bucket_img = pygame.transform.scale(bucket_img, (50, 50))
        self.bucket_x = 335  # center
        self.bucket_speed = 5
        
        self.fruit_imgs = [pygame.transform.scale(img, (40, 40)) for img in fruit_list]
        self.bomb_img = pygame.transform.scale(bomb_img, (40, 40))
        self.heart_img = pygame.transform.scale(heart_img, (30, 30))
        
        # time
        self.clock = pygame.time.Clock()
        self.last_fruit_time = 0
        self.fruit_interval = 1000
        self.fruit_speed = 1
        
        # new created fruits
        self.created_fruits = []
        
    def create_new_fruit(self):
        # create fruits every 1 second
        current_time = pygame.time.get_ticks()
        if current_time - self.last_fruit_time >= self.fruit_interval:
            is_bomb = random.random() < 0.2
            new_fruit = {
                "x": random.randint(0, 660),
                "y": 0,
                "img": self.bomb_img if is_bomb else random.choice(self.fruit_imgs),
            }
            self.created_fruits.append(new_fruit)
            self.last_fruit_time = current_time
        
        for fruit in self.created_fruits[:]:
            self.display_created_fruit(fruit)
            fruit["y"] += self.fruit_speed
        
                
    def display_created_fruit(self, fruit):
        self.screen.blit(fruit["img"], (fruit["x"], fruit["y"]))
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.bucket_x > 0:
            self.bucket_x -= self.bucket_speed
        if keys[pygame.K_RIGHT] and self.bucket_x < self.screen.get_width() - 50:
            self.bucket_x += self.bucket_speed
        
    def run(self):
        while True:
            
            self.screen.fill((172, 209, 175))
            
            # to move the bucket right and left
            self.move() 
            # display bucket
            self.screen.blit(self.bucket_img, (self.bucket_x, 450))
            
            # create a fruit and display on the screen
            self.create_new_fruit()
            
            self.clock.tick(120)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                    
if __name__ == "__main__":
    game = Game()
    game.run()