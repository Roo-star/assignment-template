import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Interactive Game")


colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
current_color = random.choice(colors)


font = pygame.font.Font(None, 36)


x, y = 320, 240
dx, dy = 2, 0
gravity = 0.5
jump_strength = -10


expressions = ["0-0", "T_T", "Q_Q", "-w-"]
current_expression = random.choice(expressions)


pipe_image = pygame.image.load("C:\\Users\\Yingr\\my_repos\\pfad\\Assignment 3\\pipe.png")
pipe_image = pygame.transform.scale(pipe_image, (80, 20))
pipe_x = 280
pipe_y = 460


clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
           
            current_color = random.choice(colors)
            dy = jump_strength

   
    dy += gravity
    x += dx
    y += dy

   
    if x <= 0 or x >= 640:
        dx = -dx
        current_expression = random.choice(expressions)
    if y <= 0 or y >= 480:
        dy = -dy
        current_expression = random.choice(expressions)

    
    if pipe_x <= x <= pipe_x + 80 and y >= pipe_y:
        x, y = random.randint(0, 640), 0
        current_expression = random.choice(expressions)

    
    screen.fill(current_color)

    
    text_background = font.render("Press any key or click to jump", True, (50, 50, 50))
    screen.blit(text_background, (50, 50))

    
    pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 20)
    expression_text = font.render(current_expression, True, (0, 0, 0))
    screen.blit(expression_text, (int(x) - 10, int(y) - 10))

    
    screen.blit(pipe_image, (pipe_x, pipe_y))

    pygame.display.flip()

    
    clock.tick(60)


pygame.quit()