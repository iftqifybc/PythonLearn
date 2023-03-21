#pygame 動畫遊戲
# https://www.pygame.org/docs/
# pygame.Surface：Surface 資料型別，代表一個矩形的影像，用來繪製在螢幕上
# pygame.Rect：Rect 資料型別，用來定位矩形空間的位置和可以用來偵測物件是否碰撞的
# pygame.event：事件模組，用來處理使用者觸發事件，包含自定義事件
# pygame.font：文字模組，用來顯示文字，可用來顯示儀表板資料
# pygame.draw：繪圖模組，可以畫出多邊形圖形，可當作背景物件
# pygame.image：圖片模組，用來處理載入圖片等相關操作，可當作角色精靈（sprite）
# pygame.time：時間模組，包含控制遊戲迴圈迭代速率，確保反饋不會太快消逝
#動畫遊戲 基本架構
#畫圖形
#操控遊戲物件
#顥示文字

#  RGB 色碼表
#  http://www.wahart.com.hk/rgb.htm
import pygame, random

BG_COLOR = (139, 62, 47)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 640
HEIGHT = 480
FPS = 200

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('pygame base set')

clock = pygame.time.Clock()
x = 50
y = 50
random_list = [-2, -1]
speedx = random.choice(random_list)
speedy = random.choice(random_list)
ball_left = 0
ball_right = 0
ball_top = 0
ball_bottom = 0
ball_x = win.get_width() / 2
ball_y = win.get_height() / 2
ball_center = (ball_x, ball_y)
ball_radius = 25
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # game update
    # ball_x += speedx
    ball_y += speedy
    ball_center = (ball_x, ball_y)  # 移動球
    ball_left = ball_x - ball_radius
    ball_right = ball_x + ball_radius
    ball_top = ball_y - ball_radius
    ball_bottom = ball_y + ball_radius
    print(f'ball_center:{ball_center}')

    if ball_left < 0 or ball_right > WIDTH:
        speedx = speedx * -1
        print(f'speedx:{speedx}')
        print(f'ball_center:{ball_center}')
    if ball_top < 0 or ball_bottom > HEIGHT:
        speedy = speedy * -1

    # windows display
    win.fill((110, 139, 61))     # set background color
    pygame.draw.circle(win, (255, 0, 0), (ball_center), ball_radius)
    pygame.display.flip()
    # pygame.display.update()  # display windows
pygame.quit()