import pygame
import random
import sys

pygame.init()


WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 28, bold=True)



def reset_game():
    global bird_x, bird_y, velocity, pipe_x, pipe_height, game_over, score
    bird_x = 100
    bird_y = 400
    velocity = 0
    pipe_x = WIDTH
    pipe_height = random.randint(150, 450)
    score = 0
    game_over = False



bird_radius = 20
gravity = 0.6
pipe_width = 80
pipe_gap = 200

reset_game()

running = True
while running:
    clock.tick(75)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    reset_game()
                else:
                    velocity = -10


    if not game_over:

        velocity += gravity
        bird_y += velocity


        pipe_x -= 6
        if pipe_x < -pipe_width:
            pipe_x = WIDTH
            pipe_height = random.randint(150, 450)
            score += 1


        bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius * 2, bird_radius * 2)
        top_pipe = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
        bottom_pipe = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT)


        if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe) or bird_y > HEIGHT or bird_y < 0:
            game_over = True




    screen.fill((100, 200, 250))

    pygame.draw.rect(screen,(0,255,0),pygame.Rect(pipe_x,0,pipe_width,pipe_height))
    pygame.draw.rect(screen,(0,255,0,),pygame.Rect(pipe_x,pipe_height + pipe_gap,pipe_width,HEIGHT))




    pygame.draw.circle(screen,(255,255,0), (bird_x,int(bird_y)),bird_radius)


    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text,(15,15))

    if game_over:
        text1 = font.render("GAME OVER!", True, (255,0,0))
        text2 =  font.render("Press SPACE to play again", True, (0,0,0))
        screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 2 - 40))
        screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 + 10))

    pygame.display.flip()

pygame.quit()
sys.exit()


