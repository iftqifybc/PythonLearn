import pygame

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
    def update(self, up, height):
        if up:
            self.y -= self.speedy
        else:
            self.y += self.speedy

        if self.y < 0:
            self.y = 0
        elif self.y + self.height > height:
            self.y = height - self.height
    def update_x(self, up, width):
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
