# 导入Pygame
import pygame
from pygame.color import THECOLORS
import math

# 初始化
pygame.init()

# 生成一个窗口
screen = pygame.display.set_mode([600, 400])

# 将白色铺满整个窗口
screen.fill(THECOLORS['white'])

# 添加蓝色与红色区域
pygame.draw.rect(screen, THECOLORS['blue'], [0, 0, 200, 400], 0)
pygame.draw.rect(screen, THECOLORS['red'], [400, 0, 200, 400], 0)

# 圆
pygame.draw.circle(screen, THECOLORS['green'], [300, 200], 90, 0)


# 八卦图
pygame.draw.circle(screen,THECOLORS['black'],[300,300],300,0)
pygame.draw.rect(screen, THECOLORS['white'],[0,300,600,300],0)
pygame.draw.circle(screen,THECOLORS['black'],[150,300],150,0)
pygame.draw.circle(screen,THECOLORS['white'],[450,300],150,0)
pygame.draw.circle(screen,THECOLORS['white'],[125,300],50,0)
pygame.draw.circle(screen,THECOLORS['black'],[475,300],50,0)
pygame.draw.arc(screen,THECOLORS['black'],[0,0,600,600],math.pi,2*math.pi,1)

# 椭圆
pygame.draw.ellipse(screen,THECOLORS['blue'],[150,100,300,75],0)

# 曲线
plotPoints = []
for x in range(0,600):
    y = int(math.cos(x/200.0 * 1 * math.pi) *50)+350
    plotPoints.append([x, y])
pygame.draw.aalines(screen, THECOLORS['red'],False, plotPoints, 1)

# 显示
pygame.display.flip()

#主循环&保存
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(screen, 'FranceFlag.jpg')
            mRunning = False
pygame.quit()
