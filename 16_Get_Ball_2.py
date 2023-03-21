import sys, pygame, random

class Ball:
    def __init__(self, x, y, redius, color):
        self.x = x
        self.y = y
        self.redius = redius
        self.color = color
        random_list = [-3, -2, -1, 1, 2, 3]
        self.speedx = random.choice(random_list)
        self.speedy = random.choice(random_list)
        print(f'self.x:{self.x}, self.y:{self.y}')
    def update(self, width, height, play_paddle):
        self.x += self.speedx
        self.y += self.speedy
        ball_top = self.y - self.redius
        ball_bottom = self.y + self.redius
        ball_left = self.x - self.redius
        ball_right = self.x + self.redius

        if ball_top < 0:
            self.speedy *= -1
        if ball_bottom > height:
            self.speedy *= -1
            self.reset(width, height)
        if ball_left < 0:
            self.speedx *= -1
        elif ball_right > width:
            self.speedx *= -1
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.redius)
    def reset(self, width, height):
        self.x = width / 2
        self.y = height / 2
        random_list = [-3, -2, -1, 1, 2, 3]
        self.speedx = random.choice(random_list)
        self.speedy = random.choice(random_list)
    def check_collide(self, play_paddle):
        play_paddle_top = play_paddle.y
        play_paddle_bottom = play_paddle.y + play_paddle.height
        play_paddle_left = play_paddle.x
        play_paddle_right = play_paddle.x + play_paddle.width

        ball_top = self.y - self.redius
        ball_bottom = self.y + self.redius
        ball_left = self.x - self.redius
        ball_right = self.x + self.redius
        print(f'ball_top:{ball_top}')
        print(f'ball_bottom:{ball_bottom}')
        print(f'ball_left:{ball_left}')
        print(f'ball_right:{ball_right}')

        print(f'play_paddle_top:{play_paddle_top}')
        print(f'play_paddle_bottom:{play_paddle_bottom}')
        print(f'play_paddle_left:{play_paddle_left}')
        print(f'play_paddle_right:{play_paddle_right}')
        print(f'self.speedy:{self.speedy}')
        # if self.speedy < 0:
        if ball_bottom > play_paddle_top and \
            ball_bottom < play_paddle_bottom and \
            ball_left < play_paddle_right and \
            ball_right > play_paddle_left:
            self.speedy *= -1
            self.speedx += random.randint(-2, 2)
            play_paddle.score += 1
            # play_Paddle.score += 1

class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speedy = 5
        self.speedx = 5
        self.score = 0
    def update(self, up, width):
        if up:
            self.x -= self.speedx
        else:
            self.x += self.speedx

        if self.x < 0:
            self.x = 0
        elif self.x + self.width > width:
            self.x = width - self.width
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

def paddle_move(keys, play_Paddle):
    if keys[pygame.K_LEFT]:
        play_Paddle.update(True, width)
    if keys[pygame.K_RIGHT]:
        play_Paddle.update(False, width)

def draw_score(screen, score):
    text = font.render(f'score:{score}', True, (255, 255, 255))
    screen.blit(text, (100, 20))

pygame.init()

# size = width, height = 500, 700
width = 500
height = 700
bg_color = (0, 0, 0)
FPS = 60
score = 0
screen = pygame.display.set_mode((width, height))
ball_redius = 18

ball = Ball(width/2, height/2, ball_redius, (200, 0, 0))
ball_2 = Ball(width/2, height/2, ball_redius, (0, 200, 0))
ball_3 = Ball(width/2, height/2, ball_redius, (0, 0, 200))

font = pygame.font.Font("myData//微軟正黑體.ttf", 36)
paddle_width = 100
paddle_height = 20
play_Paddle = Paddle(200, height-paddle_height, paddle_width, paddle_height, (255, 0, 0))

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    paddle_move(keys, play_Paddle)

    # game update
    ball.update(width, height, play_Paddle)
    ball.check_collide(play_Paddle)
    ball_2.update(width, height, play_Paddle)
    ball_2.check_collide(play_Paddle)
    ball_3.update(width, height, play_Paddle)
    ball_3.check_collide(play_Paddle)

    # window display
    screen.fill(bg_color)
    ball.draw(screen)
    ball_2.draw(screen)
    ball_3.draw(screen)
    play_Paddle.draw(screen)
    draw_score(screen, play_Paddle.score)
    pygame.display.update()
pygame.quit()