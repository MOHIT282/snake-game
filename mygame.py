from multiprocessing import Event
import pygame
pygame.init()

#Creating playing window
pygame.display.set_mode((1000,400))
pygame.display.set_caption("My First Game")

#Creating game variable
game_over = False
game_closed = False

#creating the game loop
while(game_over == False):
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            game_over = True
            
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_DOWN:
                print("Nothing")

pygame.quit()
quit()