import pygame
import os

pygame.init()
clock = pygame.time.Clock() 
fps = 60

# Title
pygame.display.set_caption("Dino Game")
icon = pygame.image.load('assets/dinosaur.png')
pygame.display.set_icon(icon)

# Screen
dis = pygame.display.set_mode((600, 300))

# Background and character
bg = pygame.image.load('assets/background.jpg')
tree = pygame.image.load('assets/tree.png')
dinosaur = pygame.image.load('assets/dinosaur.png').convert_alpha()

# Sound
sound1 = pygame.mixer.Sound(r'sound/tick.wav')
sound2 = pygame.mixer.Sound(r'sound/te.wav')

# Collision
def collision(dino_rect, tree_rect):
    if dino_rect.colliderect(tree_rect):
        sound2.play()
        return False
    return True

# Position
bgX = 0
treeX = 550
dinoX = 70  # dinoX should not be 0, otherwise dino will not be visible
dinoY = 230
x_def = 5 
jump = False
gamePlay = True
score,hscore = 0,0
game_font = pygame.font.Font('04B_19.TTF', 20)
game_font2 = pygame.font.Font('04B_19.TTF', 40)
# Score 
def display_score():
    if gamePlay:
        score_surface = game_font.render(f'Score: {score}', True, (255, 0, 0))
        score_rect = score_surface.get_rect(center=(300, 50))
        dis.blit(score_surface, score_rect)
        hscore_surface = game_font.render(f'High Score: {hscore}', True, (255, 0, 0))
        hscore_rect = hscore_surface.get_rect(center=(500, 50))
        dis.blit(hscore_surface, hscore_rect)
    else: 
        txt_GO = game_font2.render('Game Over', True, (255, 0, 0))
        dis.blit(txt_GO, (250, 150))
        txt_con = pygame.font.Font('04B_19.TTF', 30).render('Press Space to Restart', True, (255, 0, 0))
        dis.blit(txt_con, (200, 200))
        


running = True
while running:
    clock.tick(fps)
    score += 1
    if score > hscore:
        hscore = score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound1.play()
                if gamePlay and dinoY == 230:
                    jump = True
                elif not gamePlay:
                    # Reset game to start
                    gamePlay = True
                    treeX = 550
                    dinoY = 230
                    bgX = 0

    if gamePlay:
        # Update background
        dis.blit(bg, (bgX, 0))
        dis.blit(bg, (bgX + 600, 0))
        bgX -= x_def
        if bgX <= -600:
            bgX = 0

        # Update tree
        dis.blit(tree, (treeX, 230))
        treeX -= x_def
        if treeX < -tree.get_width():
            treeX = 550

        # Update dinosaur
        if jump and dinoY >= 80:
                dinoY -= 7
        else:
                jump = False
        if dinoY < 230 and not jump:
                dinoY += 7

        dis.blit(dinosaur, (dinoX, dinoY))

        # Check collision
        dino_rect = dinosaur.get_rect(topleft=(dinoX, dinoY))
        tree_rect = tree.get_rect(topleft=(treeX, 230))
        gamePlay = collision(dino_rect, tree_rect)
    else:
        # Game over, display the end screen or a message
        # (This is where you'd put your game over screen logic)
        
        dis.blit(bg, (bgX, 0))
        dis.blit(tree, (treeX, 230))
        dis.blit(dinosaur, (dinoX, dinoY)) 
        score = 0
        
    
    display_score()
    pygame.display.update()

# Properly quit pygame when the loop is exited
pygame.quit()
