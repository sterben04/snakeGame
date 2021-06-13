import pygame
from pygame.locals import *
import time
import random

SIZE = 40  #size of block
COLOR =  (100,155,80)

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode((800,600))
        self.surface.fill(COLOR)  #color of window
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2  and x1 < x2+SIZE:
            if y1 >= y2 and y1 < y2+SIZE:
                return True
        return False


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
            time.sleep(0.18)
        
    def play(self):
        self.snake.walk()
        self.apple.draw()

        if self.is_collision(self.snake.x[0],self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_lenght()
            self.apple.move()


class Snake:
    def __init__(self, parent_screen, length) -> None:
        self.parent_screen = parent_screen
        self.length = length
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x, self.y = [SIZE]*length, [SIZE]*length
        self.direction = 'right'

        self.x = [SIZE]*length
        self.y = [SIZE]*length
    
    def draw(self):
            self.parent_screen.fill(COLOR)  #color of window. it also helps in clearing the screen before moving the block
            for i in range(self.length):
                self.parent_screen.blit(self.block,(self.x[i],self.y[i]))  #drawing block in position (x,y)
            pygame.display.flip()   #Applies it to window

    def increase_lenght(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

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
        


class Apple:
    def __init__(self, parent_Screen) -> None:
        self.parent_screen = parent_Screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x, self.y = 120,120      #multiple of size

    def draw(self):
        self.parent_screen.blit(self.image,(self.x, self.y))
        pygame.display.flip()

    def move(self):
        # window_size/size
        self.x, self.y = random.randint(0,20)*SIZE, random.randint(0,15)*SIZE

if __name__ == "__main__":
    game = Game()
    game.run()

    
   

    
   

    pygame.display.flip()   #Applies it to window

