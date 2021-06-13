import pygame
from pygame.locals import *


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode((500,500))
        self.surface.fill((100,155,80))  #color of window
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN: #keypress
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_LEFT:
                        self.snake.move_left()

                elif event.type == QUIT:
                    running = False

class Snake:
    def __init__(self, parent_screen) -> None:
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x, self.y = 100, 50
    
    def draw(self):
            self.parent_screen.fill((100,155,80))  #color of window. it also helps in clearing the screen before moving the block
            self.parent_screen.blit(self.block,(self.x,self.y))  #drawing block in position (x,y)
            pygame.display.flip()   #Applies it to window
    def move_up(self):
        self.y -= 10
        self.draw()
    def move_down(self):
        self.y += 10
        self.draw()
    def move_left(self):
        self.x -= 10
        self.draw()
    def move_right(self):
        self.x += 10
        self.draw()
        
        

if __name__ == "__main__":
    game = Game()
    game.run()

    
   

    
   

    pygame.display.flip()   #Applies it to window

