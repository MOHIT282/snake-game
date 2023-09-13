import pygame
import random

#initializing pygame
pygame.init()

#defining colors
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)

#Screen variables 
screen_width = 600
screen_height = 500

#window stats
window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("<----SNAKES GAME BY MOHIT KUMAR---->")
font = pygame.font.SysFont(None,30)
clock = pygame.time.Clock()

def show_score(text,color,x,y):
    screen_score = font.render(text,True,color)
    window.blit(screen_score,[x,y])
    
def draw_snake(color,snake_lst,snake_size):
    for x,y in snake_lst:
        pygame.draw.rect(window,color,[x,y,snake_size,snake_size]) 
        
def greet():
    game_exit = False
    while(game_exit == False):
        window.fill("white")
        show_score("Welcome to the Snakes Game",black,160,200)
        show_score("Press Space Bar to play",black,190,225)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()      
        pygame.display.update()
        clock.tick(60)
        
#creating the game loop
def game_loop():
    #game variables
    game_over = False
    game_closed = False
    snake_x = 50
    snake_y = 60
    speed_x = 0
    speed_y = 0

    food_x = random.randint(80,screen_width-80)
    food_y = random.randint(80,screen_height-80)
    snake_size = 10
    fps = 60
    score = 0
    snake_lst = []
    snake_length = 1
    with open("highscore.txt","r") as f:
        highscore = f.read()
    while(game_closed == False):
        
        if game_over == True:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            window.fill("pink")
            show_score("Game is over!",red,screen_width/2.7,screen_height/2.2)
            show_score("Press Enter to continue",red,screen_width/3.3,screen_height/2)
            
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    game_closed = True
                 
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_RETURN:
                        greet()  
        else: 
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    game_closed = True
                        
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_RIGHT:
                        speed_x = 2
                        speed_y = 0
                        
                    if events.key == pygame.K_LEFT:
                        speed_x = - 2
                        speed_y = 0
                        
                    if events.key == pygame.K_UP:
                        speed_y = - 2
                        speed_x = 0
                        
                    if events.key == pygame.K_DOWN:
                        speed_y = 2
                        speed_x = 0
            snake_x += speed_x
            snake_y += speed_y
            
            if abs(food_x -snake_x)<6 and abs(food_y-snake_y)<6:
                pygame.mixer.music.load("beep.mp3")
                pygame.mixer.music.play()
                food_x = random.randint(80,screen_width-80)
                food_y = random.randint(80,screen_height-80)
                score += 10
                snake_length += 5
                
            if score > int(highscore):
                highscore = score
                    
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_lst.append(head)
            if len(snake_lst)>snake_length:
                del snake_lst[0]
                
            window.fill('white')
            show_score(f"Score : {score}",blue,10,10)
            show_score(f"High-Score : {highscore}",blue,screen_width-160,10)
            draw_snake(green,snake_lst,snake_size)
            pygame.draw.rect(window,red,[food_x,food_y,snake_size,snake_size])
            
            if snake_x < 0 or snake_x > screen_width or snake_y <0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
            
            if head in snake_lst[:-1]:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                
        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()
    quit()
greet()