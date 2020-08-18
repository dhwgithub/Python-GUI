#引入
import pygame
from pygame.color import THECOLORS
#载入三种状态的图片
mangseng_images = [r'E:\pycharm\python\pygame_learn\source\盲僧\HeroMangSeng_Down.png',
                   r'E:\pycharm\python\pygame_learn\source\盲僧\HeroMangSeng_Right.png',
                   r'E:\pycharm\python\pygame_learn\source\盲僧\HeroMangSeng_Left.png']
#定义盲僧类
class MangSengClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'E:\pycharm\python\pygame_learn\source\盲僧\HeroMangSeng_Down.png')
        self.rect = self.image.get_rect()
        #以盲僧的中心来定义他的位置
        self.rect.center = [300,300]
        self.angle = 0
    #改变盲僧的方向
    def turn(self, direction):
        self.angle = self.angle + direction
        #限制盲僧的状态
        if self.angle > 1:
            self.angle = 1
        if self.angle < -1:
            self.angle = 1
        center = self.rect.center
        self.image = pygame.image.load(mangseng_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        #设定水平方向的速度
        speed = [self.angle,0]
        return speed
    #动画函数，限定盲僧在窗口内运动
    def move(self, speed):
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 50:
            self.rect.centerx = 50
        if self.rect.centerx > 550:
            self.rect.centerx = 550
#重绘屏幕
def animate():
    screen.fill(THECOLORS['white'])
    screen.blit(mangseng.image, mangseng.rect)
    pygame.display.flip()
#设置窗口大小、游戏名称、颜色、速度范围
pygame.init()
size = width,height = 600,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('盲僧')

musicFileName = r'E:\pycharm\python\pygame_learn\source\盲僧\bg_music.ogg'
pygame.mixer.music.load(musicFileName)
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

#创建Clock的实例
clock = pygame.time.Clock()
mangseng = MangSengClass()
speed = [0,6]
#主循环
running = True
while running:
    #控制帧速率
    clock.tick(30)
    #键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = mangseng.turn(-1)
            elif event.key == pygame.K_RIGHT:
                speed = mangseng.turn(1)
            elif event.key == pygame.K_SPACE:
                running = False;
    mangseng.move(speed)
    animate()
pygame.quit()