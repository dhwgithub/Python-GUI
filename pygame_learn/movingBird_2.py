#引入：
import pygame
import random
from pygame.color import THECOLORS

#创建个类：
class AngryBirdClass(pygame.sprite.Sprite):
    #初始化对象
    def __init__(self, image_file, location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        #得到定义图像边界的矩形
        self.rect = self.image.get_rect()
        #小鸟的初始位置
        self.rect.left,self.rect.top = location
        #创建速度属性
        self.speed = speed
    #增加运动方法
    def move(self):
        self.rect = self.rect.move(self.speed)
        #检测是否达到窗口边界
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
#设置窗口大小、颜色、载入图片
size = width,height = 800,600
screen = pygame.display.set_mode(size)
screen.fill(THECOLORS['white'])
img_file = r'E:\pycharm\python\pygame_learn\source\redBird.png'
#创建一个小鸟列表
birds = []
for row in range(0,2):
    for column in range(0,2):
        #每次循环都有一个不同的位置
        location = [column*180+10,row*180+10]
        #速度随机
        speed = [random.choice([-2,2]),random.choice([-2,2])]
        bird = AngryBirdClass(img_file,location,speed)
        #将各个小鸟添加到列表中
        birds.append(bird)
#主循环
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
    #时间延迟
    pygame.time.delay(20)
    screen.fill(THECOLORS['white'])
    for bird in birds:
            bird.move()
            screen.blit(bird.image,bird.rect)
    pygame.display.flip()
pygame.quit()