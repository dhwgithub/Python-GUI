# 导入
import pygame
from pygame.color import THECOLORS

#参数准备
bird_x = 0
bird_y = 0
bird_speed_x = 5
bird_speed_y = 5

# 初始化
pygame.init()

# 创建一个窗口
screen = pygame.display.set_mode([800, 600])

# 用白色填充屏幕
screen.fill(THECOLORS['white'])

# 加载愤怒小鸟的图片，更新图像
pngFileName = r'E:\pycharm\python\pygame_learn\source\redBird.png'
birdRect = pygame.image.load(pngFileName)
screen.blit(birdRect,[bird_x, bird_y])

# 显示
pygame.display.flip()

# 主循环
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
    #时间延迟
    pygame.time.delay(20)
    #覆盖痕迹
    pygame.draw.rect(screen,THECOLORS['white'],[bird_x,bird_y,100,100],0)
    #小鸟的位置
    bird_x = bird_x + bird_speed_x
    bird_y = bird_y + bird_speed_y
    #小鸟碰壁后飞回
    if bird_x > 720 or bird_x < 0:
        bird_speed_x = -bird_speed_x
    if bird_y > 520 or bird_y < 0:
        bird_speed_y = -bird_speed_y
    screen.blit(birdRect,[bird_x, bird_y])
    pygame.display.flip()
pygame.quit()
