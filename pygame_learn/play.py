#引入
import pygame
#初始化
pygame.init()
#设定窗口大小、标题、背景图片
size = width,height = 400,300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Canon')
pngFileName_3 = r'E:\pycharm\python\pygame_learn\source\music\bgWhale.png'
backGround = pygame.image.load(pngFileName_3)
screen.blit(backGround,[0,0])
#载入Canon音乐
mp3FileName = r'E:\pycharm\python\pygame_learn\source\music\CanonInD.mp3'
pygame.mixer.music.load(mp3FileName)
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
#给unpause赋予播放状态
unpause = False
#载入图片
pngFileName_1 = r'E:\pycharm\python\pygame_learn\source\music\unpause.png'
pngFileName_2 = r'E:\pycharm\python\pygame_learn\source\music\pause.png'
imgRect_1 = pygame.image.load(pngFileName_1)
imgRect_2 = pygame.image.load(pngFileName_2)
#设定按钮的位置
unpause_rect = imgRect_1.get_rect()
unpause_rect.left,unpause_rect.top = (0),(height - unpause_rect.height)
#创建Clock的实例
clock = pygame.time.Clock()
#主循环
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
        #鼠标按下事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            unpause = not unpause
        # 键盘按下事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                unpause = not unpause
        #播放
        if unpause:
            screen.blit(imgRect_1,unpause_rect)
            pygame.mixer.music.unpause()
        #暂停
        else:
            screen.blit(imgRect_2 ,unpause_rect)
            pygame.mixer.music.pause()
        #帧速率
        clock.tick(30)
        pygame.display.flip()
pygame.quit()