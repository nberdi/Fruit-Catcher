from settings import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        
    def run(self):
        while True:
            
            self.screen.fill((172, 209, 175))
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                    
if __name__ == "__main__":
    game = Game()
    game.run()