import pygame
from pygame.locals import *
import time

SIZE = 40  #size of block
COLOR =  (100,155,80)

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode((500,500))
        self.surface.fill(COLOR)  #color of window
        self.snake = Snake(self.surface,3)
        self.snake.draw()
        self.sasuke = Sasuke(self.surface)
        self.sasuke.draw()

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
            self.play()
            time.sleep(0.2)
        
    def play(self):
        self.snake.walk()
        self.sasuke.draw()

class Snake:
    def __init__(self, parent_screen, length) -> None:
        self.parent_screen = parent_screen
        self.length = length
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x, self.y = [SIZE]*length, [SIZE]*length
        self.direction = 'right'
    
    def draw(self):
            self.parent_screen.fill(COLOR)  #color of window. it also helps in clearing the screen before moving the block
            for i in range(self.length):
                self.parent_screen.blit(self.block,(self.x[i],self.y[i]))  #drawing block in position (x,y)
            pygame.display.flip()   #Applies it to window
    def move_up(self):
        self.direction = 'up'
        
    def move_down(self):
        self.direction = 'down'
        
    def move_left(self):
        self.direction = 'left'
       
    def move_right(self):
        self.direction = 'right'
        

    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'up':
            self.y[0] -= SIZE
        elif self.direction == 'down':
            self.y[0] += SIZE
        elif self.direction == 'right':
            self.x[0] += SIZE
        elif self.direction == 'left':
            self.x[0] -= SIZE
       
        self.draw()
        


class Sasuke:
    def __init__(self, parent_Screen) -> None:
        self.parent_screen = parent_Screen
        self.image = pygame.image.load("resources/sasuke.png").convert()
        self.x, self.y = 120,120      #multiple of size

    def draw(self):
        self.parent_screen.blit(self.image,(self.x, self.y))
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()

    
   

    
   

    pygame.display.flip()   #Applies it to window

