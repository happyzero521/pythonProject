import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __int__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
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


