import pygame
import random
class Ball:
    def __init__(self, x, y, redius, color):
        self.x = x
        self.y = y
        self.redius = redius
        self.color = color
        random_list = [-3, -2, -1, 1, 2, 3]
        self.speedx = random.choice(random_list)
        self.speedy = random.choice(random_list)
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
            play_paddle.score += 1
            # self.reset(width, height)
        if ball_left < 0:
            self.speedx *= -1
        elif ball_right > width:
            self.speedx *= -1
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.redius)
    def reset(self, width, height):
        self.x = width / 2
        self.y = height / 2
        random_list = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        self.speedx = random.choice(random_list)
        self.speedy = random.choice(random_list)
    def check_collide(self, play_paddle):
        play_paddle_top = play_paddle.y
        play_paddle_bottom = play_paddle.y + play_paddle.height
        play_paddle_left = play_paddle.x
        play_paddle_right = play_paddle.x + play_paddle.width

        if self.speedx < 0:
            ball_x = self.x - self.redius
            ball_y = self.y
            print(f'ball_x:{ball_x}')
            print(f'ball_y:{ball_y}')
            print(f'play_paddle_top:{play_paddle_top}')
            print(f'play_paddle_bottom:{play_paddle_bottom}')
            print(f'play_paddle_left:{play_paddle_left}')
            print(f'play_paddle_right:{play_paddle_right}')
            print(f'ball_x:{self.x - self.redius}')
            print(f'ball_y:{self.y}')

            if play_paddle_top > ball_y and \
                play_paddle_bottom > ball_y and \
                play_paddle_left > ball_x and \
                play_paddle_right < ball_x:
                print(f'Hi')
                self.speedx *= -1
                self.speedy += random.randint(-2, 2)
        # else:
        #     ball_right_x = self.x + self.redius
        #     ball_right_y = self.y
        #     if play_paddle_top < ball_right_y and \
        #         play_paddle_bottom > ball_right_y and \
        #         play_paddle_left < ball_right_x and \
        #         play_paddle_right > ball_right_x:
        #         self.speedx *= -1
        #         self.speedy += random.randint(-2, 2)

