import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5
FPS = 60
run = True
clock = pygame.time.Clock()
while run:
    # pygame.time.delay(100)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                print("UP")
                y -= 5
            elif event.key == pygame.K_DOWN or event.key == pygame.K_x:
                print("DOWN")
                y += 5
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("LEFT")
                x -= 5
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("RIGHT")
                x += 5
            elif event.key == pygame.K_e:
                print("RIGHT & UP")
                x += 5
                y -= 5
            elif event.key == pygame.K_q:
                print("LEFT & UP")
                x -= 5
                y -= 5
            elif event.key == pygame.K_c:
                print("RIGHT & DOWN")
                x += 5
                y += 5
            elif event.key == pygame.K_z:
                print("LEFT & DOWN")
                x -= 5
                y += 5
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.button)
            if event.button == 1:
                print('left')
                y -= vel
            else:
                print('right')
                y += vel
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()