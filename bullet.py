import pygame
from pygame.sprite import Sprite

# 管理发射子弹的类
class Bullet(Sprite):
    def __int__(self, ai_settings, screen, ship):
        # 在飞船所处的位置创建一个子弹对象
        super(Bullet, self).__init__()
        self.screen = screen
        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 用小数表示子弹的位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # 更新子弹位置的值
        self.y -= self.speed_factor
        # 更新子弹的rect的位置
        self.rect.y = self.y
        # 绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)

    # 在屏幕上绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
