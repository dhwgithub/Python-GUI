# 引入
import pygame
import random
from pygame.color import THECOLORS


# 定义小鸟类
class AngryBirdClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    # 动画函数
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]


def animate(group):
    screen.fill(THECOLORS['white'])
    # 先移动所有小鸟
    for bird in group:
        bird.move()
    # 将小鸟从组中删除
    for bird in group:
        group.remove(bird)
        # 检查碰撞
        if pygame.sprite.spritecollide(bird, group, False):
            bird.speed[0] = -bird.speed[0]
            bird.speed[1] = -bird.speed[1]
        # 将小鸟添加回原组
        group.add(bird)
        bird.move()
        screen.blit(bird.image, bird.rect)
    pygame.display.flip()


# 设置窗口大小、颜色、载入图片
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screen.fill(THECOLORS['white'])
img_file1 = r'E:\pycharm\python\pygame_learn\source\redBird.png'
img_file2 = r'E:\pycharm\python\pygame_learn\source\blueBird.png'
# 创建Clock的实例
clock = pygame.time.Clock()
# 创建小组
group = pygame.sprite.Group()
for row in range(0, 1):
    for column in range(0, 2):
        location = [column * 180 + 10, row * 180 + 10]
        speed = [random.choice([-3, 3]), random.choice([-5, 5])]
        bird = AngryBirdClass(img_file1, location, speed)
        group.add(bird)

for row in range(0, 2):
    for column in range(0, 1):
        location = [column * 180 + 100, row * 180 + 100]
        speed = [random.choice([-5, 5]), random.choice([-3, 3])]
        bird = AngryBirdClass(img_file2, location, speed)
        group.add(bird)
# 主循环
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
            # 检查帧速率
            frame_rate = clock.get_fps()
            print('frame rate =', frame_rate)
    animate(group)
    # 控制帧速率
    clock.tick(30)
pygame.quit()