import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化屏幕、设置和对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_width))
    pygame.display.set_caption("飞船游戏")
    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 创建存储子弹的编组
    bullets = Group
    # 设置游戏主循环
    while True:
        gf.check_events(ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
# 启动游戏程序
run_game()
