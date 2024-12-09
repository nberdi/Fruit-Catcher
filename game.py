from settings import *
import random

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(game_caption)
        
        # initialize mixer
        pygame.mixer.init()
        pygame.mixer.music.load(game_song)  # load your song
        pygame.mixer.music.set_volume(0.5)  # setting volume (0.0 to 1.0)
        
        # sounds
        self.bomb_sound = pygame.mixer.Sound(bomb_sound)
        self.score_sound = pygame.mixer.Sound(score_sound)
        self.lost_life_sound = pygame.mixer.Sound(lost_life_sound)
        
        # imgs
        self.bucket_img = pygame.transform.scale(bucket_img, (50, 50))
        self.bucket_speed = 5
        
        self.fruit_imgs = [pygame.transform.scale(img, (40, 40)) for img in fruit_list]
        self.bomb_img = pygame.transform.scale(bomb_img, (40, 40))
        self.heart_img = pygame.transform.scale(heart_img, (30, 30))
        
        self.return_to_menu_img = pygame.transform.scale(return_to_menu, (30, 30))
        self.return_to_menu = True

        self.volume = pygame.transform.scale(volume, (30, 30))
        self.mute = pygame.transform.scale(mute, (30, 30))
        self.is_mute = False
    
        # time
        self.clock = pygame.time.Clock()
        self.fruit_interval = 1000
        self.fruit_speed = 1
        
        # font for text
        self.font = pygame.font.SysFont(None, 36)
        self.header_font = pygame.font.SysFont(None, 72)
        
        self.highest_score = 0
                
        self.reset_game()
        
    def reset_game(self):
        self.created_fruits = []    # new created fruits
        self.last_fruit_time = 0
        self.bucket_x = 335  # center
        self.score = 0
        self.lives = 3
        self.game_over = False  # game over
    
    def show_start_screen(self):
        while True:
            self.screen.fill(screen_bg_color)   # bg color (light green)
            
            # header
            title = self.header_font.render(game_caption, True, (255, 255, 255))
            self.screen.blit(title, (195, 100))

            # start button
            start_text = self.font.render("Start", True, (255, 255, 255))
            start_rect = pygame.Rect(300, 220, 100, 50)
            pygame.draw.rect(self.screen, (0, 128, 255), start_rect)    # draw start btn with blue bg color
            self.screen.blit(start_text, (322, 233))    # put start_text on top of the btn

            # rules button
            rules_text = self.font.render("Rules", True, (255, 255, 255))
            rules_rect = pygame.Rect(300, 290, 100, 50)
            pygame.draw.rect(self.screen, (0, 128, 255), rules_rect)     # draw rules btn with blue bg color
            self.screen.blit(rules_text, (317, 303))    # put rules_text on top of the btn
            
            # mute the song
            volume_rect = pygame.Rect(650, 10, 30, 30)
            if not self.is_mute:
                self.screen.blit(self.volume, (650, 10))
            
            if self.is_mute:
                self.screen.blit(self.mute, (650, 10))                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_rect.collidepoint(event.pos):
                        return True
                    if rules_rect.collidepoint(event.pos):
                        self.show_rules_screen()
                    if volume_rect.collidepoint(event.pos):
                        self.is_mute = not self.is_mute
                        
                    # play the music in a loop
                    if self.is_mute:
                        pygame.mixer.music.stop()  # stop music
                    else:
                        pygame.mixer.music.play(-1)  

            pygame.display.update()

    def show_rules_screen(self):
        while True:
            self.screen.fill(screen_bg_color)   # bg color (light green)
            
            title_text = self.header_font.render("Game Rules", True, (255, 255, 255))
            self.screen.blit(title_text, (210, 50))

            # display each rule
            for i, rule in enumerate(rules_text):
                rule_text = self.font.render(rule, True, (255, 255, 255))
                self.screen.blit(rule_text, (30, 150 + i * 40))

            # back button
            back_text = self.font.render("Back", True, (255, 255, 255))
            back_rect = pygame.Rect(300, 400, 100, 50)
            pygame.draw.rect(self.screen, (0, 128, 255), back_rect) # draw back btn with blue bg color
            self.screen.blit(back_text, (322, 412)) # put back_text on top of the btn

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos):
                        return

            pygame.display.update()  

    def display_game_over(self):
        # game over text
        game_over_text = self.header_font.render("Game Over", True, (255, 255, 255))
        self.screen.blit(game_over_text, (225, 100))

        # final score
        final_score_text = self.font.render(f"Your Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(final_score_text, (275, 180))
        
        # highest score 
        highest_score_text = self.font.render(f"Highest Score: {self.highest_score}", True, (255, 255, 255))
        self.screen.blit(highest_score_text, (260, 230))

        # restart button
        restart_text = self.font.render("Restart", True, (255, 255, 255))
        restart_rect = pygame.Rect(300, 300, 100, 50)
        pygame.draw.rect(self.screen, (0, 128, 255), restart_rect)  # draw restart_text btn with blue bg color
        self.screen.blit(restart_text, (310, 310))  # put restart_text on top of the btn

        # quit button
        quit_text = self.font.render("Quit", True, (255, 255, 255))
        quit_rect = pygame.Rect(300, 370, 100, 50)
        pygame.draw.rect(self.screen, (0, 128, 255), quit_rect) # draw quit_text btn with blue bg color
        self.screen.blit(quit_text, (322, 380)) # put quit_text on top of the btn
        
        # return to menu
        self.screen.blit(self.return_to_menu_img, (660, 10))  # top right corner
        return_to_menu_rect = pygame.Rect(660, 10, 30, 30)
        
        return restart_rect, quit_rect, return_to_menu_rect

    def check_collision(self, fruit):
        bucket_rect = pygame.Rect(self.bucket_x, 450, 50, 50)
        fruit_rect = pygame.Rect(fruit["x"], fruit["y"], 40, 40)
        return bucket_rect.colliderect(fruit_rect)
        
    def display_score_and_lives(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        
        for i in range(self.lives):
            self.screen.blit(self.heart_img, (10 + i * 35, 50))  # hearts under score 
            
        self.screen.blit(self.return_to_menu_img, (660, 10))  # top right corner
        return_to_menu_rect = pygame.Rect(660, 10, 30, 30)
        
        # check if the left mouse button is pressed
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if mouse_buttons[0] and return_to_menu_rect.collidepoint(mouse_pos):  # left button and within rect
            return True
        
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
                    self.bomb_sound.play()
                    self.lives -= 1
                    self.lost_life_sound.play()
                else:
                    self.score_sound.play()
                    self.score += 1
                self.created_fruits.remove(fruit)
            elif fruit["y"] > 500:
                self.created_fruits.remove(fruit)
                if not fruit["is_bomb"]:
                    self.lost_life_sound.play()
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
        # play the music in a loop
        if not self.is_mute:
            pygame.mixer.music.play(-1)  
        else:
            pygame.mixer.music.stop()
        
        while True:
            self.screen.fill(screen_bg_color)   # bg color (light green)
            
            if self.return_to_menu:
                if self.show_start_screen():
                    self.reset_game()
                    self.return_to_menu = False
                    self.game_over = False
            
            if not self.game_over:
                # save highest score
                if self.score > self.highest_score:
                    self.highest_score = self.score
                    
                # display the bucket
                self.screen.blit(self.bucket_img, (self.bucket_x, 450))
                # to move the bucket right or left
                self.move() 
                
                # create a new fruit and display it on the screen
                self.create_new_fruit()
            
                # display score and lives
                if self.display_score_and_lives():
                    self.return_to_menu = True
                    self.game_over = True
            else:
                if not self.return_to_menu:
                    restart_rect, quit_rect, return_to_menu_rect = self.display_game_over()
                    
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
                    if return_to_menu_rect.collidepoint(mouse_pos):
                        self.return_to_menu = True


if __name__ == "__main__":
    game = Game()
    game.run()