from settings import *
import random

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        
        # imgs
        self.bucket_img = pygame.transform.scale(bucket_img, (50, 50))
        self.bucket_speed = 5
        
        self.fruit_imgs = [pygame.transform.scale(img, (40, 40)) for img in fruit_list]
        self.bomb_img = pygame.transform.scale(bomb_img, (40, 40))
        self.heart_img = pygame.transform.scale(heart_img, (30, 30))
        
        # time
        self.clock = pygame.time.Clock()
        self.fruit_interval = 1000
        self.fruit_speed = 1
        
        # font for text
        self.font = pygame.font.SysFont(None, 36)
        self.header_font = pygame.font.SysFont(None, 72)
        
        self.reset_game()
        
    def reset_game(self):
        # new created fruits
        self.created_fruits = []
        self.last_fruit_time = 0
        self.bucket_x = 335  # center
        # score and lives 
        self.score = 0
        self.lives = 3
        # game over
        self.game_over = False
        
    def display_game_over(self):
        # game over text
        game_over_text = self.header_font.render("Game Over", True, (255, 255, 255))
        self.screen.blit(game_over_text, (225, 150))

        # final score
        final_score_text = self.font.render(f"Your Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(final_score_text, (275, 230))

        # restart button
        restart_text = self.font.render("Restart", True, (255, 255, 255))
        restart_rect = pygame.Rect(300, 300, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), restart_rect)
        self.screen.blit(restart_text, (310, 310))

        # quit button
        quit_text = self.font.render("Quit", True, (255, 255, 255))
        quit_rect = pygame.Rect(300, 370, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), quit_rect)
        self.screen.blit(quit_text, (322, 380))
        
        return restart_rect, quit_rect

    def check_collision(self, fruit):
        bucket_rect = pygame.Rect(self.bucket_x, 450, 50, 50)
        fruit_rect = pygame.Rect(fruit["x"], fruit["y"], 40, 40)
        return bucket_rect.colliderect(fruit_rect)
        
    def display_score_and_lives(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        for i in range(self.lives):
            self.screen.blit(self.heart_img, (10 + i * 35, 50))  # hearts under score
        
    def create_new_fruit(self):
        # create fruits every 1 second
        current_time = pygame.time.get_ticks()
        if current_time - self.last_fruit_time >= self.fruit_interval:
            is_bomb = random.random() < 0.2
            new_fruit = {
                "x": random.randint(0, 660),
                "y": 0,
                "img": self.bomb_img if is_bomb else random.choice(self.fruit_imgs),
                "is_bomb": is_bomb
            }
            self.created_fruits.append(new_fruit)
            self.last_fruit_time = current_time
        
        for fruit in self.created_fruits[:]:
            self.display_created_fruit(fruit)
            fruit["y"] += self.fruit_speed
            if self.check_collision(fruit):
                if fruit["is_bomb"]:
                    self.lives -= 1
                else:
                    self.score += 1
                self.created_fruits.remove(fruit)
            elif fruit["y"] > 500:
                self.created_fruits.remove(fruit)
                if not fruit["is_bomb"]:
                    self.lives -= 1

            if self.lives == 0:
                self.game_over = True     
        
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
            
            if not self.game_over:
                # display the bucket
                self.screen.blit(self.bucket_img, (self.bucket_x, 450))
                # to move the bucket right or left
                self.move() 
                
                # create a new fruit and display it on the screen
                self.create_new_fruit()
            
                # display score and lives
                self.display_score_and_lives()
            else:
                restart_rect, quit_rect = self.display_game_over()
                
            self.clock.tick(120)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                if self.game_over and event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_rect.collidepoint(mouse_pos):
                        self.reset_game()  # restart the game
                    if quit_rect.collidepoint(mouse_pos):
                        pygame.quit()
                    
                    
if __name__ == "__main__":
    game = Game()
    game.run()